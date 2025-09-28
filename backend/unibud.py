''' Mr. Unibud's Functionality - Received requests from frontend and sends it, with the kg as context, to Gemini for a response 
Uses a Hybrid GraphRag system, using Neo4j's native vector index with a brief cypher expansions 
'''

import os
from query_utils import get_driver, load_dotenv_automatically, fetch_all_relations
load_dotenv_automatically()

# Quiting goofy ahh warnings
os.environ.setdefault("GRPC_VERBOSITY", "ERROR")
os.environ.setdefault("GRPC_TRACE", "")

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from typing import List

import os, google.generativeai as genai
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
for m in genai.list_models():
    if "generateContent" in getattr(m, "supported_generation_methods", []):
        print(m.name)

# Initialize the LLM with Gemini API key
API_KEY: str = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set")

embedding = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004", 
    api_key=API_KEY
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0,
    api_key=API_KEY
)

# Pull in the neo4j driver instance
driver = get_driver()

# Get all relations from the database
all_relations = fetch_all_relations()

# Create a text view for the LLM
def text_view(n_props, labels):
    ''' Create a text view for the LLM from node properties and labels '''
    name = n_props.get("name") or n_props.get("id") or "Unknown"
    desc = n_props.get("description") or ""
    return f"{name} ({', '.join(labels)}): {desc}"

# Adding embeddings to all Doc nodes and creating a vector index
def ensure_vector_index(session):
    # Guard index creation to avoid "EquivalentSchemaRuleAlreadyExists"
    existing = session.run("SHOW INDEXES WHERE name = $name", {"name": "node_vec_idx"}).data()
    if not existing:
        session.run("""
        CREATE VECTOR INDEX node_vec_idx
        FOR (n:Doc) ON (n.embedding)
        OPTIONS {
          indexConfig: {
            `vector.dimensions`: 768,
            `vector.similarity_function`: 'cosine'
          }
        }
        """)
        # Optionally wait for ONLINE:
        session.run("CALL db.awaitIndexes()")

def backfill_embeddings():
    '''Run this ONCE (or behind an admin endpoint/CLI), not at import time'''
    with driver.session() as session:
        # Add/refresh embeddings for Doc nodes that are missing them
        recs = session.run("""
            MATCH (n:Doc)
            WHERE n.embedding IS NULL
            RETURN elementId(n) AS eid, labels(n) AS labs, n AS n
        """)
        for r in recs:
            vec = embedding.embed_query(text_view(r["n"]._properties, r["labs"]))
            session.run("""
                MATCH (n) WHERE elementId(n) = $eid
                SET n.embedding = $e
            """, {"eid": r["eid"], "e": vec})

        ensure_vector_index(session)
    
def ask(q: str):
    qv = embedding.embed_query(q)

    with driver.session() as s:
        recs = s.run("""
        WITH $qv AS qv
        CALL db.index.vector.queryNodes('node_vec_idx', 12, qv) YIELD node, score
        WITH collect(elementId(node))[0..6] AS seeds, $rels AS rels
        MATCH p=(s)-[r*1..2]-(m)
        WHERE elementId(s) IN seeds AND all(x IN r WHERE type(x) IN rels)
        WITH nodes(p) AS ns, relationships(p) AS rs
        UNWIND ns AS n
        UNWIND rs AS rel
        RETURN DISTINCT elementId(n) AS nid, labels(n) AS labs, n AS n,
            elementId(startNode(rel)) AS src, type(rel) AS rt, elementId(endNode(rel)) AS dst
        LIMIT 1200
        """, {"qv": qv, "rels": all_relations})

        nodes, edges = {}, []
        for r in recs:
            nid = r["nid"]
            if nid not in nodes:
                nodes[nid] = {"labels": r["labs"], **r["n"]._properties}
            edges.append((r["src"], r["rt"], r["dst"]))

    def tag(nid):
        n = nodes[nid]; lbl = n["labels"][0] if n["labels"] else "Node"
        name = n.get("name") or n.get("title") or str(nid)
        return f"{lbl}:{name}"

    triples = []
    for s_id, rel, t_id in edges[:300]:
        triples.append(f"({tag(s_id)}) -[{rel}]-> ({tag(t_id)})")

    prompt = f"GRAPH FACTS:\n" + "\n".join(triples) + f"\n\nQUESTION: {q}\nAnswer using only GRAPH FACTS. If there are none, just give a very general answer.'"
    reply = llm.invoke(prompt).content
    return reply
''' Mr. Unibud's Functionality - Received requests from frontend and sends it, with the kg as context, to Gemini for a response 
Uses a Hybrid GraphRag system, using Neo4j's native vector index with a brief cypher expansions 
'''

from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from typing import List
from query_utils import get_driver, load_dotenv_automatically, fetch_all_relations
import os

# Initialize the LLM with Gemini API key
load_dotenv_automatically()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-1.5-flash", 
    temperature=0,
    api_key=GEMINI_API_KEY
)
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    api_key=os.GEMINI_API_KEY
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
with driver.session() as session:
    # Adding embeddings
    recs = session.run("MATCH (n:Doc) RETURN id(n) AS id, labels(n) AS labs, n AS n")
    for r in recs:
        v = embedding.embed_query(text_view(r["n"]._properties, r["labs"]))
        session.run("MATCH (n) WHERE id(n)=$id SET n.embedding=$e", {"id": r["id"], "e": v})

    # Creating vector index
    session.run("""
    CREATE VECTOR INDEX node_vec_idx
    FOR (n:Doc) ON (n.embedding)
    OPTIONS {indexConfig: {`vector.dimensions`: 768, `vector.similarity_function`: 'cosine'}};
    """)
    
    def ask(q: str):
        qv = embedding.embed_query(q)
    
        with driver.session() as s:
            recs = s.run("""
            WITH $qv AS qv
            CALL db.index.vector.queryNodes('node_vec_idx', 12, qv) YIELD node, score
            WITH collect(id(node))[0..6] AS seeds, $rels AS rels
            MATCH p=(s)-[r*1..2]-(m)
            WHERE id(s) IN seeds AND all(x IN r WHERE type(x) IN rels)
            WITH nodes(p) AS ns, relationships(p) AS rs
            UNWIND ns AS n
            UNWIND rs AS rel
            RETURN DISTINCT id(n) AS nid, labels(n) AS labs, n AS n,
                id(startNode(rel)) AS src, type(rel) AS rt, id(endNode(rel)) AS dst
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

        prompt = f"GRAPH FACTS:\n" + "\n".join(triples) + f"\n\nQUESTION: {q}\nAnswer using only GRAPH FACTS. IF YOU ARE UNSURE, \
        GIVE A VERY BRIEF GENERAL RESPONSE AND BE LIGHT. DO NOT MAKE UP FACTS. IF THE QUESTION IS NOT ABOUT THE UNIVERSITY, SAY 'I AM UNIBUD, YOUR UNIVERSITY BUDDY! I CANNOT ANSWER THAT.'"
        return llm.invoke(prompt).content
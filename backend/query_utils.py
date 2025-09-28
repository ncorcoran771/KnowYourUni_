''' Tons of utility functions for querying the neo4j backend '''

from neo4j import GraphDatabase, basic_auth
import os
from dotenv import load_dotenv
from pathlib import Path

def load_dotenv_automatically():
    ''' Automatically load .env file from the same directory as this script '''
    script_dir = Path(__file__).resolve().parent
    dotenv_path = script_dir / '.env'
    if dotenv_path.exists():
        load_dotenv(dotenv_path=dotenv_path)
    else:
        raise FileNotFoundError(f".env file not found in {script_dir}")

# Call the function to load environment variables
load_dotenv_automatically()

# Connecting to Neo4j and setting up the driver
name = os.getenv('NEO4J_NAME')
NEO4J_URI = f"neo4j+s://{name}.databases.neo4j.io"
NEO4J_AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)

# --------- Validating student ID ---------
def validate_student_id(student_id: str) -> bool:
    ''' Validate if a student ID exists in the database '''
    with driver.session() as session:
        result = session.run(
            "MATCH (s:Student {id: $student_id}) RETURN s LIMIT 1",
            student_id=student_id
        )
        return result.single() is not None
    
# --------- Fetching data for a specific student ---------
def fetch_student_data(student_id: str) -> dict:
    ''' Fetch all nodes and relationships for a specific student '''
    with driver.session() as session:
        result = session.run(
            """
            MATCH (s:Student {id: $student_id})-[r]-(n)
            RETURN s, collect(r) AS relationships, collect(n) AS nodes
            """,
            student_id=student_id
        )
        record = result.single()
        if record:
            nodes = [record["s"]] + record["nodes"]
            relationships = record["relationships"]
            return {
                "nodes": [dict(node) for node in nodes],
                "relationships": [dict(rel) for rel in relationships]
            }
        return {"nodes": [], "relationships": []}
    

# --------- Fetching all relationships in the knowledge graph ---------
def fetch_all_relations() -> dict:
    ''' Fetch all unique relationship types in the KG to allow filtering'''
    with driver.session() as session:
        result = session.run(
            """
            MATCH ()-[r]->()
            RETURN DISTINCT TYPE(r) AS relationships
            """
        )
        return [record["relationships"] for record in result]
    
# --------- Fetch nodes in a specified relation to display later ---------
def fetch_graph(relation: str, max: int) -> dict:
    ''' Fetch nodes and relationshios of a specified relatyion type'''
    with driver.session() as session:
        # select maximum number of nodes/relationships to return
        result = session.run(
            f"""
            MATCH (n)-[r:{relation}]-(m)
            RETURN n, r, m
            LIMIT $max
            """,
            max=max
        )
        nodes_map = {}
        edges = []

        for record in result:
            n = record["n"]
            m = record["m"]
            r = record["r"]

        #add nodes
        for node in [n, m]:
                if node.id not in nodes_map:
                    nodes_map[node.id] = {
                        "data": {
                            "id": str(node.id),
                            "label": node.get("name", f"Node-{node.id}")
                        }
                    }
        #add edges
        edges.append(
            {
                "data": {
                    "source": str(n.id),
                    "target": str(m.id),
                    "label": type(r).__name__
                }
            }
        )

        return list(nodes_map.values()), edges;


# --------- Fetching all data in the knowledge graph ---------
def fetch_full_kg_data() -> dict:
    ''' Fetch all nodes and relationships in the knowledge graph '''
    with driver.session() as session:
        result = session.run(
            """
            MATCH (n)-[r]-(m)
            RETURN collect(DISTINCT n) AS nodes, collect(DISTINCT r) AS relationships
            """
        )
        record = result.single()
        if record:
            nodes = record["nodes"]
            relationships = record["relationships"]
            return {
                "nodes": [dict(node) for node in nodes],
                "relationships": [dict(rel) for rel in relationships]
            }
        return {"nodes": [], "relationships": []}
    


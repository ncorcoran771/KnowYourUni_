''' Tons of utility functions for querying the neo4j backend '''

import math
from time import time
from datetime import datetime, date, time
from typing import List

from neo4j import GraphDatabase, basic_auth, Driver
from neo4j.exceptions import Neo4jError
import os
from dotenv import load_dotenv
from pathlib import Path
from utils import to_plain

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

# --------- Returning the driver instance ---------
def get_driver():
    ''' Return the Neo4j driver instance for the LLM instance '''
    return driver

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
    """Fetch all nodes and relationships connected to a specific student (JSON-ready)."""
    cypher = """
    MATCH (s:Student {id: $student_id})
    OPTIONAL MATCH (s)-[r]-(n)
    WITH s, collect(DISTINCT n) AS ns, collect(DISTINCT r) AS rs
    RETURN
      { id: elementId(s), labels: labels(s), props: properties(s) } AS student,
      [n IN ns | { id: elementId(n), labels: labels(n), props: properties(n) }] AS nodes,
      [rel IN rs | {
        id: elementId(rel),
        type: type(rel),
        start: elementId(startNode(rel)),
        end: elementId(endNode(rel)),
        props: properties(rel)
      }] AS relationships
    """
    with driver.session() as session:
        rec = session.run(cypher, student_id=student_id).single()
        if not rec:
            # student not found
            return {"student": None, "nodes": [], "relationships": []}
        data = rec.data()
        # put the student in the nodes list too, if you prefer that shape:
        return {
            "student": data["student"],
            "nodes": [data["student"], *data["nodes"]],
            "relationships": data["relationships"],
        }

    

# --------- Fetching all relationships in the knowledge graph ---------
def fetch_all_relations() -> dict:
    ''' Fetch all unique relationship types in the KG to allow filtering'''
    with driver.session() as session:
        # First try
        try:
            res = session.run("""
                SHOW RELATIONSHIP TYPES
                YIELD name
                RETURN name ORDER BY name
            """)
            return [r["name"] for r in res]
        except Neo4jError:
            pass

        # Second try
        try:
            res = session.run("""
                CALL db.relationshipTypes() YIELD relationshipType
                RETURN relationshipType AS name ORDER BY name
            """)
            return [r["name"] for r in res]
        except Neo4jError:
            pass

        # Scan as last resort (slower)
        res = session.run("""
            MATCH ()-[r]->()
            RETURN DISTINCT type(r) AS name
            ORDER BY name
        """)
        return [r["name"] for r in res]
    
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


# --------- Fetching all data in the knowledge graph - Crazy checking since it is needed for LLM ---------
def _jsonify_value(v: any) -> any:
    """Best-effort conversion of Neo4j values to JSON-safe types."""
    # None / primitives
    if v is None or isinstance(v, (str, int, float, bool)):
        # guard for NaN/Infinity which are not valid in JSON
        if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
            return None
        return v

    # datetimes
    if isinstance(v, (datetime, date, time)):
        # ISO 8601 strings are safe
        try:
            return v.isoformat()
        except Exception:
            return str(v)

    # bytes-like
    if isinstance(v, (bytes, bytearray, memoryview)):
        return v.decode("utf-8", errors="replace")

    # spatial
    if Neo4jPoint is not None and isinstance(v, Neo4jPoint):  # type: ignore
        # include both Cartesian and WGS-84 friendly fields, when present
        out = {"srid": v.srid}
        if hasattr(v, "x"): out["x"] = v.x
        if hasattr(v, "y"): out["y"] = v.y
        if hasattr(v, "z"): 
            try:
                out["z"] = v.z
            except Exception:
                pass
        # WGS-84 helpers (lat/lon) if available
        if hasattr(v, "latitude"): out["latitude"] = v.latitude
        if hasattr(v, "longitude"): out["longitude"] = v.longitude
        return out

    # lists / tuples / sets
    if isinstance(v, (list, tuple, set)):
        return [_jsonify_value(x) for x in v]

    # dict-like
    if isinstance(v, dict):
        return {str(k): _jsonify_value(val) for k, val in v.items()}

    # fallback
    return str(v)

def _jsonify_props(props: dict[str, any]) -> dict[str, any]:
    return {str(k): _jsonify_value(v) for k, v in props.items()}

# --- Main mover ----
def fetch_full_kg_data(n_limit: int | None = None, r_limit: int | None = None) -> dict:
    """
    Fetch the whole graph as plain JSON-friendly dicts.

    - Uses elementId(...) everywhere (no deprecation warnings).
    - Works on an empty DB (always returns a single row).
    - Optionally caps returned nodes/relationships via n_limit/r_limit (safe for big graphs).
    """
    cypher = """
    // Collect all nodes (OPTIONAL MATCH ensures one row even if graph is empty)
    OPTIONAL MATCH (n)
    WITH collect(DISTINCT n) AS ns

    // Optionally trim node set to limit payload size
    WITH (CASE WHEN $n_limit IS NULL THEN ns ELSE ns[0..toInteger($n_limit)] END) AS ns

    // Collect rels only among those nodes
    OPTIONAL MATCH (a)-[r]->(b)
    WHERE a IN ns AND b IN ns
    WITH ns, collect(DISTINCT r) AS rs

    // Optionally trim relationships
    WITH ns, (CASE WHEN $r_limit IS NULL THEN rs ELSE rs[0..toInteger($r_limit)] END) AS rs

    RETURN
      [x IN ns | { 
        id: elementId(x), 
        labels: labels(x), 
        props: properties(x) 
      }] AS nodes,
      [x IN rs | { 
        id: elementId(x), 
        type: type(x), 
        start: elementId(startNode(x)), 
        end: elementId(endNode(x)),
        props: properties(x)
      }] AS relationships
    """

    with driver.session() as session:
        rec = session.run(
            cypher,
            n_limit=n_limit,
            r_limit=r_limit,
        ).single()

        # Safety: rec can technically be None if the query changes or fails silently
        if not rec:
            return {"nodes": [], "relationships": []}

        # JSON-safe post-processing for property maps (handles points/bytes/datetimes/etc.)
        raw_nodes: List[dict[str, any]] = rec["nodes"] or []
        raw_rels:  List[dict[str, any]] = rec["relationships"] or []

        nodes = [
            {
                "id": n.get("id"),
                "labels": list(n.get("labels") or []),
                "props": _jsonify_props(n.get("props") or {}),
            }
            for n in raw_nodes
        ]

        relationships = [
            {
                "id": r.get("id"),
                "type": r.get("type"),
                "start": r.get("start"),
                "end": r.get("end"),
                "props": _jsonify_props(r.get("props") or {}),
            }
            for r in raw_rels
        ]

        return {"nodes": nodes, "relationships": relationships}
    


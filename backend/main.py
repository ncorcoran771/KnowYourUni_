''' Declaring routes and whatnot to use with fastapi '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import query_utils as qu  # Neo4j query utils

from fdev import student_metrics #metric functions

# TODO Import all helper modules/functions here

# Initializng the connection
app = FastAPI()
app.add_middleware(  # Letting Vite talk to the API
    CORSMiddleware,
    allow_origins=["*"],  # all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],  # all methods
    allow_headers=["*"],  # all headers
)

# dev health endpoint
@app.get("/api/health")
def health():
    return {"status": "ok"}

# Validate a given student id
@app.get("/api/validate/${id}")
def validate_id(id: str) -> bool:
    v: bool = qu.validate_student_id(id)
    return {"ok": v}

# study buddy metric
@app.get("/api/validate/${id}")
def get_study_buddies(id: str) -> bool:
    v = student_metrics.study_buddy_finder(id)
    return {"ok": v}

# Return all nodes/data for a specific user
@app.get("/api/kg/${id}")
def get_id_data(id: str) -> dict:
    return qu.fetch_student_data(id)

#Return all relations in a KG
@app.get("/api/kg/relations")
def get_all_relations() -> dict:
    return qu.fetch_all_relations()

# Return all nodes/data in the KG
@app.get("/api/kg/")
def get_all_data() -> dict:
    return qu.fetch_full_kg_data()

# Return nodes in a specified relation
@app.get("/api/kg/graph")
def get_graph(id: str) -> dict:
    return qu.fetch_graph(id)

''' TODO (endpoints/connections)
- LLM requests + responses
- NLP/LLM text suggestions
'''
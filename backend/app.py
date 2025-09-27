''' Declaring routes and whatnot to use with fastapi '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import query_utils as qu  # Neo4j query utils
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
@app.post("/api/validate/${id}")
def validate_id(id: str):
    return # Query from Neo4j to validate

# Return all nodes/data for a specific user
@app.post("/api/kg/${id}")
def get_id_data(id: str):
    return # Query from Neo4j to return user

# Return all nodes/data in the KG
@app.post("/api/kg/")
def get_all_data():
    return # Query from Neo4j to return all data

''' TODO (endpoints/connections)
- LLM requests + responses
- NLP/LLM text suggestions
'''
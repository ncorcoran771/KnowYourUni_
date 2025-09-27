''' Declaring routes and whatnot to use with fastapi '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Will import all other modules here

# Initializng the connection
app = FastAPI()
app.add_middleware(  # Letting Vite talk to the API
    CORSMiddleware,
    allow_origins=["*"],  # all origins
    allow_credentials=True,
    allow_methods=["*"],  # all methods
    allow_headers=["*"],  # all headers
)

# dev health endpoint
@app.get("/api/health")
def health():
    return {"status": "ok"}

# Return all nodes/data for a specific user
@app.post("/api/get_id_data")
def get_id_data():
    return # Query from Neo4j to return user

@app.post("/api/get_all_data")
def get_all_data():
    return # Query from Neo4j to return all data

''' TODO (endpoints/connections)
- Auth (Student ID or Admin to see everything)
- LLM requests + responses
- NLP/LLM text suggestions
'''


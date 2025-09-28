''' Declaring routes and whatnot to use with fastapi '''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import query_utils as qu  # Neo4j query utils
from utils import to_plain  # helper function to convert neo4j objects to plain python
from pydantic import BaseModel

from fdev import student_metrics #metric functions

# Pydantic Classes
class ValidateOut(BaseModel):  # Validating user IDs
    ok: bool

# Initializng the connection
app = FastAPI(debug=True)
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
@app.get("/api/validate/{id}", response_model=ValidateOut)
def validate_id(id: str):
    v: bool = qu.validate_student_id(id)
    return {"ok": v}

# study buddy metric
@app.get("/api/get_study_buddies/{id}")
def get_study_buddies(id: str):
    return JSONResponse(jsonable_encoder(student_metrics.study_buddy_finder(id)))

# suggested next semester core courses and professor
@app.get("/api/suggest_next_semester_classes/{id}")
def suggest_next_semester_classes(id: str):
    raw = JSONResponse(jsonable_encoder(student_metrics.suggest_next_semester_classes(id, top_k=15))),
    payload = {
        "student_id": id,
        "suggestions": [
            {
                "course_code": s.get("course_code"),
                "professor": s.get("professor"),
                "confidence": float(s["confidence"]) if "confidence" in s else None,
            }
            for s in (raw or [])
        ],
    }
    return JSONResponse(jsonable_encoder(payload))

# Return all nodes/data for a specific user
@app.get("/api/kg/{id}")
def get_id_data(id: str) -> dict:
    data = qu.fetch_student_data(id)
    return JSONResponse(jsonable_encoder(to_plain(data)))

#Return all relations in a KG
@app.get("/api/kg/relations")
def get_all_relations() -> dict:
    return JSONResponse(qu.fetch_all_relations())

# Return all nodes/data in the KG
@app.get("/api/kg/")
def get_all_data() -> dict:
    return JSONResponse(qu.fetch_full_kg_data())

# Return nodes in a specified relation
@app.get("/api/kg/graph")
def get_graph(id: str, id2: int) -> dict:
    return qu.fetch_graph(id, id2)

''' TODO (endpoints/connections)
- LLM requests + responses
- NLP/LLM text suggestions
'''
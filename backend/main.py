''' Declaring routes and whatnot to use with fastapi '''

import json
from fastapi import FastAPI, logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import query_utils as qu  # Neo4j query utils
from utils import to_plain, normalize_suggestion  # helper function to convert neo4j objects to plain python
from pydantic import BaseModel
from typing import Optional, List, Any, Dict, Tuple, Union
from fdev import student_metrics #metric functions
import unibud as ubud

# Pydantic Classes
class ValidateOut(BaseModel):  # Validating user IDs
    ok: bool
    
class SuggestionOut(BaseModel):
    course_code: str
    professor: Optional[str] = None
    confidence: Optional[float] = None

class SuggestionsResponse(BaseModel):
    student_id: str
    suggestions: List[SuggestionOut] = []

# For the lovely unibud    
class AskReq(BaseModel):
    query: str

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

# Suggest next semester classes metric
@app.get("/api/suggest_next_semester_classes/{id}", response_model=SuggestionsResponse)
def suggest_next_semester_classes(id: str):
    raw = student_metrics.suggest_next_semester_classes(id, top_k=15)
    obj = _to_obj(raw)  # Convert to raw python object
    obj = jsonable_encoder(obj)  # normalize everything
    items = _as_list(obj)  # Extract list of suggestions
    suggestions: List[Dict[str, Optional[Union[str, float]]]] = []
    for it in items:
        norm = _normalize_item(it)
        if norm["course_code"]:
            suggestions.append(norm)

    return {
        "student_id": id,
        "suggestions": suggestions,
    }

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

# Post endpoint for unibud llm (gemini)
@app.post("/api/unibud/ask")
def unibud(req: AskReq):
    answer = ubud.ask(req.query)
    return {"text": answer}

''' Random helper functions, feel free to ignore '''

def _to_obj(raw: Any) -> Any:
    """Turn stringified JSON into Python objects; otherwise return as-is."""
    if isinstance(raw, (bytes, bytearray)):
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return raw
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except Exception:
            # Log a preview to help debug
            logger.warning("suggest_next_semester_classes() returned str that isn't JSON. Preview: %r", raw[:200])
            return raw  # will be handled downstream (becomes empty list)
    return raw

def _as_list(obj: Any) -> List[Any]:
    """Extract the list of suggestions from common container shapes."""
    if obj is None:
        return []
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for key in ("results", "suggestions", "items", "data"):
            val = obj.get(key)
            if isinstance(val, list):
                return val
        # single dict item – treat as one suggestion
        return [obj]
    # Anything else (e.g., stray string) -> empty list
    return []

def _norm_num(x: Any) -> Optional[float]:
    if x is None:
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None

def _normalize_item(item: Any) -> Optional[Dict[str, Union[str, float, None]]]:
    # dict-like
    if isinstance(item, dict):
        # field aliases
        code = (
            item.get("course_code")
            or item.get("course_id")
            or item.get("code")
            or item.get("course")
            or ""
        )
        prof = (
            item.get("professor")
            or item.get("faculty_name")
            or item.get("instructor")
            or item.get("teacher")
        )
        conf = (
            item.get("confidence")
            or item.get("final_score")
            or item.get("score")
            or item.get("initial_prof_rating")
        )
        code = str(code) if code is not None else ""
        if not code.strip():
            return None
        return {"course_code": code, "professor": prof, "confidence": _norm_num(conf)}

    # tuple/list positional: [code, professor?, confidence?]
    if isinstance(item, (list, tuple)) and item:
        code = str(item[0]) if len(item) >= 1 and item[0] is not None else ""
        prof = str(item[1]) if len(item) >= 2 and item[1] is not None else None
        conf = _norm_num(item[2]) if len(item) >= 3 else None
        if not code.strip():
            return None
        return {"course_code": code, "professor": prof, "confidence": conf}

    # plain string – use as course code if it looks like one
    if isinstance(item, str):
        code = item.strip()
        if not code:
            return None
        return {"course_code": code, "professor": None, "confidence": None}

    # fallback
    s = str(item).strip()
    if not s:
        return None
    return {"course_code": s, "professor": None, "confidence": None}

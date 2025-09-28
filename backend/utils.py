''' Random helper functions '''

from neo4j.graph import Node, Relationship
from neo4j.time import Date, DateTime, Time, Duration
from typing import Optional, List, Any, Dict, Tuple, Union
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

# Convert any weird neo4j objects to plain python data structures
def to_plain(obj):
    ''' Convert Neo4j objects to plain Python data structures '''
    if isinstance(obj, Node):
        return {
            "id": obj.element_id,
            "labels": list(obj.labels),
            "properties": {k: to_plain(v) for k, v in dict(obj).items()},
        }
    if isinstance(obj, Relationship):
        return {
            "id": obj.element_id,
            "type": obj.type,
            "start": obj.start_node.element_id,
            "end": obj.end_node.element_id,
            "properties": {k: to_plain(v) for k, v in dict(obj).items()},
        }
    if isinstance(obj, (list, tuple)):
        return [to_plain(v) for v in obj]
    if isinstance(obj, dict):
        return {k: to_plain(v) for k, v in obj.items()}
    if isinstance(obj, (Date, DateTime, Time)):
        return obj.to_native().isoformat()  # 'YYYY-MM-DD' / ISO 8601
    if isinstance(obj, Duration):
        return str(obj)
    return obj

def normalize_suggestion(item: Any) -> Dict[str, Optional[Union[str, float]]]:
    """
    Accepts a variety of shapes and returns a uniform dict:
    { course_code: str, professor: Optional[str], confidence: Optional[float] }
    Supported inputs:
      - {"course_code": "...", "professor": "...", "confidence": 0.9}
      - ("CS101", "Dr. Ada", 0.92)  or ["CS101", "Dr. Ada", 0.92]
      - "CS101"
      - Any other object -> str(object) as course_code
    """
    # dict-like (ideal)
    if isinstance(item, dict):
        conf = item.get("confidence")
        return {
            "course_code": str(item.get("course_code") or item.get("code") or item.get("course") or ""),
            "professor": item.get("professor") or item.get("instructor"),
            "confidence": float(conf) if conf is not None else None,
        }

    # tuple/list positional
    if isinstance(item, (tuple, list)):
        # heuristics: [code, professor?, confidence?]
        code = str(item[0]) if len(item) >= 1 else ""
        prof = str(item[1]) if len(item) >= 2 and item[1] is not None else None
        conf_raw = item[2] if len(item) >= 3 else None
        try:
            conf = float(conf_raw) if conf_raw is not None else None
        except (TypeError, ValueError):
            conf = None
        return {"course_code": code, "professor": prof, "confidence": conf}

    # plain string -> course code only
    if isinstance(item, str):
        return {"course_code": item, "professor": None, "confidence": None}

    # fallback
    return {"course_code": str(item), "professor": None, "confidence": None}

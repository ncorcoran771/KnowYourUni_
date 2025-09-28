''' Random helper functions '''

from neo4j.graph import Node, Relationship
from neo4j.time import Date, DateTime, Time, Duration

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
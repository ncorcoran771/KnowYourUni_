
MATCH (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"}), (d:Degree {id: "BS-ComputerScience-1"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BS-ComputerScience-1"}), (d:Degree {id: "BS-ComputerScience-1"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"}), (d:Degree {id: "BS-ComputerScience-1"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"}), (d:Degree {id: "BA-ComputerScience-2"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-ComputerScience-2"}), (d:Degree {id: "BA-ComputerScience-2"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-ELECTIVE-2-BA-ComputerScience-2"}), (d:Degree {id: "BA-ComputerScience-2"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"}), (d:Degree {id: "BS-Biology-1"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-ELECTIVE-1-BS-Biology-1"}), (d:Degree {id: "BS-Biology-1"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"}), (d:Degree {id: "BS-Biology-1"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"}), (d:Degree {id: "BA-Biology-2"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-Biology-2"}), (d:Degree {id: "BA-Biology-2"})
CREATE (r)-[:PART_OF]->(d);

MATCH (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"}), (d:Degree {id: "BA-Biology-2"})
CREATE (r)-[:PART_OF]->(d);

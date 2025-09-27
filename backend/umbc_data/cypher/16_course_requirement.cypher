
MATCH (c:Course {id: "CSJJ 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSXX 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSMM 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSZZ 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSHH 200"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSBB 200"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSNN 300"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSRR 300-6-7"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSVV 300"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSOO 300-9"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSFF 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSKK 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSUU 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSSS 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BEEE 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSII 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSRR 300"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSPP 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BLLL 100"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSAA 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSSS 300"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSZZ 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSKK 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSOO 100"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSRR 400"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BS-ComputerScience-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSXX 100"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSKK 200-4"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSII 200"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSYY 200"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSDD 200"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSYY 200-1"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSSS 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSNN 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSAA 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSRR 300-2"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSKK 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSMM 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSKK 400"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSQQ 400"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSUU 400"}), (r:RequirementGroup {id: "REQ-CORE-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSOO 300"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSVV 300"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSUU 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSGG 300"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSVV 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BCCC 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSBB 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BXXX 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSXX 200"}), (r:RequirementGroup {id: "REQ-ELECTIVE-2-BA-ComputerScience-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BFFF 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BMMM 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BHHH 100"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BBBB 100-3"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BUUU 200"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BOOO 200"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BXXX 200"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BNNN 200-7"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BWWW 200-2"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BJJJ 300"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BFFF 300"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BTTT 300"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BQQQ 300-9"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BKKK 300"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BGGG 300-1"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BFFF 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BZZZ 400-3"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BDDD 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BNNN 400"}), (r:RequirementGroup {id: "REQ-CORE-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BUUU 300"}), (r:RequirementGroup {id: "REQ-ELECTIVE-1-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BLLL 100"}), (r:RequirementGroup {id: "REQ-ELECTIVE-1-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSRR 300-6-7"}), (r:RequirementGroup {id: "REQ-ELECTIVE-1-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BUUU 300-4"}), (r:RequirementGroup {id: "REQ-ELECTIVE-1-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSSS 100"}), (r:RequirementGroup {id: "REQ-ELECTIVE-1-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BEEE 300"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSDD 200"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BNNN 200"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BLLL 100"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BIII 300"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BEEE 200"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSXX 200"}), (r:RequirementGroup {id: "REQ-CONCENTRATION-2-BS-Biology-1"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BMMM 100"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BEEE 100"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BFFF 100-4"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BUUU 200"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BQQQ 200"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BQQQ 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BRRR 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BGGG 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BRRR 300-8"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BKKK 300"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BPPP 400"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BZZZ 400"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BNNN 400"}), (r:RequirementGroup {id: "REQ-CORE-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSKK 300"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BWWW 200-2"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BXXX 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BOOO 200-2"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BUUU 300"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-1-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSZZ 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BZZZ 400-3"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BQQQ 300-9"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BGGG 300-2"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "BWWW 200-2"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

MATCH (c:Course {id: "CSYY 200"}), (r:RequirementGroup {id: "REQ-SPECIALIZATION-2-BA-Biology-2"})
CREATE (c)-[:FULFILLS]->(r);

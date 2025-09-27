
MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSPP 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSXX 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSUU 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSAA 300-2"}), (target:Course {id: "CSSS 100"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BFFF 400"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BZZZ 400"}), (target:Course {id: "BMMM 100"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BRRR 300-8"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "CSSS 300"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSRR 300-6"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSSS 100"}), (target:Course {id: "CSHH 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSGG 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSZZ 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSSS 100"}), (target:Course {id: "CSBB 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSAA 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSAA 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSRR 300-6-7"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSVV 100"}), (target:Course {id: "CSPP 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSAA 300-4"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSCC 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSMM 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "CSKK 300"}), (target:Course {id: "CSUU 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSRR 300-2"}), (target:Course {id: "CSUU 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSVV 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "CSKK 300"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSUU 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSRR 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSOO 300-9"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSGG 300-8"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSAA 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "CSJJ 100-4"}), (target:Course {id: "CSVV 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BOOO 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BFFF 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BFFF 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BIII 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BIII 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BBBB 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BBBB 100-3"}), (target:Course {id: "BQQQ 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BGGG 300-1"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BQQQ 300-9"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BQQQ 300-9"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BNNN 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BYYY 200"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BEEE 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BRRR 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BFFF 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BIII 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BWWW 200-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BBBB 200-9"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BJJJ 300"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D"}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "D-"}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C"}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Recommended"}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BGGG 300-1"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BNNN 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BNNN 400"})
CREATE (source)-[:PREREQUISITE_FOR {strength: "Required", minGrade: "C-"}]->(target);

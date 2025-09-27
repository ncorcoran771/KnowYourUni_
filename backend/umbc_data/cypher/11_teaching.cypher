
MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSSS 300"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSNN 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01011"}), (c:Course {id: "CSNN 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSNN 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSXX 400"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSXX 400"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSXX 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSKK 200"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSKK 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSKK 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSHH 200"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSGG 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSGG 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01010"}), (c:Course {id: "CSFF 400"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSFF 400"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSGG 300-2"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSZZ 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01010"}), (c:Course {id: "CSKK 200-4"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSKK 200-4"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01023"}), (c:Course {id: "CSRR 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSXX 200"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSJJ 100"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSJJ 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSBB 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01011"}), (c:Course {id: "CSBB 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSRR 300-6"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01011"}), (c:Course {id: "CSSS 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSSS 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSAA 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSAA 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSAA 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSAA 300-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSJJ 100-4"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01023"}), (c:Course {id: "CSJJ 100-4"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01017"}), (c:Course {id: "CSVV 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01030"}), (c:Course {id: "CSVV 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01010"}), (c:Course {id: "CSVV 100"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01023"}), (c:Course {id: "CSRR 300-6-7"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSRR 300-6-7"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01011"}), (c:Course {id: "CSRR 300-2"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSRR 300-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01030"}), (c:Course {id: "CSRR 300-2"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSII 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSPP 200"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSPP 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01023"}), (c:Course {id: "CSNN 100"})
CREATE (f)-[:TEACHES {terms: ["Summer"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSNN 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSAA 300-4"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSKK 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01010"}), (c:Course {id: "CSKK 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSOO 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSOO 100"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSOO 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSXX 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSQQ 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSQQ 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSQQ 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01023"}), (c:Course {id: "CSMM 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSMM 100"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSMM 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01011"}), (c:Course {id: "CSCC 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSCC 300"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01018"}), (c:Course {id: "CSVV 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSVV 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSYY 200"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01030"}), (c:Course {id: "CSYY 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSKK 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01011"}), (c:Course {id: "CSKK 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSOO 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01017"}), (c:Course {id: "CSOO 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSUU 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSGG 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSSS 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSDD 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSDD 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSDD 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSMM 300"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSMM 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01021"}), (c:Course {id: "CSMM 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSUU 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSUU 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSRR 400"})
CREATE (f)-[:TEACHES {terms: ["Summer"]}]->(c);

MATCH (f:Faculty {id: "F01009"}), (c:Course {id: "CSRR 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSRR 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01010"}), (c:Course {id: "CSEE 200"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01024"}), (c:Course {id: "CSEE 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01003"}), (c:Course {id: "CSEE 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01023"}), (c:Course {id: "CSGG 300-8"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01010"}), (c:Course {id: "CSAA 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01016"}), (c:Course {id: "CSAA 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01002"}), (c:Course {id: "CSAA 200"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSYY 200-1"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01015"}), (c:Course {id: "CSYY 200-1"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01027"}), (c:Course {id: "CSYY 200-1"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01018"}), (c:Course {id: "CSZZ 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01022"}), (c:Course {id: "CSVV 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BFFF 100"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BQQQ 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BQQQ 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BQQQ 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BFFF 400"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BFFF 400"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BUUU 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01005"}), (c:Course {id: "BUUU 200"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BBBB 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BBBB 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01005"}), (c:Course {id: "BJJJ 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BJJJ 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BIII 200"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01029"}), (c:Course {id: "BCCC 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BOOO 200"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BUUU 300"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BRRR 300"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BFFF 300"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01028"}), (c:Course {id: "BFFF 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BFFF 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BXXX 200"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BXXX 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BIII 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01007"}), (c:Course {id: "BIII 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BMMM 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BTTT 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01007"}), (c:Course {id: "BTTT 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BTTT 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01012"}), (c:Course {id: "BBBB 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01005"}), (c:Course {id: "BBBB 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BQQQ 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01029"}), (c:Course {id: "BQQQ 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BQQQ 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BPPP 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01012"}), (c:Course {id: "BPPP 400"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BPPP 400"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BGGG 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BGGG 300"})
CREATE (f)-[:TEACHES {terms: ["Summer"]}]->(c);

MATCH (f:Faculty {id: "F01001"}), (c:Course {id: "BGGG 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BQQQ 300-9"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01029"}), (c:Course {id: "BQQQ 300-9"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BQQQ 300-9"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01012"}), (c:Course {id: "BNNN 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BOOO 200-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BOOO 200-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01029"}), (c:Course {id: "BOOO 200-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01020"}), (c:Course {id: "BEEE 300"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BEEE 300"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BWWW 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BEEE 200"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BEEE 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BYYY 200"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BYYY 200"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01020"}), (c:Course {id: "BYYY 200"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01029"}), (c:Course {id: "BZZZ 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BZZZ 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BZZZ 400"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BNNN 200-7"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BNNN 200-7"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BMMM 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BMMM 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BHHH 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BHHH 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BRRR 300-8"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01012"}), (c:Course {id: "BRRR 300-8"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BLLL 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01007"}), (c:Course {id: "BLLL 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BLLL 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BBBB 100-3"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BBBB 100-3"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01028"}), (c:Course {id: "BBBB 100-3"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BUUU 300-4"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BUUU 300-4"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01005"}), (c:Course {id: "BUUU 300-4"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BEEE 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01004"}), (c:Course {id: "BFFF 300-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BZZZ 400-3"})
CREATE (f)-[:TEACHES {terms: ["Fall"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BZZZ 400-3"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01001"}), (c:Course {id: "BZZZ 400-3"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BWWW 200-2"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01001"}), (c:Course {id: "BWWW 200-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01019"}), (c:Course {id: "BWWW 200-2"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01005"}), (c:Course {id: "BBBB 200-9"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01007"}), (c:Course {id: "BBBB 200-9"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01020"}), (c:Course {id: "BBBB 200-9"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BUUU 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01020"}), (c:Course {id: "BUUU 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BUUU 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BSSS 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BSSS 100"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01007"}), (c:Course {id: "BSSS 100"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BDDD 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01020"}), (c:Course {id: "BDDD 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01013"}), (c:Course {id: "BDDD 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01020"}), (c:Course {id: "BKKK 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01025"}), (c:Course {id: "BKKK 300"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BFFF 100-4"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01028"}), (c:Course {id: "BSSS 300"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01001"}), (c:Course {id: "BGGG 300-2"})
CREATE (f)-[:TEACHES {terms: ["Spring"]}]->(c);

MATCH (f:Faculty {id: "F01014"}), (c:Course {id: "BFFF 100-4-1"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01008"}), (c:Course {id: "BFFF 100-4-1"})
CREATE (f)-[:TEACHES {terms: ["Spring", "Summer"]}]->(c);

MATCH (f:Faculty {id: "F01001"}), (c:Course {id: "BGGG 300-1"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01026"}), (c:Course {id: "BNNN 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

MATCH (f:Faculty {id: "F01006"}), (c:Course {id: "BNNN 400"})
CREATE (f)-[:TEACHES {terms: ["Fall", "Spring"]}]->(c);

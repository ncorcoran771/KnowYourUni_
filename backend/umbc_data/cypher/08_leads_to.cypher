
MATCH (source:Course {id: "CSSS 300"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSSS 300"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSSS 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.42, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "CSSS 300"}), (target:Course {id: "CSRR 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.79, successCorrelation: 0.73}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSAA 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.98, successCorrelation: 0.79}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.36, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.24, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "CSKK 200"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.42, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.42, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSHH 200"}), (target:Course {id: "CSGG 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSGG 300"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "CSGG 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSGG 300-2"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSGG 300-2"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.48, successCorrelation: 0.7}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSAA 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSZZ 200"}), (target:Course {id: "CSOO 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "CSKK 200-4"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSKK 200-4"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.59}]->(target);

MATCH (source:Course {id: "CSKK 200-4"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSKK 200-4"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSKK 200-4"}), (target:Course {id: "CSOO 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "CSRR 300"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.36, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "CSRR 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.8, successCorrelation: 0.71}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.9, successCorrelation: 0.79}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.36, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSAA 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.36, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSXX 200"}), (target:Course {id: "CSGG 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSPP 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.92, successCorrelation: 0.73}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.89, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.77, successCorrelation: 0.78}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSKK 200-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.5, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSXX 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.2, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.34, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSDD 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSEE 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSAA 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.21, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "CSJJ 100"}), (target:Course {id: "CSVV 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.32, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.99, successCorrelation: 0.77}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.95, successCorrelation: 0.71}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.83, successCorrelation: 0.75}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.74, successCorrelation: 0.72}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSAA 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSBB 200"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSRR 300-6"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.89, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSRR 300-6"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.2, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "CSRR 300-6"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSSS 100"}), (target:Course {id: "CSHH 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.96, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "CSSS 100"}), (target:Course {id: "CSBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.87, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSSS 100"}), (target:Course {id: "CSII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.24, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "CSSS 100"}), (target:Course {id: "CSVV 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSAA 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSAA 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSAA 300-2"}), (target:Course {id: "CSSS 100"})
CREATE (source)-[:LEADS_TO {commonality: 0.99, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "CSAA 300-2"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSAA 300-2"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "CSAA 300-2"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "CSJJ 100-4"}), (target:Course {id: "CSVV 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.91, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSJJ 100-4"}), (target:Course {id: "CSII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSJJ 100-4"}), (target:Course {id: "CSUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "CSJJ 100-4"}), (target:Course {id: "CSAA 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSVV 100"}), (target:Course {id: "CSHH 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "CSVV 100"}), (target:Course {id: "CSKK 200-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSVV 100"}), (target:Course {id: "CSII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "CSVV 100"}), (target:Course {id: "CSYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSVV 100"}), (target:Course {id: "CSDD 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.94, successCorrelation: 0.83}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSRR 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.83, successCorrelation: 0.78}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSRR 300-6-7"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSRR 300-2"}), (target:Course {id: "CSUU 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.91, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSRR 300-2"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "CSRR 300-2"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSRR 300-2"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.96, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.92, successCorrelation: 0.82}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.4}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSRR 300-6-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.59}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSAA 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.4}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "CSII 200"}), (target:Course {id: "CSOO 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.73, successCorrelation: 0.72}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.42, successCorrelation: 0.7}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSPP 200"}), (target:Course {id: "CSOO 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.48, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.97, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSRR 300-6-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.78, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.75, successCorrelation: 0.79}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSKK 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSHH 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "CSNN 100"}), (target:Course {id: "CSDD 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.82, successCorrelation: 0.72}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSZZ 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.98, successCorrelation: 0.74}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSAA 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.7, successCorrelation: 0.77}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.74, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.71}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSAA 200"})
CREATE (source)-[:LEADS_TO {commonality: 1.0, successCorrelation: 0.81}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSKK 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSHH 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.7}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSDD 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSYY 200-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSOO 100"}), (target:Course {id: "CSVV 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.86, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSGG 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.96, successCorrelation: 0.72}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSKK 200-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.21, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSXX 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "CSXX 100"}), (target:Course {id: "CSYY 200-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.59}]->(target);

MATCH (source:Course {id: "CSMM 100"}), (target:Course {id: "CSKK 200-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "CSMM 100"}), (target:Course {id: "CSYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.5, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "CSMM 100"}), (target:Course {id: "CSUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "CSMM 100"}), (target:Course {id: "CSEE 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSMM 100"}), (target:Course {id: "CSAA 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.6, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSMM 100"}), (target:Course {id: "CSYY 200-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSCC 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.78, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "CSCC 300"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSCC 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSCC 300"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "CSVV 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.82, successCorrelation: 0.82}]->(target);

MATCH (source:Course {id: "CSVV 300"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "CSVV 300"}), (target:Course {id: "CSRR 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.48, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "CSYY 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.31, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "CSYY 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "CSYY 200"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSYY 200"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSYY 200"}), (target:Course {id: "CSMM 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSKK 300"}), (target:Course {id: "CSUU 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.72, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "CSKK 300"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.87, successCorrelation: 0.72}]->(target);

MATCH (source:Course {id: "CSKK 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.48, successCorrelation: 0.4}]->(target);

MATCH (source:Course {id: "CSKK 300"}), (target:Course {id: "CSRR 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.5, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSOO 300"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "CSOO 300"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSOO 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.32, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "CSOO 300"}), (target:Course {id: "CSSS 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.93, successCorrelation: 0.86}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.96, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSAA 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSRR 300-6-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "CSDD 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.21, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "CSMM 300"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.9, successCorrelation: 0.71}]->(target);

MATCH (source:Course {id: "CSMM 300"}), (target:Course {id: "CSXX 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSMM 300"}), (target:Course {id: "CSUU 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "CSMM 300"}), (target:Course {id: "CSGG 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.77, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.5, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSCC 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.56, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "CSUU 200"}), (target:Course {id: "CSOO 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.42, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "CSOO 300-9"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.59}]->(target);

MATCH (source:Course {id: "CSOO 300-9"}), (target:Course {id: "CSKK 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "CSOO 300-9"}), (target:Course {id: "CSUU 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.93, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.81, successCorrelation: 0.77}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSAA 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.85, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSNN 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSEE 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.34, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "CSGG 300-8"}), (target:Course {id: "CSQQ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.93, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSRR 300-6-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.32, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSAA 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.89, successCorrelation: 0.78}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.89, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSAA 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "CSYY 200-1"}), (target:Course {id: "CSVV 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.7}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.85, successCorrelation: 0.76}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.48, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSPP 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.24, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSDD 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "CSZZ 100"}), (target:Course {id: "CSVV 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "CSVV 200"}), (target:Course {id: "CSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "CSVV 200"}), (target:Course {id: "CSGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "CSVV 200"}), (target:Course {id: "CSRR 300-6"})
CREATE (source)-[:LEADS_TO {commonality: 0.41, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "CSVV 200"}), (target:Course {id: "CSRR 300-6-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "CSVV 200"}), (target:Course {id: "CSRR 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.31, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "CSVV 200"}), (target:Course {id: "CSOO 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.77, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BBBB 200-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.98, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.79, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BOOO 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BMMM 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BQQQ 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BWWW 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BFFF 100"}), (target:Course {id: "BYYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BQQQ 300"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.6, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "BQQQ 300"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "BQQQ 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.31, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BFFF 400"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.73, successCorrelation: 0.81}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BFFF 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.87, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "BUUU 200"}), (target:Course {id: "BGGG 300-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BYYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.87, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.93, successCorrelation: 0.77}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BOOO 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BQQQ 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "BBBB 100"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BJJJ 300"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.78, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "BJJJ 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.82, successCorrelation: 0.85}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.86, successCorrelation: 0.75}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.31, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BFFF 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "BIII 200"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.7, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BQQQ 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.89, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.42, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "BCCC 200"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.34, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BQQQ 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BFFF 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.4}]->(target);

MATCH (source:Course {id: "BOOO 200"}), (target:Course {id: "BGGG 300-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "BUUU 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "BUUU 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.2, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BRRR 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.74, successCorrelation: 0.7}]->(target);

MATCH (source:Course {id: "BRRR 300"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "BRRR 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BRRR 300"}), (target:Course {id: "BNNN 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BFFF 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BFFF 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.34, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.73, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.86, successCorrelation: 0.81}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "BXXX 200"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BIII 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BIII 300"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BIII 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "BIII 300"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.6, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.95, successCorrelation: 0.9}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.79, successCorrelation: 0.83}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BNNN 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.81, successCorrelation: 0.75}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.31, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BIII 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BQQQ 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.2, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BMMM 200"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BTTT 300"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BTTT 300"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.52}]->(target);

MATCH (source:Course {id: "BBBB 200"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "BBBB 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "BBBB 200"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BBBB 200"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BBBB 200"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.73, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BFFF 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.34, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BQQQ 200"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BGGG 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BFFF 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BQQQ 300-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.29, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "BNNN 200"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BFFF 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.92, successCorrelation: 0.88}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.41, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "BOOO 200-2"}), (target:Course {id: "BGGG 300-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "BEEE 300"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.79}]->(target);

MATCH (source:Course {id: "BEEE 300"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "BEEE 300"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.76, successCorrelation: 0.89}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BIII 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.32, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.59}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BWWW 200"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "BEEE 200"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BEEE 200"}), (target:Course {id: "BJJJ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.43, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BEEE 200"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BEEE 200"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.41, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BYYY 200"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BYYY 200"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.47, successCorrelation: 0.64}]->(target);

MATCH (source:Course {id: "BZZZ 400"}), (target:Course {id: "BMMM 100"})
CREATE (source)-[:LEADS_TO {commonality: 0.71, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.81, successCorrelation: 0.84}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.69}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.6, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BNNN 200-7"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.85, successCorrelation: 0.86}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.99, successCorrelation: 0.73}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BNNN 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.77, successCorrelation: 0.84}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.57, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BXXX 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BOOO 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BEEE 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BYYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.51, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BMMM 100"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.61}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BRRR 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.75, successCorrelation: 0.84}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.94, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BOOO 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BWWW 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.5, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BYYY 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BWWW 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BHHH 100"}), (target:Course {id: "BBBB 200-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.36, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "BRRR 300-8"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "BRRR 300-8"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BOOO 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.85, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BBBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.96, successCorrelation: 0.86}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BNNN 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.95, successCorrelation: 0.75}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.21, successCorrelation: 0.7}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.21, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BWWW 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BLLL 100"}), (target:Course {id: "BBBB 200-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.27, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BBBB 100-3"}), (target:Course {id: "BQQQ 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.79, successCorrelation: 0.77}]->(target);

MATCH (source:Course {id: "BBBB 100-3"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BBBB 100-3"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "BBBB 100-3"}), (target:Course {id: "BXXX 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.6, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "BBBB 100-3"}), (target:Course {id: "BBBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BUUU 300-4"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "BUUU 300-4"}), (target:Course {id: "BNNN 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.4, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BEEE 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.82, successCorrelation: 0.83}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BNNN 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.49, successCorrelation: 0.66}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BOOO 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BEEE 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BEEE 100"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.68}]->(target);

MATCH (source:Course {id: "BFFF 300-2"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.59}]->(target);

MATCH (source:Course {id: "BFFF 300-2"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.33, successCorrelation: 0.51}]->(target);

MATCH (source:Course {id: "BFFF 300-2"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.34, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BFFF 300-2"}), (target:Course {id: "BDDD 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BIII 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.85, successCorrelation: 0.67}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BGGG 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.78, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.88, successCorrelation: 0.88}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.45, successCorrelation: 0.56}]->(target);

MATCH (source:Course {id: "BWWW 200-2"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BQQQ 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.92, successCorrelation: 0.87}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BRRR 300-8"})
CREATE (source)-[:LEADS_TO {commonality: 0.79, successCorrelation: 0.75}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BGGG 300-1"})
CREATE (source)-[:LEADS_TO {commonality: 0.75, successCorrelation: 0.79}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.24, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BIII 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BUUU 300-4"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BKKK 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.22, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "BBBB 200-9"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.54, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.83, successCorrelation: 0.79}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BMMM 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BBBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.47, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BNNN 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BOOO 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BEEE 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.28, successCorrelation: 0.53}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BWWW 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BUUU 100"}), (target:Course {id: "BBBB 200-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.53, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BUUU 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.99, successCorrelation: 0.76}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BGGG 300-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.98, successCorrelation: 0.85}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BXXX 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.47}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BBBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.48}]->(target);

MATCH (source:Course {id: "BSSS 100"}), (target:Course {id: "BNNN 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.59, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BKKK 300"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.36, successCorrelation: 0.43}]->(target);

MATCH (source:Course {id: "BKKK 300"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.44, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BCCC 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.97, successCorrelation: 0.84}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BTTT 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.72, successCorrelation: 0.9}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BSSS 300"})
CREATE (source)-[:LEADS_TO {commonality: 0.89, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.5}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BOOO 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.42}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BOOO 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.6}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BEEE 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.37, successCorrelation: 0.49}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BNNN 200-7"})
CREATE (source)-[:LEADS_TO {commonality: 0.25, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BWWW 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.46, successCorrelation: 0.57}]->(target);

MATCH (source:Course {id: "BFFF 100-4"}), (target:Course {id: "BBBB 200-9"})
CREATE (source)-[:LEADS_TO {commonality: 0.58, successCorrelation: 0.54}]->(target);

MATCH (source:Course {id: "BSSS 300"}), (target:Course {id: "BFFF 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.41}]->(target);

MATCH (source:Course {id: "BGGG 300-2"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.39, successCorrelation: 0.58}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BWWW 200-2"})
CREATE (source)-[:LEADS_TO {commonality: 0.77, successCorrelation: 0.86}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BUUU 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.3, successCorrelation: 0.65}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BIII 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.63}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BXXX 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.55, successCorrelation: 0.46}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BBBB 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.26, successCorrelation: 0.44}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BQQQ 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.35, successCorrelation: 0.45}]->(target);

MATCH (source:Course {id: "BFFF 100-4-1"}), (target:Course {id: "BWWW 200"})
CREATE (source)-[:LEADS_TO {commonality: 0.38, successCorrelation: 0.55}]->(target);

MATCH (source:Course {id: "BGGG 300-1"}), (target:Course {id: "BPPP 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.85, successCorrelation: 0.8}]->(target);

MATCH (source:Course {id: "BGGG 300-1"}), (target:Course {id: "BZZZ 400"})
CREATE (source)-[:LEADS_TO {commonality: 0.52, successCorrelation: 0.62}]->(target);

MATCH (source:Course {id: "BGGG 300-1"}), (target:Course {id: "BZZZ 400-3"})
CREATE (source)-[:LEADS_TO {commonality: 0.23, successCorrelation: 0.61}]->(target);

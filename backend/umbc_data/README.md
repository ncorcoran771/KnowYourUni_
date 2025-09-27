# UMBC Neo4j Academic Graph Database

This dataset contains synthetic academic data for UMBC, generated to model student degree pathways in Neo4j.

## Contents

This directory contains:

1. Cypher scripts (`*.cypher`) for creating the database incrementally
2. CSV files for bulk import
3. `import_to_neo4j.sh` script for bulk import
4. This README file

## Data Model

The database follows this graph model:

- **Nodes**: Student, Course, Faculty, Degree, RequirementGroup, Term
- **Relationships**:
  - Student-Course: COMPLETED, ENROLLED_IN
  - Student-Degree: PURSUING
  - Student-Student: SIMILAR_LEARNING_STYLE, SIMILAR_PERFORMANCE
  - Course-Course: PREREQUISITE_FOR, LEADS_TO, SIMILAR_CONTENT, SIMILAR_DIFFICULTY
  - Faculty-Course: TEACHES
  - RequirementGroup-Degree: PART_OF
  - Course-RequirementGroup: FULFILLS
  - Course-Term: OFFERED_IN

## Import Options

### Option 1: Cypher Scripts (Incremental)

Execute the Cypher scripts in numerical order using the Neo4j Browser or Cypher-shell:

```
cat 00_indexes.cypher 01_students.cypher 02_faculty.cypher [...] | bin/cypher-shell -u neo4j -p [password]
```

### Option 2: Bulk Import (Faster)

1. Stop your Neo4j server
2. Edit the `import_to_neo4j.sh` script to set the correct NEO4J_HOME path
3. Run the script: `./import_to_neo4j.sh`
4. Update your neo4j.conf to use the imported database

## Sample Queries

See the accompanying documentation for sample queries that demonstrate using
this data for personalized degree pathway planning.

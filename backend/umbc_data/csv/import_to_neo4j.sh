#!/bin/bash
# This script imports the generated CSV files into Neo4j.
# This script is idempotent - it will destroy and recreate the target database.
# Make sure Neo4j is stopped before running this script.

# Exit on error
set -e

# Path to the Neo4j installation (with proper escaping)
NEO4J_HOME="${HOME}/Library/Application Support/Neo4j Desktop/Application/relate-data/dbmss/dbms-b3818c40-56e6-4a47-a4e8-e8183cecc545"

# Database name
DB_NAME="umbc-degree-pathways"

# Path to the import directory (absolute path)
IMPORT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Check if Neo4j is running
if pgrep -x "neo4j" > /dev/null; then
    echo "Error: Neo4j appears to be running. Please stop Neo4j before running this import script."
    exit 1
fi

# Check if import directory exists and contains required files
if [ ! -d "$IMPORT_DIR" ]; then
    echo "Error: Import directory not found: $IMPORT_DIR"
    exit 1
fi

# Check for required CSV files
required_files=(
    "students.csv" "faculty.csv" "courses.csv" "degrees.csv" "terms.csv"
    "requirement_groups.csv" "textbooks.csv" "prerequisites.csv" "leads_to.csv"
    "course_similarity_content.csv" "course_similarity_difficulty.csv"
    "student_degree.csv" "teaching.csv" "completed_courses.csv"
    "enrolled_courses.csv" "learning_style_similarity.csv"
    "performance_similarity.csv" "requirement_degree.csv"
    "course_requirement.csv" "course_term.csv" "course_textbooks.csv"
    "page_views.csv" "textbook_interactions.csv"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$IMPORT_DIR/$file" ]; then
        echo "Error: Required file not found: $file"
        exit 1
    fi
done

echo "Starting import process..."
echo "Using Neo4j installation at: $NEO4J_HOME"
echo "Importing from directory: $IMPORT_DIR"
echo "Target database name: $DB_NAME"

# Clean up any existing database files
DB_PATH="$NEO4J_HOME/data/databases/$DB_NAME"
if [ -d "$DB_PATH" ]; then
    echo "Cleaning up existing database directory..."
    rm -rf "$DB_PATH"
fi

echo "Creating fresh database..."

# Run the import command with proper quoting
"$NEO4J_HOME/bin/neo4j-admin" database import full \
  --nodes="Student=$IMPORT_DIR/students.csv" \
  --nodes="Faculty=$IMPORT_DIR/faculty.csv" \
  --nodes="Course=$IMPORT_DIR/courses.csv" \
  --nodes="Degree=$IMPORT_DIR/degrees.csv" \
  --nodes="Term=$IMPORT_DIR/terms.csv" \
  --nodes="RequirementGroup=$IMPORT_DIR/requirement_groups.csv" \
  --nodes="Textbook=$IMPORT_DIR/textbooks.csv" \
  --relationships="PREREQUISITE_FOR=$IMPORT_DIR/prerequisites.csv" \
  --relationships="LEADS_TO=$IMPORT_DIR/leads_to.csv" \
  --relationships="SIMILAR_CONTENT=$IMPORT_DIR/course_similarity_content.csv" \
  --relationships="SIMILAR_DIFFICULTY=$IMPORT_DIR/course_similarity_difficulty.csv" \
  --relationships="PURSUING=$IMPORT_DIR/student_degree.csv" \
  --relationships="TEACHES=$IMPORT_DIR/teaching.csv" \
  --relationships="COMPLETED=$IMPORT_DIR/completed_courses.csv" \
  --relationships="ENROLLED_IN=$IMPORT_DIR/enrolled_courses.csv" \
  --relationships="SIMILAR_LEARNING_STYLE=$IMPORT_DIR/learning_style_similarity.csv" \
  --relationships="SIMILAR_PERFORMANCE=$IMPORT_DIR/performance_similarity.csv" \
  --relationships="PART_OF=$IMPORT_DIR/requirement_degree.csv" \
  --relationships="FULFILLS=$IMPORT_DIR/course_requirement.csv" \
  --relationships="OFFERED_IN=$IMPORT_DIR/course_term.csv" \
  --relationships="REQUIRES,RECOMMENDS=$IMPORT_DIR/course_textbooks.csv" \
  --relationships="VIEWED_PAGE=$IMPORT_DIR/page_views.csv" \
  --relationships="INTERACTED_WITH=$IMPORT_DIR/textbook_interactions.csv" \
  --delimiter="," \
  --array-delimiter=";" \
  --ignore-empty-strings=true \
  --ignore-extra-columns=true \
  --skip-bad-relationships=true \
  --skip-duplicate-nodes=true \
  --high-parallel-io=on \
  --normalize-types=true \
  --overwrite-destination=true \
  "$DB_NAME"

if [ $? -eq 0 ]; then
    echo "Import completed successfully!"
    echo "To use the database, edit neo4j.conf to set dbms.default_database=$DB_NAME"
    echo "Then restart Neo4j."
else
    echo "Import failed. Check the error messages above for details."
    exit 1
fi

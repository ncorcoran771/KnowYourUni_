
#!/usr/bin/env python3
"""
UMBC Neo4j Graph Database Generator

This script generates synthetic data for UMBC's Neo4j graph database
focused on student degree pathways. It creates realistic nodes and
relationships that model students, courses, degree programs, and more.

The script produces Cypher files that can be directly imported into Neo4j.
"""

import random
import string
import uuid
import csv
import os
import datetime
import math
import json
from collections import defaultdict
from faker import Faker

# Initialize Faker with a specific locale for more realistic data
fake = Faker(['en_US'])

# =============================================================================
#                           CONFIGURATION SETTINGS
# =============================================================================

# Output directory
OUTPUT_DIR = "umbc_data"

# Data Size Configuration
NUM_STUDENTS = 500        # Reduced number of students for more focused data
NUM_COURSES = 100         # Reduced number of courses for two departments
NUM_FACULTY = 30          # Reduced number of faculty for two departments
NUM_DEGREES = 4           # Two degrees per department (BS and BA)
TERMS_TO_GENERATE = 12    # Number of academic terms to generate
HISTORY_YEARS = 4         # Years of historical data

# System Complexity
AVG_COURSES_PER_STUDENT = 20    # Average number of courses each student has taken
MAX_PREREQS_PER_COURSE = 3      # Maximum number of prerequisites per course
AVG_COURSES_PER_DEGREE = 40     # Average courses needed for a degree
AVG_REQUIREMENTS_PER_DEGREE = 5  # Average requirement groups per degree

# Variation Settings
LEARNING_STYLE_DISTRIBUTION = {
    "Visual": 0.35,
    "Auditory": 0.25,
    "Kinesthetic": 0.2,
    "Reading-Writing": 0.2
}

COURSE_DIFFICULTY_DISTRIBUTION = {
    1: 0.05,  # Very Easy
    2: 0.25,  # Easy
    3: 0.40,  # Medium
    4: 0.25,  # Hard
    5: 0.05   # Very Hard
}

GRADE_DISTRIBUTION = {
    "A": 0.15,
    "A-": 0.15,
    "B+": 0.15,
    "B": 0.15,
    "B-": 0.1,
    "C+": 0.1,
    "C": 0.08,
    "C-": 0.05,
    "D+": 0.03,
    "D": 0.02,
    "F": 0.01,
    "W": 0.01  # Withdrawal
}

# The departments at UMBC (focused on CS and Biology)
DEPARTMENTS = [
    "Computer Science",
    "Biology"
]

# Course levels and their weights (adjusted for CS and Biology focus)
COURSE_LEVELS = {
    100: 0.25,  # Freshman
    200: 0.30,  # Sophomore
    300: 0.30,  # Junior
    400: 0.15   # Senior
}

# =============================================================================
#                           UTILITY FUNCTIONS
# =============================================================================

def weighted_choice(choices_dict):
    """
    Make a weighted random choice from a dictionary of choices and weights.
    """
    choices = list(choices_dict.keys())
    weights = list(choices_dict.values())
    return random.choices(choices, weights=weights, k=1)[0]

def generate_campus_id():
    """
    Generate a realistic UMBC Campus ID (unique student identifier).
    Format: Typically 'AB12345' where:
    - 'AB' represents two letters
    - '12345' represents 5 digits
    """
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=5))
    return f"{letters}{numbers}"

def generate_course_id(department, level):
    """
    Generate a realistic course ID like 'CMSC 341' or 'ENGL 100'.
    """
    dept_prefix = ''.join([d[0] for d in department.split()[:2]]).upper()
    if len(dept_prefix) < 4:
        dept_prefix += random.choice(string.ascii_uppercase) * (4 - len(dept_prefix))
    return f"{dept_prefix[:4]} {level}"

def generate_course_name(department, level):
    """
    Generate realistic course names based on department and level.
    """
    dept_names = {
        "Computer Science": [
            # Core CS courses
            "Introduction to Programming", "Data Structures", 
            "Algorithms", "Operating Systems", "Computer Architecture",
            "Software Engineering", "Database Systems", "Computer Networks",
            "Programming Languages", "Theory of Computation",
            
            # Specialized CS courses
            "Artificial Intelligence", "Machine Learning", "Computer Graphics",
            "Cybersecurity", "Web Development", "Mobile Computing",
            "Cloud Computing", "Distributed Systems", "Compiler Design",
            "Computer Vision", "Natural Language Processing",
            
            # CS Electives
            "Game Development", "Blockchain Technology", "IoT Development",
            "Robotics", "Data Science", "Big Data Analytics",
            "Human-Computer Interaction", "Software Testing", "DevOps",
            "Quantum Computing", "Edge Computing"
        ],
        "Biology": [
            # Core Biology courses
            "General Biology", "Cell Biology", "Molecular Biology",
            "Genetics", "Ecology", "Evolution", "Microbiology",
            "Anatomy and Physiology", "Biochemistry", "Cell Physiology",
            "Developmental Biology", "Immunology",
            
            # Specialized Biology courses
            "Neurobiology", "Cancer Biology", "Plant Biology",
            "Animal Behavior", "Marine Biology", "Conservation Biology",
            "Population Genetics", "Molecular Genetics", "Bioinformatics",
            "Systems Biology", "Stem Cell Biology",
            
            # Biology Electives
            "Environmental Biology", "Tropical Biology", "Behavioral Ecology",
            "Comparative Anatomy", "Virology", "Parasitology",
            "Biotechnology", "Genomics", "Proteomics", "Metabolomics",
            "Synthetic Biology", "Computational Biology"
        ]
    }
    
    # Get course names for the department
    names = dept_names.get(department, ["Course"])
    
    # Add level-appropriate prefix/suffix
    if level < 200:
        prefixes = ["Introduction to ", "Fundamentals of ", "Principles of ", "Basic "]
        return f"{random.choice(prefixes)}{random.choice(names)}"
    elif level < 300:
        return f"{random.choice(names)}"
    elif level < 400:
        suffixes = [" I", " Analysis", " Methods", " Applications", " Theory"]
        return f"{random.choice(names)}{random.choice(suffixes)}"
    else:
        prefixes = ["Advanced ", "Topics in ", "Special Topics in "]
        return f"{random.choice(prefixes)}{random.choice(names)}"

def get_term_by_date(date):
    """
    Return the academic term (e.g., 'Fall2022') for a given date.
    """
    month = date.month
    year = date.year
    
    if 1 <= month <= 5:
        return f"Spring{year}"
    elif 6 <= month <= 7:
        return f"Summer{year}"
    else:
        return f"Fall{year}"

def generate_date(year_min, year_max=None):
    """
    Generate a random date between year_min and year_max.
    """
    if year_max is None:
        year_max = year_min
        
    start_date = datetime.date(year_min, 1, 1)
    end_date = datetime.date(year_max, 12, 31)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_days = random.randrange(days_between_dates)
    
    return start_date + datetime.timedelta(days=random_days)

# =============================================================================
#                           DATA GENERATION
# =============================================================================

def generate_terms():
    """
    Generate academic terms for the past few years and upcoming year.
    """
    terms = []
    current_year = datetime.datetime.now().year
    start_year = current_year - HISTORY_YEARS
    end_year = current_year + 1
    
    term_info = {
        "Spring": {"start_month": 1, "start_day": 25, "end_month": 5, "end_day": 15},
        "Summer": {"start_month": 6, "start_day": 1, "end_month": 7, "end_day": 30},
        "Fall": {"start_month": 8, "start_day": 25, "end_month": 12, "end_day": 15}
    }
    
    for year in range(start_year, end_year + 1):
        for term_name, dates in term_info.items():
            term_id = f"{term_name}{year}"
            
            # Skip generating too many terms if we exceed TERMS_TO_GENERATE
            if len(terms) >= TERMS_TO_GENERATE:
                break
                
            start_date = datetime.date(year, dates["start_month"], dates["start_day"])
            end_date = datetime.date(year, dates["end_month"], dates["end_day"])
            
            terms.append({
                "id": term_id,
                "name": f"{term_name} {year}",
                "startDate": start_date.strftime("%Y-%m-%d"),
                "endDate": end_date.strftime("%Y-%m-%d"),
                "type": term_name
            })
    
    return terms

def generate_students():
    """
    Generate student data.
    """
    students = []
    
    current_year = datetime.datetime.now().year
    
    learning_styles = list(LEARNING_STYLE_DISTRIBUTION.keys())
    learning_style_weights = list(LEARNING_STYLE_DISTRIBUTION.values())
    
    course_loads = {
        "Accelerated": 0.1,
        "Standard": 0.7,
        "Part-time": 0.2
    }
    
    instruction_prefs = {
        "In-person": 0.6,
        "Online": 0.2,
        "Hybrid": 0.2
    }
    
    financial_statuses = {
        "Scholarship": 0.15,
        "FinancialAid": 0.35,
        "Self-Pay": 0.35,
        "Loans": 0.15
    }
    
    for i in range(NUM_STUDENTS):
        # Generate basic info
        campus_id = generate_campus_id()
        
        # Ensure campus_id is unique
        while any(s["id"] == campus_id for s in students):
            campus_id = generate_campus_id()
            
        # Use faker for name generation
        first_name = fake.first_name()
        last_name = fake.last_name()
        
        # Generate enrollment date (between 1-5 years ago)
        enrollment_years_ago = random.randint(1, 5)
        enrollment_date = generate_date(current_year - enrollment_years_ago, current_year)
        
        # Generate expected graduation (1-4 years from enrollment)
        grad_years = random.randint(1, 4) if enrollment_years_ago <= 3 else random.randint(0, 2)
        expected_graduation = generate_date(current_year + grad_years)
        
        # Learning style
        learning_style = random.choices(learning_styles, weights=learning_style_weights)[0]
        
        # Course load preference
        preferred_course_load = random.randint(2, 5)
        preferred_pace = weighted_choice(course_loads)
        
        # Work hours
        work_hours = 0
        if preferred_pace == "Part-time":
            work_hours = random.randint(20, 40)
        elif preferred_pace == "Standard":
            work_hours = random.randint(0, 20)
        
        # Financial aid status
        financial_aid_status = weighted_choice(financial_statuses)
        
        # Preferred instruction mode
        preferred_instruction_mode = weighted_choice(instruction_prefs)
        
        students.append({
            "id": campus_id,
            "name": f"{first_name} {last_name}",
            "enrollmentDate": enrollment_date.strftime("%Y-%m-%d"),
            "expectedGraduation": expected_graduation.strftime("%Y-%m-%d"),
            "learningStyle": learning_style,
            "preferredCourseLoad": preferred_course_load,
            "preferredPace": preferred_pace,
            "workHoursPerWeek": work_hours,
            "financialAidStatus": financial_aid_status,
            "preferredInstructionMode": preferred_instruction_mode
        })
    
    return students

def generate_faculty():
    """
    Generate faculty data.
    """
    faculty = []
    
    titles = ["Dr.", "Professor", "Dr.", "Professor", "Dr.", "Assoc. Prof.", "Asst. Prof."]
    
    teaching_styles = [
        "Lecture", "Discussion", "Problem-Based", "Flipped Classroom", 
        "Case Study", "Project-Based", "Hands-on", "Collaborative",
        "Socratic", "Demonstrative", "Research-Oriented", "Activity-Based"
    ]
    
    faculty_by_dept = defaultdict(list)
    
    for i in range(NUM_FACULTY):
        faculty_id = f"F{str(i+1001).zfill(5)}"
        
        title = random.choice(titles)
        # Use faker for name generation
        first_name = fake.first_name()
        last_name = fake.last_name()
        name = f"{title} {first_name} {last_name}"
        
        # Assign department
        department = random.choice(DEPARTMENTS)
        
        # Assign 1-3 teaching styles
        num_styles = random.randint(1, 3)
        faculty_teaching_styles = random.sample(teaching_styles, num_styles)
        
        # Random rating between 3.0 and 5.0
        avg_rating = round(random.uniform(3.0, 5.0), 1)
        
        faculty_data = {
            "id": faculty_id,
            "name": name,
            "department": department,
            "teachingStyle": faculty_teaching_styles,
            "avgRating": avg_rating
        }
        
        faculty.append(faculty_data)
        faculty_by_dept[department].append(faculty_data)
    
    return faculty, faculty_by_dept

def generate_courses(faculty_by_dept):
    """
    Generate course data for CS and Biology departments.
    """
    courses = []
    dept_courses = defaultdict(list)
    
    # Generate courses for each department
    for dept in DEPARTMENTS:
        # Number of courses for this department
        dept_course_count = max(25, int(NUM_COURSES * (1 / len(DEPARTMENTS))))
        
        for i in range(dept_course_count):
            # Pick a course level
            level = weighted_choice(COURSE_LEVELS)
            
            # Generate course ID and name
            course_id = generate_course_id(dept, level)
            
            # Ensure course_id is unique
            while any(c["id"] == course_id for c in courses):
                course_id = f"{course_id}-{random.randint(1, 9)}"
                
            course_name = generate_course_name(dept, level)
            
            # Generate course difficulty (adjusted for CS and Biology)
            avg_difficulty = weighted_choice(COURSE_DIFFICULTY_DISTRIBUTION)
            
            # Generate time commitment (hours per week)
            avg_time_commitment = level // 100 + avg_difficulty + random.randint(1, 3)
            
            # Available terms
            available_terms = ["Fall", "Spring"]
            if random.random() < 0.3:  # 30% chance to be offered in summer
                available_terms.append("Summer")
                
            # Instruction modes
            instruction_modes = ["In-person"]
            if random.random() < 0.6:  # 60% chance for online option
                instruction_modes.append("Online")
            if random.random() < 0.4:  # 40% chance for hybrid option
                instruction_modes.append("Hybrid")
                
            # Credit hours (most are 3, some are 4, few are 1 or 2)
            if random.random() < 0.7:
                credits = 3
            elif random.random() < 0.2:
                credits = 4
            else:
                credits = random.choice([1, 2])
                
            # Topic tags
            tags = [dept, f"Level-{level//100}"]
            if "Introduction" in course_name:
                tags.append("Intro")
            if "Advanced" in course_name:
                tags.append("Advanced")
                
            # Add specific topic tags based on course name
            topic_keywords = {
                "Computer Science": [
                    "Programming", "Data", "Theory", "Analysis", "Design", 
                    "Research", "Applications", "Methods", "Systems", "Project",
                    "AI", "ML", "Security", "Web", "Mobile", "Cloud",
                    "Distributed", "Compiler", "Vision", "NLP", "Game",
                    "Blockchain", "IoT", "Robotics", "Data Science", "HCI"
                ],
                "Biology": [
                    "Cell", "Molecular", "Genetics", "Ecology", "Evolution",
                    "Micro", "Anatomy", "Physiology", "Biochemistry", "Development",
                    "Neuro", "Cancer", "Plant", "Animal", "Marine", "Conservation",
                    "Population", "Bioinformatics", "Systems", "Stem Cell",
                    "Environmental", "Tropical", "Behavioral", "Comparative",
                    "Virology", "Parasitology", "Biotech", "Genomics"
                ]
            }
            
            for keyword in topic_keywords.get(dept, []):
                if keyword.lower() in course_name.lower():
                    tags.append(keyword)
                    
            # Create learning style success rates
            visual_success = round(random.uniform(0.6, 1.0), 2)
            auditory_success = round(random.uniform(0.6, 1.0), 2)
            kinesthetic_success = round(random.uniform(0.6, 1.0), 2)
            reading_success = round(random.uniform(0.6, 1.0), 2)
            
            # Make certain courses favor certain learning styles
            if "Lab" in course_name or "Practical" in course_name:
                kinesthetic_success = min(1.0, kinesthetic_success + 0.2)
            if "Lecture" in course_name or "Theory" in course_name:
                auditory_success = min(1.0, auditory_success + 0.2)
            if "Design" in course_name or "Graphics" in course_name:
                visual_success = min(1.0, visual_success + 0.2)
            if "Literature" in course_name or "Research" in course_name:
                reading_success = min(1.0, reading_success + 0.2)
            
            course = {
                "id": course_id,
                "name": course_name,
                "department": dept,
                "credits": credits,
                "level": level,
                "avgDifficulty": avg_difficulty,
                "avgTimeCommitment": avg_time_commitment,
                "termAvailability": available_terms,
                "instructionModes": instruction_modes,
                "tags": tags,
                "visualLearnerSuccess": visual_success,
                "auditoryLearnerSuccess": auditory_success,
                "kinestheticLearnerSuccess": kinesthetic_success,
                "readingLearnerSuccess": reading_success
            }
            
            courses.append(course)
            dept_courses[dept].append(course)
    
    return courses, dept_courses

def generate_degrees(dept_courses):
    """
    Generate degree programs for CS and Biology.
    """
    degrees = []
    requirement_groups = []
    
    # Define degree types for each department
    degree_configs = {
        "Computer Science": [
            {
                "type": "Bachelor of Science",
                "prefix": "BS",
                "total_credits": 120,
                "core_credits": 75,
                "elective_credits": 45
            },
            {
                "type": "Bachelor of Arts",
                "prefix": "BA",
                "total_credits": 120,
                "core_credits": 60,
                "elective_credits": 60
            }
        ],
        "Biology": [
            {
                "type": "Bachelor of Science",
                "prefix": "BS",
                "total_credits": 120,
                "core_credits": 80,
                "elective_credits": 40
            },
            {
                "type": "Bachelor of Arts",
                "prefix": "BA",
                "total_credits": 120,
                "core_credits": 65,
                "elective_credits": 55
            }
        ]
    }
    
    for dept, configs in degree_configs.items():
        for i, config in enumerate(configs):
            degree_id = f"{config['prefix']}-{dept.replace(' ', '')}-{i+1}"
            degree_name = f"{config['type']} in {dept}"
            
            degree = {
                "id": degree_id,
                "name": degree_name,
                "department": dept,
                "type": config["type"].split()[0],  # "Bachelor"
                "totalCreditsRequired": config["total_credits"],
                "coreCreditsRequired": config["core_credits"],
                "electiveCreditsRequired": config["elective_credits"]
            }
            
            degrees.append(degree)
            
            # Generate requirement groups for this degree
            available_courses = dept_courses[dept].copy()
            
            # Core requirements group
            core_req_id = f"REQ-CORE-{degree_id}"
            core_req_name = f"Core {dept} Requirements"
            
            # Select core courses (higher level courses are more likely to be required)
            core_courses = []
            level_weights = {
                100: 0.2,
                200: 0.3,
                300: 0.4,
                400: 0.5
            }
            
            # Sort by level and randomly select based on level weights
            sorted_by_level = sorted(available_courses, key=lambda x: x["level"])
            target_core_courses = min(25, len(available_courses) // 2)
            
            for course in sorted_by_level:
                level = course["level"]
                weight = level_weights.get(level, 0.3)
                
                if random.random() < weight and len(core_courses) < target_core_courses:
                    core_courses.append(course)
            
            # Calculate credits
            core_min_credits = sum([c["credits"] for c in core_courses])
            core_min_courses = len(core_courses)
            
            core_requirement = {
                "id": core_req_id,
                "name": core_req_name,
                "description": f"Required courses for {degree_name}",
                "minimumCourses": core_min_courses,
                "minimumCredits": core_min_credits,
                "degreeId": degree_id,
                "courses": [c["id"] for c in core_courses]
            }
            
            requirement_groups.append(core_requirement)
            
            # Remaining requirement groups (electives, concentrations, etc.)
            remaining_courses = [c for c in available_courses if c not in core_courses]
            
            # Add some related department courses for electives
            related_dept = "Biology" if dept == "Computer Science" else "Computer Science"
            if related_dept in dept_courses:
                remaining_courses.extend(random.sample(dept_courses[related_dept], 
                                                   min(10, len(dept_courses[related_dept]))))
            
            # Create elective requirement groups
            num_req_groups = 3  # Fixed number of requirement groups per degree
            
            for j in range(num_req_groups - 1):
                req_type = random.choice(["Elective", "Concentration", "Specialization"])
                req_id = f"REQ-{req_type.upper()}-{j+1}-{degree_id}"
                req_name = f"{dept} {req_type} Requirements - Group {j+1}"
                
                # Select a subset of remaining courses for this requirement
                num_req_courses = random.randint(3, 8)
                if remaining_courses:
                    req_courses = random.sample(remaining_courses, min(num_req_courses, len(remaining_courses)))
                else:
                    req_courses = []
                    
                # How many of these are required?
                min_courses = random.randint(1, max(1, len(req_courses) - 1))
                min_credits = min_courses * 3  # Approximate
                
                req_requirement = {
                    "id": req_id,
                    "name": req_name,
                    "description": f"{req_type} courses for {degree_name}",
                    "minimumCourses": min_courses,
                    "minimumCredits": min_credits,
                    "degreeId": degree_id,
                    "courses": [c["id"] for c in req_courses]
                }
                
                requirement_groups.append(req_requirement)
    
    return degrees, requirement_groups

def generate_prerequisites(courses):
    """
    Generate prerequisite relationships between courses for CS and Biology.
    """
    prerequisites = []
    
    # Group courses by department and level
    by_dept_level = defaultdict(list)
    for course in courses:
        by_dept_level[(course["department"], course["level"])].append(course)
    
    # Define core prerequisite sequences for each department
    core_sequences = {
        "Computer Science": [
            # Programming sequence
            ["Introduction to Programming", "Data Structures", "Algorithms"],
            # Systems sequence
            ["Computer Architecture", "Operating Systems", "Computer Networks"],
            # Theory sequence
            ["Theory of Computation", "Compiler Design"],
            # Software sequence
            ["Software Engineering", "Database Systems"],
            # AI/ML sequence
            ["Artificial Intelligence", "Machine Learning", "Deep Learning"]
        ],
        "Biology": [
            # Core sequence
            ["General Biology", "Cell Biology", "Molecular Biology"],
            # Genetics sequence
            ["Genetics", "Molecular Genetics", "Population Genetics"],
            # Physiology sequence
            ["Anatomy and Physiology", "Cell Physiology", "Developmental Biology"],
            # Ecology sequence
            ["Ecology", "Evolution", "Conservation Biology"],
            # Specialized sequences
            ["Microbiology", "Immunology"],
            ["Biochemistry", "Systems Biology"]
        ]
    }
    
    for dept, sequences in core_sequences.items():
        for sequence in sequences:
            for i in range(len(sequence) - 1):
                # Find the prerequisite course
                prereq_name = sequence[i]
                prereq_courses = [c for c in courses 
                                if c["department"] == dept and 
                                prereq_name.lower() in c["name"].lower()]
                
                # Find the target course
                target_name = sequence[i + 1]
                target_courses = [c for c in courses 
                                if c["department"] == dept and 
                                target_name.lower() in c["name"].lower()]
                
                if prereq_courses and target_courses:
                    prereq = prereq_courses[0]
                    target = target_courses[0]
                    
                    prerequisites.append({
                        "source": prereq["id"],
                        "target": target["id"],
                        "strength": "Required",
                        "minGrade": "C"
                    })
    
    # Add additional prerequisites based on course level
    for course in courses:
        dept = course["department"]
        level = course["level"]
        
        # Higher-level courses have prerequisites
        if level > 100:
            # Number of prerequisites
            num_prereqs = 0
            if level <= 200:
                num_prereqs = random.randint(0, 1)
            elif level <= 300:
                num_prereqs = random.randint(1, 2)
            elif level <= 400:
                num_prereqs = random.randint(1, 3)
                
            num_prereqs = min(num_prereqs, MAX_PREREQS_PER_COURSE)
            
            # Select prerequisites (prefer lower-level courses from same department)
            potential_prereqs = []
            for l in range(100, level, 100):
                if (dept, l) in by_dept_level:
                    potential_prereqs.extend(by_dept_level[(dept, l)])
            
            # If we don't have enough potential prerequisites, look at other departments
            if len(potential_prereqs) < num_prereqs:
                other_dept = "Biology" if dept == "Computer Science" else "Computer Science"
                for l in range(100, level, 100):
                    if (other_dept, l) in by_dept_level:
                        potential_prereqs.extend(by_dept_level[(other_dept, l)])
            
            # If we still don't have enough, reduce number of prerequisites
            num_prereqs = min(num_prereqs, len(potential_prereqs))
            
            # Select the prerequisites
            selected_prereqs = random.sample(potential_prereqs, num_prereqs) if num_prereqs > 0 else []
            
            for prereq in selected_prereqs:
                # Sometimes make it a "recommended" prerequisite
                strength = "Required" if random.random() < 0.8 else "Recommended"
                
                # Minimum grade requirement
                min_grade = random.choice(["C", "C-", "D", "D-"]) if strength == "Required" else ""
                
                prerequisites.append({
                    "source": prereq["id"],
                    "target": course["id"],
                    "strength": strength,
                    "minGrade": min_grade
                })
    
    return prerequisites

def generate_leads_to_relationships(courses, prerequisites):
    """
    Generate "LEADS_TO" relationships between courses (common course sequences).
    """
    leads_to = []
    
    # Build a graph of prerequisites to help determine potential leads_to relationships
    prereq_graph = defaultdict(list)
    for p in prerequisites:
        prereq_graph[p["source"]].append(p["target"])
    
    for course in courses:
        # Courses that list this as a prerequisite
        followers = prereq_graph.get(course["id"], [])
        
        # Create LEADS_TO to most followers
        for follower_id in followers:
            # Most prerequisites also have LEADS_TO with high commonality
            if random.random() < 0.9:
                leads_to.append({
                    "source": course["id"],
                    "target": follower_id,
                    "commonality": round(random.uniform(0.7, 1.0), 2),
                    "successCorrelation": round(random.uniform(0.6, 0.9), 2)
                })
        
        # Some random LEADS_TO relationships for courses in same department at next level
        dept = course["department"]
        level = course["level"]
        next_level = level + 100
        
        same_dept_next_level = [c for c in courses 
                               if c["department"] == dept and c["level"] == next_level]
        
        # Randomly create some LEADS_TO that aren't prerequisites
        for potential in same_dept_next_level:
            if potential["id"] not in followers and random.random() < 0.3:
                leads_to.append({
                    "source": course["id"],
                    "target": potential["id"],
                    "commonality": round(random.uniform(0.2, 0.6), 2),
                    "successCorrelation": round(random.uniform(0.4, 0.7), 2)
                })
    
    return leads_to

def generate_course_similarity(courses):
    """
    Generate similarity relationships between courses.
    """
    similarity_content = []
    similarity_difficulty = []
    
    # Group courses by department and tags
    by_dept = defaultdict(list)
    by_tag = defaultdict(list)
    
    for course in courses:
        by_dept[course["department"]].append(course)
        for tag in course.get("tags", []):
            by_tag[tag].append(course)
    
    # Generate content similarity within departments and shared tags
    for course in courses:
        # Find similar courses in same department
        same_dept_courses = by_dept[course["department"]]
        
        # Find courses with shared tags
        shared_tag_courses = []
        for tag in course.get("tags", []):
            shared_tag_courses.extend(by_tag[tag])
        
        # Create content similarity to some courses in same department
        for similar in same_dept_courses:
            if similar["id"] != course["id"] and random.random() < 0.1:
                similarity_score = round(random.uniform(0.1, 0.8), 2)
                similarity_content.append({
                    "source": course["id"],
                    "target": similar["id"],
                    "similarity": similarity_score
                })
        
        # Create content similarity to courses with shared tags
        # Create a list of unique course IDs to avoid duplicates
        seen_course_ids = set()
        for similar in shared_tag_courses:
            if similar["id"] not in seen_course_ids:
                seen_course_ids.add(similar["id"])
            if similar["id"] != course["id"] and random.random() < 0.2:
                # Higher similarity for more shared tags
                course_tags = set(course.get("tags", []))
                similar_tags = set(similar.get("tags", []))
                shared_tags = len(course_tags.intersection(similar_tags))
                
                base_similarity = 0.2 + (shared_tags * 0.1)
                similarity_score = round(min(0.9, base_similarity + random.uniform(0, 0.2)), 2)
                
                similarity_content.append({
                    "source": course["id"],
                    "target": similar["id"],
                    "similarity": similarity_score
                })
        
        # Create difficulty similarity to some random courses
        for similar in random.sample(courses, min(10, len(courses))):
            if similar["id"] != course["id"] and abs(course["avgDifficulty"] - similar["avgDifficulty"]) <= 1:
                difficulty_diff = abs(course["avgDifficulty"] - similar["avgDifficulty"])
                similarity_score = round(1.0 - (difficulty_diff / 5.0), 2)
                
                similarity_difficulty.append({
                    "source": course["id"],
                    "target": similar["id"],
                    "similarity": similarity_score
                })
    
    # Remove duplicates by converting to dictionary with (source,target) as key
    content_dict = {(s["source"], s["target"]): s for s in similarity_content}
    difficulty_dict = {(s["source"], s["target"]): s for s in similarity_difficulty}
    
    return list(content_dict.values()), list(difficulty_dict.values())

def generate_student_degree_relationships(students, degrees):
    """
    Generate relationships between students and degrees.
    """
    student_degree = []
    
    for student in students:
        # Each student pursues at least one degree
        primary_degree = random.choice(degrees)
        
        student_degree.append({
            "studentId": student["id"],
            "degreeId": primary_degree["id"]
        })
        
        # Some students pursue a second degree
        if random.random() < 0.1:  # 10% chance for double major
            second_degree = random.choice([d for d in degrees if d["id"] != primary_degree["id"]])
            
            student_degree.append({
                "studentId": student["id"],
                "degreeId": second_degree["id"]
            })
    
    return student_degree

def generate_teaching_relationships(faculty_by_dept, courses):
    """
    Generate teaching relationships between faculty and courses.
    """
    teaching = []
    
    for course in courses:
        dept = course["department"]
        potential_faculty = faculty_by_dept.get(dept, [])
        
        # If no faculty in that department, pick random faculty
        if not potential_faculty:
            potential_faculty = random.sample([f for depts in faculty_by_dept.values() for f in depts], 
                                min(3, sum(len(f) for f in faculty_by_dept.values())))
        
        # Assign 1-3 faculty to teach this course
        num_faculty = random.randint(1, min(3, len(potential_faculty)))
        selected_faculty = random.sample(potential_faculty, num_faculty)
        
        for faculty in selected_faculty:
            # Which terms they teach
            taught_terms = []
            for term in ["Fall", "Spring", "Summer"]:
                if term in course["termAvailability"] and random.random() < 0.7:
                    taught_terms.append(term)
            
            if taught_terms:  # Only create relationship if they actually teach in some terms
                teaching.append({
                    "facultyId": faculty["id"],
                    "courseId": course["id"],
                    "terms": taught_terms
                })
    
    return teaching

def generate_student_course_history(students, courses, terms, prerequisites):
    """
    Generate student course history.
    """
    completed_courses = []
    enrolled_courses = []
    
    # Build prerequisite graph
    prereq_graph = defaultdict(list)
    for p in prerequisites:
        target_id = p["target"]
        source_id = p["source"]
        prereq_graph[target_id].append(source_id)
    
    # Current term
    now = datetime.datetime.now()
    current_term = get_term_by_date(now)
    
    # Find current term object
    current_term_obj = next((t for t in terms if t["id"] == current_term), None)
    if not current_term_obj:
        current_term_obj = terms[-1]  # Use last term if current not found
    
    for student in students:
        # Determine how many courses this student has taken
        enrollment_date = datetime.datetime.strptime(student["enrollmentDate"], "%Y-%m-%d")
        terms_enrolled = min(TERMS_TO_GENERATE, 
                            (now - enrollment_date).days // 120)  # ~4 months per term
        
        # If zero terms, they're brand new
        if terms_enrolled == 0:
            terms_enrolled = 1
        
        # Which terms were they enrolled in?
        enrolled_term_indices = list(range(max(0, len(terms) - terms_enrolled), len(terms)))
        
        # Last X terms (chronological order)
        student_terms = [terms[i] for i in enrolled_term_indices]
        
        # Track courses taken by this student
        taken_courses = set()
        
        # For each term
        for term_idx, term in enumerate(student_terms):
            # How many courses in this term?
            num_courses = random.randint(1, student["preferredCourseLoad"])
            
            # Get potential courses for this term
            term_type = term["type"]  # e.g., "Fall", "Spring"
            potential_courses = [
                c for c in courses 
                if term_type in c["termAvailability"] and c["id"] not in taken_courses
            ]
            
            # Filter out courses where prerequisites aren't met
            valid_courses = []
            for course in potential_courses:
                prereqs = prereq_graph.get(course["id"], [])
                if all(p in taken_courses for p in prereqs):
                    valid_courses.append(course)
            
            # If no valid courses, use some without prerequisites
            if not valid_courses:
                valid_courses = [c for c in potential_courses if not prereq_graph.get(c["id"], [])]
            
            # Select courses for this term
            term_courses = random.sample(valid_courses, min(num_courses, len(valid_courses)))
            
            for course in term_courses:
                # Add to taken courses
                taken_courses.add(course["id"])
                
                # If this is the current term, they're enrolled
                if term["id"] == current_term_obj["id"]:
                    enrolled_courses.append({
                        "studentId": student["id"],
                        "courseId": course["id"],
                        "term": term["id"]
                    })
                    continue
                
                # For past terms, generate completion record
                if datetime.datetime.strptime(term["endDate"], "%Y-%m-%d") < now:
                    # Generate grade
                    grade = weighted_choice(GRADE_DISTRIBUTION)
                    
                    # Generate difficulty rating (influenced by learning style match)
                    student_style = student["learningStyle"]
                    base_difficulty = course["avgDifficulty"]
                    
                    # Adjust difficulty based on learning style match
                    style_match_modifier = 0
                    if student_style == "Visual" and "visualLearnerSuccess" in course:
                        style_match_modifier = (course["visualLearnerSuccess"] - 0.8) * 2
                    elif student_style == "Auditory" and "auditoryLearnerSuccess" in course:
                        style_match_modifier = (course["auditoryLearnerSuccess"] - 0.8) * 2
                    elif student_style == "Kinesthetic" and "kinestheticLearnerSuccess" in course:
                        style_match_modifier = (course["kinestheticLearnerSuccess"] - 0.8) * 2
                    elif student_style == "Reading-Writing" and "readingLearnerSuccess" in course:
                        style_match_modifier = (course["readingLearnerSuccess"] - 0.8) * 2
                    
                    perceived_difficulty = max(1, min(5, round(base_difficulty - style_match_modifier)))
                    
                    # Time spent (hours per week)
                    avg_time = course["avgTimeCommitment"]
                    time_spent = max(1, int(avg_time * random.uniform(0.7, 1.3)))
                    
                    # Instruction mode
                    instruction_mode = random.choice(course["instructionModes"])
                    
                    # Enjoyment (boolean)
                    enjoyment = grade in ["A", "A-", "B+", "B"] and perceived_difficulty <= 4
                    
                    completed_courses.append({
                        "studentId": student["id"],
                        "courseId": course["id"],
                        "term": term["id"],
                        "grade": grade,
                        "difficulty": perceived_difficulty,
                        "timeSpent": time_spent,
                        "instructionMode": instruction_mode,
                        "enjoyment": enjoyment
                    })
    
    return completed_courses, enrolled_courses

def generate_student_similarity(students, completed_courses):
    """
    Generate similarity relationships between students.
    """
    learning_style_similarity = []
    performance_similarity = []
    
    # Group students by learning style
    by_style = defaultdict(list)
    for student in students:
        by_style[student["learningStyle"]].append(student)
    
    # Group completed courses by student
    student_courses = defaultdict(list)
    for completed in completed_courses:
        student_courses[completed["studentId"]].append(completed)
    
    # For each student
    for i, student in enumerate(students):
        # Similar learning style students
        same_style_students = by_style[student["learningStyle"]]
        
        # Pick a subset to create relationships with
        num_similar = min(20, len(same_style_students))
        similar_students = random.sample(same_style_students, num_similar)
        
        for similar in similar_students:
            if similar["id"] == student["id"]:
                continue
                
            # Calculate similarity (higher for same pace, course load)
            base_similarity = 0.7  # Base similarity for same learning style
            
            if similar["preferredPace"] == student["preferredPace"]:
                base_similarity += 0.1
                
            load_diff = abs(similar["preferredCourseLoad"] - student["preferredCourseLoad"])
            base_similarity -= (load_diff * 0.02)
            
            if similar["preferredInstructionMode"] == student["preferredInstructionMode"]:
                base_similarity += 0.1
                
            similarity_score = round(max(0.1, min(1.0, base_similarity + random.uniform(-0.1, 0.1))), 2)
            
            learning_style_similarity.append({
                "sourceId": student["id"],
                "targetId": similar["id"],
                "similarity": similarity_score
            })
        
        # Performance similarity (for students who took same courses)
        student_taken = {c["courseId"]: c for c in student_courses.get(student["id"], [])}
        
        # Only process every few students (for performance)
        if i % 5 == 0:
            for other_student in students:
                if other_student["id"] == student["id"]:
                    continue
                    
                other_taken = {c["courseId"]: c for c in student_courses.get(other_student["id"], [])}
                
                # Find courses both students have taken
                common_courses = set(student_taken.keys()).intersection(set(other_taken.keys()))
                
                if len(common_courses) >= 3:  # Only if they have several courses in common
                    # Calculate grade similarity
                    grade_map = {
                        "A": 4.0, "A-": 3.7,
                        "B+": 3.3, "B": 3.0, "B-": 2.7,
                        "C+": 2.3, "C": 2.0, "C-": 1.7,
                        "D+": 1.3, "D": 1.0, "D-": 0.7,
                        "F": 0.0, "W": 0.0
                    }
                    
                    # Calculate grade difference
                    grade_diffs = []
                    for course_id in common_courses:
                        student_grade = grade_map.get(student_taken[course_id]["grade"], 0)
                        other_grade = grade_map.get(other_taken[course_id]["grade"], 0)
                        
                        grade_diffs.append(abs(student_grade - other_grade))
                    
                    avg_grade_diff = sum(grade_diffs) / len(grade_diffs)
                    grade_similarity = max(0, 1 - (avg_grade_diff / 4.0))
                    
                    # Calculate difficulty perception similarity
                    difficulty_diffs = []
                    for course_id in common_courses:
                        student_diff = student_taken[course_id]["difficulty"]
                        other_diff = other_taken[course_id]["difficulty"]
                        
                        difficulty_diffs.append(abs(student_diff - other_diff))
                    
                    avg_diff_diff = sum(difficulty_diffs) / len(difficulty_diffs)
                    diff_similarity = max(0, 1 - (avg_diff_diff / 5.0))
                    
                    # Overall similarity
                    overall_similarity = round((grade_similarity * 0.7 + diff_similarity * 0.3), 2)
                    
                    performance_similarity.append({
                        "sourceId": student["id"],
                        "targetId": other_student["id"],
                        "similarity": overall_similarity,
                        "courses": list(common_courses)
                    })
    
    return learning_style_similarity, performance_similarity

def generate_textbooks(courses):
    """
    Generate textbooks for courses with realistic metadata.
    """
    textbooks = []
    course_textbooks = []
    
    # Define textbook categories and their characteristics
    textbook_categories = {
        "Computer Science": {
            "Programming": {
                "publishers": ["O'Reilly", "Addison-Wesley", "Prentice Hall", "Manning"],
                "price_range": (40, 120),
                "avg_pages": 800,
                "page_variance": 200
            },
            "Theory": {
                "publishers": ["Springer", "MIT Press", "Cambridge University Press"],
                "price_range": (60, 150),
                "avg_pages": 600,
                "page_variance": 150
            },
            "Systems": {
                "publishers": ["Pearson", "McGraw-Hill", "Wiley"],
                "price_range": (50, 130),
                "avg_pages": 700,
                "page_variance": 180
            }
        },
        "Biology": {
            "General": {
                "publishers": ["Pearson", "McGraw-Hill", "Wiley", "Cengage"],
                "price_range": (80, 200),
                "avg_pages": 1000,
                "page_variance": 250
            },
            "Specialized": {
                "publishers": ["Springer", "Elsevier", "Oxford University Press"],
                "price_range": (70, 180),
                "avg_pages": 800,
                "page_variance": 200
            },
            "Lab": {
                "publishers": ["Pearson", "McGraw-Hill", "Cengage"],
                "price_range": (40, 100),
                "avg_pages": 400,
                "page_variance": 100
            }
        }
    }
    
    # Generate textbooks for each course
    for course in courses:
        dept = course["department"]
        level = course["level"]
        
        # Determine number of textbooks (1-3 per course)
        num_textbooks = random.choices([1, 2, 3], weights=[0.5, 0.3, 0.2])[0]
        
        # Determine course category based on name and level
        course_category = None
        if dept == "Computer Science":
            if "Programming" in course["name"] or "Software" in course["name"]:
                course_category = "Programming"
            elif "Theory" in course["name"] or "Algorithms" in course["name"]:
                course_category = "Theory"
            else:
                course_category = "Systems"
        else:  # Biology
            if "Lab" in course["name"] or "Practical" in course["name"]:
                course_category = "Lab"
            elif level <= 200:
                course_category = "General"
            else:
                course_category = "Specialized"
        
        # Get category characteristics
        cat_info = textbook_categories[dept][course_category]
        
        # Generate textbooks for this course
        for i in range(num_textbooks):
            # Generate unique textbook ID
            textbook_id = f"TXT-{dept[:3]}-{level}-{i+1}"
            
            # Generate realistic textbook name
            if i == 0:  # Primary textbook
                if level <= 200:
                    name = f"Introduction to {course['name']}"
                else:
                    name = f"Advanced {course['name']}"
            else:  # Supplementary textbooks
                name = f"{course['name']}: {random.choice(['A Comprehensive Guide', 'Principles and Applications', 'Theory and Practice', 'Case Studies', 'Problem Solving'])}"
            
            # Generate metadata
            publisher = random.choice(cat_info["publishers"])
            price = round(random.uniform(*cat_info["price_range"]), 2)
            pages = int(random.gauss(cat_info["avg_pages"], cat_info["page_variance"]))
            pages = max(100, min(2000, pages))  # Ensure reasonable page count
            
            # Generate edition (1st-5th)
            edition = random.randint(1, 5)
            
            # Generate publication year (more recent for higher levels)
            base_year = 2020 - (level // 100)  # Higher level = newer books
            pub_year = random.randint(base_year, 2023)
            
            # Generate ISBN
            isbn = f"978-{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}-{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}-{random.randint(0,9)}"
            
            textbook = {
                "id": textbook_id,
                "name": name,
                "publisher": publisher,
                "price": price,
                "pages": pages,
                "edition": edition,
                "publicationYear": pub_year,
                "isbn": isbn,
                "category": course_category
            }
            
            textbooks.append(textbook)
            
            # Create course-textbook relationship
            course_textbooks.append({
                "courseId": course["id"],
                "textbookId": textbook_id,
                "isRequired": i == 0,  # First textbook is required
                "recommendedOrder": i + 1  # Order in which textbooks are recommended
            })
    
    return textbooks, course_textbooks

def generate_textbook_interactions(students, courses, textbooks, course_textbooks, terms, completed_courses):
    """Generate realistic textbook interaction patterns."""
    interactions = []
    page_views = []
    
    # Create lookup for completed courses by student
    student_courses = defaultdict(list)
    for comp in completed_courses:
        student_courses[comp["studentId"]].append(comp)
    
    # Create lookup for course textbooks
    course_text_lookup = defaultdict(list)
    for ct in course_textbooks:
        course_text_lookup[ct["courseId"]].append(
            next(t for t in textbooks if t["id"] == ct["textbookId"])
        )
    
    for student in students:
        # Get all completed courses for this student
        student_completed = student_courses[student["id"]]
        
        for comp in student_completed:
            # Get textbooks for this course
            course_texts = course_text_lookup[comp["courseId"]]
            if not course_texts:
                continue
                
            # Generate interaction patterns based on student's learning style
            if student["learningStyle"] == "Visual":
                # Visual learners tend to read more frequently but for shorter durations
                num_sessions = random.randint(15, 25)
                avg_duration = random.randint(2, 5)
            elif student["learningStyle"] == "Auditory":
                # Auditory learners might read less frequently but for longer durations
                num_sessions = random.randint(8, 15)
                avg_duration = random.randint(5, 10)
            else:  # Reading-Writing or Kinesthetic
                # Reading/writing learners have consistent reading patterns
                num_sessions = random.randint(12, 20)
                avg_duration = random.randint(3, 7)
            
            # Get the term dates for this completed course
            term = next(t for t in terms if t["id"] == comp["term"])
            term_start = datetime.datetime.strptime(term["startDate"], "%Y-%m-%d")
            term_end = datetime.datetime.strptime(term["endDate"], "%Y-%m-%d")
            
            # Generate page views for each session
            for session in range(num_sessions):
                # Randomly select a textbook for this session
                textbook = random.choice(course_texts)
                num_pages = random.randint(5, 15)
                
                # Generate timestamps for this session
                session_start = term_start + datetime.timedelta(
                    days=random.randint(0, (term_end - term_start).days),
                    hours=random.randint(8, 22)  # During reasonable hours
                )
                
                for page in range(num_pages):
                    # Add some randomness to page view duration (in minutes)
                    duration = random.randint(avg_duration - 1, avg_duration + 1)
                    
                    # Generate timestamp for this page view
                    timestamp = session_start + datetime.timedelta(
                        minutes=page * duration,
                        seconds=random.randint(0, 59)
                    )
                    
                    # Create page view record
                    page_views.append({
                        "studentId": student["id"],
                        "textbookId": textbook["id"],
                        "courseId": comp["courseId"],
                        "pageNumber": random.randint(1, textbook["pages"]),
                        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "duration": duration
                    })
                    
                    # Create interaction record
                    interactions.append({
                        "studentId": student["id"],
                        "textbookId": textbook["id"],
                        "courseId": comp["courseId"],
                        "interactionType": random.choice(["read", "highlight", "note"]),
                        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "duration": duration
                    })
    
    return interactions, page_views

# =============================================================================
#                           EXPORT FUNCTIONS
# =============================================================================

def export_to_cypher(data, output_dir):
    """
    Export data to Cypher script files.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Export students
    with open(os.path.join(output_dir, "01_students.cypher"), "w") as f:
        for student in data["students"]:
            cypher = f"""
CREATE (s:Student {{
    id: "{student["id"]}",
    name: "{student["name"]}",
    enrollmentDate: date("{student["enrollmentDate"]}"),
    expectedGraduation: date("{student["expectedGraduation"]}"),
    learningStyle: "{student["learningStyle"]}",
    preferredCourseLoad: {student["preferredCourseLoad"]},
    preferredPace: "{student["preferredPace"]}",
    workHoursPerWeek: {student["workHoursPerWeek"]},
    financialAidStatus: "{student["financialAidStatus"]}",
    preferredInstructionMode: "{student["preferredInstructionMode"]}"
}});
"""
            f.write(cypher)
    
    # 2. Export faculty
    with open(os.path.join(output_dir, "02_faculty.cypher"), "w") as f:
        for faculty in data["faculty"]:
            teaching_styles_str = ", ".join([f'"{style}"' for style in faculty["teachingStyle"]])
            cypher = f"""
CREATE (f:Faculty {{
    id: "{faculty["id"]}",
    name: "{faculty["name"]}",
    department: "{faculty["department"]}",
    teachingStyle: [{teaching_styles_str}],
    avgRating: {faculty["avgRating"]}
}});
"""
            f.write(cypher)
    
    # 3. Export terms
    with open(os.path.join(output_dir, "03_terms.cypher"), "w") as f:
        for term in data["terms"]:
            cypher = f"""
CREATE (t:Term {{
    id: "{term["id"]}",
    name: "{term["name"]}",
    startDate: date("{term["startDate"]}"),
    endDate: date("{term["endDate"]}"),
    type: "{term["type"]}"
}});
"""
            f.write(cypher)
            
    # 4. Export courses
    with open(os.path.join(output_dir, "04_courses.cypher"), "w") as f:
        for course in data["courses"]:
            term_avail_str = ", ".join([f'"{term}"' for term in course["termAvailability"]])
            instruction_modes_str = ", ".join([f'"{mode}"' for mode in course["instructionModes"]])
            tags_str = ", ".join([f'"{tag}"' for tag in course.get("tags", [])])
            
            # Handle optional fields
            visual_success = f', visualLearnerSuccess: {course.get("visualLearnerSuccess", 0.8)}' if "visualLearnerSuccess" in course else ""
            auditory_success = f', auditoryLearnerSuccess: {course.get("auditoryLearnerSuccess", 0.8)}' if "auditoryLearnerSuccess" in course else ""
            kinesthetic_success = f', kinestheticLearnerSuccess: {course.get("kinestheticLearnerSuccess", 0.8)}' if "kinestheticLearnerSuccess" in course else ""
            reading_success = f', readingLearnerSuccess: {course.get("readingLearnerSuccess", 0.8)}' if "readingLearnerSuccess" in course else ""
            
            cypher = f"""
CREATE (c:Course {{
    id: "{course["id"]}",
    name: "{course["name"]}",
    department: "{course["department"]}",
    credits: {course["credits"]},
    level: {course["level"]},
    avgDifficulty: {course["avgDifficulty"]},
    avgTimeCommitment: {course["avgTimeCommitment"]},
    termAvailability: [{term_avail_str}],
    instructionModes: [{instruction_modes_str}],
    tags: [{tags_str}]{visual_success}{auditory_success}{kinesthetic_success}{reading_success}
}});
"""
            f.write(cypher)
            
    # 5. Export degrees
    with open(os.path.join(output_dir, "05_degrees.cypher"), "w") as f:
        for degree in data["degrees"]:
            cypher = f"""
CREATE (d:Degree {{
    id: "{degree["id"]}",
    name: "{degree["name"]}",
    department: "{degree["department"]}",
    type: "{degree["type"]}",
    totalCreditsRequired: {degree["totalCreditsRequired"]},
    coreCreditsRequired: {degree["coreCreditsRequired"]},
    electiveCreditsRequired: {degree["electiveCreditsRequired"]}
}});
"""
            f.write(cypher)
            
    # 6. Export requirement groups
    with open(os.path.join(output_dir, "06_requirement_groups.cypher"), "w") as f:
        for req in data["requirement_groups"]:
            cypher = f"""
CREATE (r:RequirementGroup {{
    id: "{req["id"]}",
    name: "{req["name"]}",
    description: "{req["description"]}",
    minimumCourses: {req["minimumCourses"]},
    minimumCredits: {req["minimumCredits"]}
}});
"""
            f.write(cypher)
    
    # 7. Export relationships: Course Prerequisites
    with open(os.path.join(output_dir, "07_course_prerequisites.cypher"), "w") as f:
        for prereq in data["prerequisites"]:
            min_grade = f', minGrade: "{prereq["minGrade"]}"' if prereq["minGrade"] else ""
            cypher = f"""
MATCH (source:Course {{id: "{prereq["source"]}"}}), (target:Course {{id: "{prereq["target"]}"}})
CREATE (source)-[:PREREQUISITE_FOR {{strength: "{prereq["strength"]}"{min_grade}}}]->(target);
"""
            f.write(cypher)
            
    # 8. Export relationships: LEADS_TO
    with open(os.path.join(output_dir, "08_leads_to.cypher"), "w") as f:
        for lead in data["leads_to"]:
            cypher = f"""
MATCH (source:Course {{id: "{lead["source"]}"}}), (target:Course {{id: "{lead["target"]}"}})
CREATE (source)-[:LEADS_TO {{commonality: {lead["commonality"]}, successCorrelation: {lead["successCorrelation"]}}}]->(target);
"""
            f.write(cypher)
            
    # 9. Export relationships: Course similarity
    with open(os.path.join(output_dir, "09_course_similarity.cypher"), "w") as f:
        # Content similarity
        for sim in data["similarity_content"]:
            cypher = f"""
MATCH (source:Course {{id: "{sim["source"]}"}}), (target:Course {{id: "{sim["target"]}"}})
CREATE (source)-[:SIMILAR_CONTENT {{similarity: {sim["similarity"]}}}]->(target);
"""
            f.write(cypher)
            
        # Difficulty similarity
        for sim in data["similarity_difficulty"]:
            cypher = f"""
MATCH (source:Course {{id: "{sim["source"]}"}}), (target:Course {{id: "{sim["target"]}"}})
CREATE (source)-[:SIMILAR_DIFFICULTY {{similarity: {sim["similarity"]}}}]->(target);
"""
            f.write(cypher)
    
    # 10. Export relationships: Student-Degree
    with open(os.path.join(output_dir, "10_student_degree.cypher"), "w") as f:
        for rel in data["student_degree"]:
            cypher = f"""
MATCH (s:Student {{id: "{rel["studentId"]}"}}), (d:Degree {{id: "{rel["degreeId"]}"}})
CREATE (s)-[:PURSUING]->(d);
"""
            f.write(cypher)
            
    # 11. Export relationships: Faculty-Course
    with open(os.path.join(output_dir, "11_teaching.cypher"), "w") as f:
        for teach in data["teaching"]:
            terms_str = ", ".join([f'"{term}"' for term in teach["terms"]])
            cypher = f"""
MATCH (f:Faculty {{id: "{teach["facultyId"]}"}}), (c:Course {{id: "{teach["courseId"]}"}})
CREATE (f)-[:TEACHES {{terms: [{terms_str}]}}]->(c);
"""
            f.write(cypher)
            
    # 12. Export relationships: Student-Course (Completed)
    with open(os.path.join(output_dir, "12_completed_courses.cypher"), "w") as f:
        for comp in data["completed_courses"]:
            enjoyment = "true" if comp["enjoyment"] else "false"
            cypher = f"""
MATCH (s:Student {{id: "{comp["studentId"]}"}}), (c:Course {{id: "{comp["courseId"]}"}})
CREATE (s)-[:COMPLETED {{
    term: "{comp["term"]}",
    grade: "{comp["grade"]}",
    difficulty: {comp["difficulty"]},
    timeSpent: {comp["timeSpent"]},
    instructionMode: "{comp["instructionMode"]}",
    enjoyment: {enjoyment}
}}]->(c);
"""
            f.write(cypher)
            
    # 13. Export relationships: Student-Course (Enrolled)
    with open(os.path.join(output_dir, "13_enrolled_courses.cypher"), "w") as f:
        for enroll in data["enrolled_courses"]:
            cypher = f"""
MATCH (s:Student {{id: "{enroll["studentId"]}"}}), (c:Course {{id: "{enroll["courseId"]}"}})
CREATE (s)-[:ENROLLED_IN]->(c);
"""
            f.write(cypher)
            
    # 14. Export relationships: Student similarity
    with open(os.path.join(output_dir, "14_student_similarity.cypher"), "w") as f:
        # Learning style similarity
        for sim in data["learning_style_similarity"]:
            cypher = f"""
MATCH (source:Student {{id: "{sim["sourceId"]}"}}), (target:Student {{id: "{sim["targetId"]}"}})
CREATE (source)-[:SIMILAR_LEARNING_STYLE {{similarity: {sim["similarity"]}}}]->(target);
"""
            f.write(cypher)
            
        # Performance similarity
        for sim in data["performance_similarity"]:
            courses_str = ", ".join([f'"{c}"' for c in sim["courses"]])
            cypher = f"""
MATCH (source:Student {{id: "{sim["sourceId"]}"}}), (target:Student {{id: "{sim["targetId"]}"}})
CREATE (source)-[:SIMILAR_PERFORMANCE {{similarity: {sim["similarity"]}, courses: [{courses_str}]}}]->(target);
"""
            f.write(cypher)
            
    # 15. Export relationships: Requirement Group - Degree
    with open(os.path.join(output_dir, "15_requirement_degree.cypher"), "w") as f:
        for req in data["requirement_groups"]:
            cypher = f"""
MATCH (r:RequirementGroup {{id: "{req["id"]}"}}), (d:Degree {{id: "{req["degreeId"]}"}})
CREATE (r)-[:PART_OF]->(d);
"""
            f.write(cypher)
            
    # 16. Export relationships: Course - Requirement Group
    with open(os.path.join(output_dir, "16_course_requirement.cypher"), "w") as f:
        for req in data["requirement_groups"]:
            for course_id in req["courses"]:
                cypher = f"""
MATCH (c:Course {{id: "{course_id}"}}), (r:RequirementGroup {{id: "{req["id"]}"}})
CREATE (c)-[:FULFILLS]->(r);
"""
                f.write(cypher)
                
    # 17. Export relationships: Course - Term
    with open(os.path.join(output_dir, "17_course_term.cypher"), "w") as f:
        for course in data["courses"]:
            for term_type in course["termAvailability"]:
                # For each matching term
                for term in data["terms"]:
                    if term["type"] == term_type:
                        cypher = f"""
MATCH (c:Course {{id: "{course["id"]}"}}), (t:Term {{id: "{term["id"]}"}})
CREATE (c)-[:OFFERED_IN]->(t);
"""
                        f.write(cypher)
                        
    # 18. Create indexes and constraints
    with open(os.path.join(output_dir, "00_indexes.cypher"), "w") as f:
        f.write("""
// Uniqueness constraints
CREATE CONSTRAINT FOR (s:Student) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT FOR (c:Course) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT FOR (d:Degree) REQUIRE d.id IS UNIQUE;
CREATE CONSTRAINT FOR (f:Faculty) REQUIRE f.id IS UNIQUE;
CREATE CONSTRAINT FOR (t:Term) REQUIRE t.id IS UNIQUE;
CREATE CONSTRAINT FOR (r:RequirementGroup) REQUIRE r.id IS UNIQUE;

// Indexes for common lookups
CREATE INDEX FOR (s:Student) ON (s.learningStyle);
CREATE INDEX FOR (c:Course) ON (c.department);
CREATE INDEX FOR (c:Course) ON (c.level);
CREATE INDEX FOR (d:Degree) ON (d.department);
CREATE INDEX FOR (d:Degree) ON (d.type);
CREATE INDEX FOR (t:Term) ON (t.type);
""")

def export_to_csv(data, output_dir):
    """
    Export data to CSV files for Neo4j Import.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Export students
    with open(os.path.join(output_dir, "students.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(Student)", "name", "enrollmentDate", "expectedGraduation", 
            "learningStyle", "preferredCourseLoad:int", "preferredPace", 
            "workHoursPerWeek:int", "financialAidStatus", "preferredInstructionMode"
        ])
        
        for student in data["students"]:
            writer.writerow([
                student["id"], 
                student["name"], 
                student["enrollmentDate"], 
                student["expectedGraduation"],
                student["learningStyle"], 
                student["preferredCourseLoad"], 
                student["preferredPace"],
                student["workHoursPerWeek"], 
                student["financialAidStatus"], 
                student["preferredInstructionMode"]
            ])
    
    # 2. Export faculty
    with open(os.path.join(output_dir, "faculty.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(Faculty)", "name", "department", "teachingStyle", "avgRating:float"
        ])
        
        for faculty in data["faculty"]:
            writer.writerow([
                faculty["id"], 
                faculty["name"], 
                faculty["department"], 
                ";".join(faculty["teachingStyle"]), 
                faculty["avgRating"]
            ])
    
    # 3. Export terms
    with open(os.path.join(output_dir, "terms.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(Term)", "name", "startDate", "endDate", "type"
        ])
        
        for term in data["terms"]:
            writer.writerow([
                term["id"], 
                term["name"], 
                term["startDate"], 
                term["endDate"], 
                term["type"]
            ])
            
    # 4. Export courses
    with open(os.path.join(output_dir, "courses.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(Course)", "name", "department", "credits:int", "level:int",
            "avgDifficulty:float", "avgTimeCommitment:int", "termAvailability",
            "instructionModes", "tags", "visualLearnerSuccess:float", "auditoryLearnerSuccess:float",
            "kinestheticLearnerSuccess:float", "readingLearnerSuccess:float"
        ])
        
        for course in data["courses"]:
            writer.writerow([
                course["id"], 
                course["name"], 
                course["department"], 
                course["credits"],
                course["level"], 
                course["avgDifficulty"], 
                course["avgTimeCommitment"],
                ";".join(course["termAvailability"]), 
                ";".join(course["instructionModes"]), 
                ";".join(course.get("tags", [])),
                course.get("visualLearnerSuccess", ""),
                course.get("auditoryLearnerSuccess", ""),
                course.get("kinestheticLearnerSuccess", ""),
                course.get("readingLearnerSuccess", "")
            ])
            
    # 5. Export degrees
    with open(os.path.join(output_dir, "degrees.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(Degree)", "name", "department", "type", "totalCreditsRequired:int",
            "coreCreditsRequired:int", "electiveCreditsRequired:int"
        ])
        
        for degree in data["degrees"]:
            writer.writerow([
                degree["id"], 
                degree["name"], 
                degree["department"], 
                degree["type"],
                degree["totalCreditsRequired"], 
                degree["coreCreditsRequired"], 
                degree["electiveCreditsRequired"]
            ])
            
    # 6. Export requirement groups
    with open(os.path.join(output_dir, "requirement_groups.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(RequirementGroup)", "name", "description", "minimumCourses:int", "minimumCredits:int"
        ])
        
        for req in data["requirement_groups"]:
            writer.writerow([
                req["id"], 
                req["name"], 
                req["description"], 
                req["minimumCourses"],
                req["minimumCredits"]
            ])
    
    # 7. Export relationship: Prerequisites
    with open(os.path.join(output_dir, "prerequisites.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(Course)", ":TYPE", "strength", "minGrade"
        ])
        
        for prereq in data["prerequisites"]:
            writer.writerow([
                prereq["source"],
                prereq["target"],
                "PREREQUISITE_FOR",
                prereq["strength"],
                prereq.get("minGrade", "")
            ])
            
    # 8. Export relationship: LEADS_TO
    with open(os.path.join(output_dir, "leads_to.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(Course)", ":TYPE", "commonality:float", "successCorrelation:float"
        ])
        
        for lead in data["leads_to"]:
            writer.writerow([
                lead["source"],
                lead["target"],
                "LEADS_TO",
                lead["commonality"],
                lead["successCorrelation"]
            ])
            
    # 9. Export relationship: Course similarity
    with open(os.path.join(output_dir, "course_similarity_content.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(Course)", ":TYPE", "similarity:float"
        ])
        
        for sim in data["similarity_content"]:
            writer.writerow([
                sim["source"],
                sim["target"],
                "SIMILAR_CONTENT",
                sim["similarity"]
            ])
            
    with open(os.path.join(output_dir, "course_similarity_difficulty.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(Course)", ":TYPE", "similarity:float"
        ])
        
        for sim in data["similarity_difficulty"]:
            writer.writerow([
                sim["source"],
                sim["target"],
                "SIMILAR_DIFFICULTY",
                sim["similarity"]
            ])
    
    # 10. Export relationship: Student-Degree
    with open(os.path.join(output_dir, "student_degree.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Degree)", ":TYPE"
        ])
        
        for rel in data["student_degree"]:
            writer.writerow([
                rel["studentId"],
                rel["degreeId"],
                "PURSUING"
            ])
            
    # 11. Export relationship: Faculty-Course
    with open(os.path.join(output_dir, "teaching.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Faculty)", ":END_ID(Course)", ":TYPE", "terms"
        ])
        
        for teach in data["teaching"]:
            writer.writerow([
                teach["facultyId"],
                teach["courseId"],
                "TEACHES",
                ";".join(teach["terms"])
            ])
            
    # 12. Export relationship: Student-Course (Completed)
    with open(os.path.join(output_dir, "completed_courses.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Course)", ":TYPE", "term", "grade",
            "difficulty:int", "timeSpent:int", "instructionMode", "enjoyment:boolean"
        ])
        
        for comp in data["completed_courses"]:
            writer.writerow([
                comp["studentId"],
                comp["courseId"],
                "COMPLETED",
                comp["term"],
                comp["grade"],
                comp["difficulty"],
                comp["timeSpent"],
                comp["instructionMode"],
                "true" if comp["enjoyment"] else "false"
            ])
            
    # 13. Export relationship: Student-Course (Enrolled)
    with open(os.path.join(output_dir, "enrolled_courses.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Course)", ":TYPE"
        ])
        
        for enroll in data["enrolled_courses"]:
            writer.writerow([
                enroll["studentId"],
                enroll["courseId"],
                "ENROLLED_IN"
            ])
            
    # 14. Export relationship: Student similarity
    with open(os.path.join(output_dir, "learning_style_similarity.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Student)", ":TYPE", "similarity:float"
        ])
        
        for sim in data["learning_style_similarity"]:
            writer.writerow([
                sim["sourceId"],
                sim["targetId"],
                "SIMILAR_LEARNING_STYLE",
                sim["similarity"]
            ])
            
    with open(os.path.join(output_dir, "performance_similarity.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Student)", ":TYPE", "similarity:float", "courses"
        ])
        
        for sim in data["performance_similarity"]:
            writer.writerow([
                sim["sourceId"],
                sim["targetId"],
                "SIMILAR_PERFORMANCE",
                sim["similarity"],
                ";".join(sim["courses"])
            ])
            
    # 15. Export relationship: Requirement Group - Degree
    with open(os.path.join(output_dir, "requirement_degree.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(RequirementGroup)", ":END_ID(Degree)", ":TYPE"
        ])
        
        for req in data["requirement_groups"]:
            writer.writerow([
                req["id"],
                req["degreeId"],
                "PART_OF"
            ])
            
    # 16. Export relationship: Course - Requirement Group
    with open(os.path.join(output_dir, "course_requirement.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(RequirementGroup)", ":TYPE"
        ])
        
        for req in data["requirement_groups"]:
            for course_id in req["courses"]:
                writer.writerow([
                    course_id,
                    req["id"],
                    "FULFILLS"
                ])
                
    # 17. Export relationship: Course - Term
    with open(os.path.join(output_dir, "course_term.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(Term)", ":TYPE"
        ])
        
        for course in data["courses"]:
            for term_type in course["termAvailability"]:
                # For each matching term
                for term in data["terms"]:
                    if term["type"] == term_type:
                        writer.writerow([
                            course["id"],
                            term["id"],
                            "OFFERED_IN"
                        ])
    
    # Export textbooks
    with open(os.path.join(output_dir, "textbooks.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "id:ID(Textbook)", "name", "publisher", "price:float", "pages:int",
            "edition:int", "publicationYear:int", "isbn", "category"
        ])
        
        for textbook in data["textbooks"]:
            writer.writerow([
                textbook["id"],
                textbook["name"],
                textbook["publisher"],
                textbook["price"],
                textbook["pages"],
                textbook["edition"],
                textbook["publicationYear"],
                textbook["isbn"],
                textbook["category"]
            ])
    
    # Export course-textbook relationships
    with open(os.path.join(output_dir, "course_textbooks.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Course)", ":END_ID(Textbook)", ":TYPE",
            "isRequired:boolean", "recommendedOrder:int"
        ])
        
        for rel in data["course_textbooks"]:
            writer.writerow([
                rel["courseId"],
                rel["textbookId"],
                "REQUIRES" if rel["isRequired"] else "RECOMMENDS",
                rel["isRequired"],
                rel["recommendedOrder"]
            ])
    
    # Export textbook page views
    with open(os.path.join(output_dir, "page_views.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Textbook)", ":TYPE",
            "courseId", "pageNumber:int", "timestamp", "duration:int"
        ])
        
        for view in data["page_views"]:
            writer.writerow([
                view["studentId"],
                view["textbookId"],
                "VIEWED_PAGE",
                view["courseId"],
                view["pageNumber"],
                view["timestamp"],
                view["duration"]
            ])
    
    # Export textbook interactions
    with open(os.path.join(output_dir, "textbook_interactions.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            ":START_ID(Student)", ":END_ID(Textbook)", ":TYPE",
            "courseId", "interactionType", "timestamp", "duration:int"
        ])
        
        for interaction in data["textbook_interactions"]:
            writer.writerow([
                interaction["studentId"],
                interaction["textbookId"],
                "INTERACTED_WITH",
                interaction["courseId"],
                interaction["interactionType"],
                interaction["timestamp"],
                interaction["duration"]
            ])

def generate_neo4j_import_script(output_dir):
    """
    Generate a shell script to import the CSV files into Neo4j.
    The script is idempotent - it will destroy and recreate the target database.
    """
    script_path = os.path.join(output_dir, "import_to_neo4j.sh")
    
    with open(script_path, "w") as f:
        f.write("""#!/bin/bash
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
"$NEO4J_HOME/bin/neo4j-admin" database import full \\
  --nodes="Student=$IMPORT_DIR/students.csv" \\
  --nodes="Faculty=$IMPORT_DIR/faculty.csv" \\
  --nodes="Course=$IMPORT_DIR/courses.csv" \\
  --nodes="Degree=$IMPORT_DIR/degrees.csv" \\
  --nodes="Term=$IMPORT_DIR/terms.csv" \\
  --nodes="RequirementGroup=$IMPORT_DIR/requirement_groups.csv" \\
  --nodes="Textbook=$IMPORT_DIR/textbooks.csv" \\
  --relationships="PREREQUISITE_FOR=$IMPORT_DIR/prerequisites.csv" \\
  --relationships="LEADS_TO=$IMPORT_DIR/leads_to.csv" \\
  --relationships="SIMILAR_CONTENT=$IMPORT_DIR/course_similarity_content.csv" \\
  --relationships="SIMILAR_DIFFICULTY=$IMPORT_DIR/course_similarity_difficulty.csv" \\
  --relationships="PURSUING=$IMPORT_DIR/student_degree.csv" \\
  --relationships="TEACHES=$IMPORT_DIR/teaching.csv" \\
  --relationships="COMPLETED=$IMPORT_DIR/completed_courses.csv" \\
  --relationships="ENROLLED_IN=$IMPORT_DIR/enrolled_courses.csv" \\
  --relationships="SIMILAR_LEARNING_STYLE=$IMPORT_DIR/learning_style_similarity.csv" \\
  --relationships="SIMILAR_PERFORMANCE=$IMPORT_DIR/performance_similarity.csv" \\
  --relationships="PART_OF=$IMPORT_DIR/requirement_degree.csv" \\
  --relationships="FULFILLS=$IMPORT_DIR/course_requirement.csv" \\
  --relationships="OFFERED_IN=$IMPORT_DIR/course_term.csv" \\
  --relationships="REQUIRES,RECOMMENDS=$IMPORT_DIR/course_textbooks.csv" \\
  --relationships="VIEWED_PAGE=$IMPORT_DIR/page_views.csv" \\
  --relationships="INTERACTED_WITH=$IMPORT_DIR/textbook_interactions.csv" \\
  --delimiter="," \\
  --array-delimiter=";" \\
  --ignore-empty-strings=true \\
  --ignore-extra-columns=true \\
  --skip-bad-relationships=true \\
  --skip-duplicate-nodes=true \\
  --high-parallel-io=on \\
  --normalize-types=true \\
  --overwrite-destination=true \\
  "$DB_NAME"

if [ $? -eq 0 ]; then
    echo "Import completed successfully!"
    echo "To use the database, edit neo4j.conf to set dbms.default_database=$DB_NAME"
    echo "Then restart Neo4j."
else
    echo "Import failed. Check the error messages above for details."
    exit 1
fi
""")
    
    # Make the script executable
    os.chmod(script_path, 0o755)

def create_readme(output_dir):
    """
    Create a README file with usage instructions.
    """
    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write("""# UMBC Neo4j Academic Graph Database

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
""")

def create_neo4j_browser_guide(output_dir):
    """
    Create a Neo4j Browser guide with sample queries.
    """
    with open(os.path.join(output_dir, "umbc_guide.html"), "w") as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>UMBC Neo4j Academic Graph Browser Guide</title>
</head>
<body>
  <article class="guide" data-title="UMBC Academic Pathways Guide">
    <carousel class="deck container-fluid">
      <slide class="row-fluid">
        <div class="col-sm-12">
          <h3>UMBC Academic Graph - Personalized Degree Pathways</h3>
          <p>This guide demonstrates key queries for exploring and analyzing the UMBC academic graph database.</p>
          <p>The data model represents students, courses, faculty, degrees, and their interrelationships to power personalized degree pathway planning.</p>
          <h4>Data Overview</h4>
          <figure>
            <pre class="code runnable">
CALL db.schema.visualization
            </pre>
          </figure>
        </div>
      </slide>
      
      <slide class="row-fluid">
        <div class="col-sm-12">
          <h3>Find Optimal Next Courses for a Student</h3>
          <p>This query finds the best next courses for a specific student based on their learning style, prerequisites, and term availability.</p>
          <figure>
            <pre class="code runnable">
// Find optimal next courses based on learning style and prerequisites
MATCH (student:Student)-[:PURSUING]->(degree:Degree)
WHERE student.id = 'AB12345' // Replace with a real campus ID from the dataset
MATCH (term:Term {id: 'Fall2023'}) // Update with appropriate term
MATCH (course:Course)-[:OFFERED_IN]->(term)
MATCH (course)-[:FULFILLS]->(:RequirementGroup)-[:PART_OF]->(degree)

// Ensure prerequisites are met
WHERE NOT EXISTS {
  MATCH (prereq:Course)-[:PREREQUISITE_FOR]->(course)
  WHERE NOT (student)-[:COMPLETED]->(prereq)
}

// Student hasn't already completed the course
AND NOT (student)-[:COMPLETED]->(course)

// Find similar students and their experiences with these courses
OPTIONAL MATCH (student)-[sim:SIMILAR_LEARNING_STYLE]->(similar:Student)-[comp:COMPLETED]->(course)
WHERE sim.similarity > 0.7

WITH student, course, term, degree,
     CASE WHEN COUNT(comp) > 0 
          THEN AVG(comp.difficulty) 
          ELSE course.avgDifficulty END AS predictedDifficulty,
     COUNT(comp) AS similarStudentsCount

// Check how many future courses this would unlock
OPTIONAL MATCH (course)-[:PREREQUISITE_FOR]->(futureCourse)
WHERE (futureCourse)-[:FULFILLS]->(:RequirementGroup)-[:PART_OF]->(degree)

RETURN course.id AS courseId,
       course.name AS courseName,
       course.credits AS credits,
       predictedDifficulty,
       COUNT(futureCourse) AS unlockedCourses,
       similarStudentsCount,
       course.instructionModes AS availableModes
ORDER BY predictedDifficulty ASC, unlockedCourses DESC, credits DESC
LIMIT 5
            </pre>
          </figure>
        </div>
      </slide>
      
      <slide class="row-fluid">
        <div class="col-sm-12">
          <h3>Find Balanced Course Load</h3>
          <p>This query helps students find a balanced course load with appropriate difficulty distribution.</p>
          <figure>
            <pre class="code runnable">
// Find balanced course combinations for a student
MATCH (student:Student {id: 'AB12345'})-[:PURSUING]->(degree:Degree)
MATCH (term:Term {id: 'Fall2023'})

// Find available courses for the upcoming term
MATCH (course:Course)-[:OFFERED_IN]->(term)
WHERE (course)-[:FULFILLS]->(:RequirementGroup)-[:PART_OF]->(degree)
  AND NOT (student)-[:COMPLETED]->(course)
  AND NOT EXISTS {
    MATCH (prereq:Course)-[:PREREQUISITE_FOR]->(course)
    WHERE NOT (student)-[:COMPLETED]->(prereq)
  }

// Predict personalized difficulty
OPTIONAL MATCH (student)-[:SIMILAR_LEARNING_STYLE]->(similar:Student)-[comp:COMPLETED]->(course)
WITH student, course, term, degree,
     CASE WHEN COUNT(comp) > 0 
          THEN AVG(comp.difficulty) 
          ELSE course.avgDifficulty END AS predictedDifficulty,
     course.credits AS credits,
     course.id AS courseId,
     course.name AS courseName

// Return the courses in a way they can be manually combined
RETURN courseId, 
       courseName, 
       credits, 
       predictedDifficulty,
       CASE 
         WHEN predictedDifficulty <= 2 THEN 'Easy'
         WHEN predictedDifficulty <= 3.5 THEN 'Moderate'
         ELSE 'Challenging'
       END AS difficultyCategory
ORDER BY predictedDifficulty DESC
            </pre>
          </figure>
        </div>
      </slide>
      
      <slide class="row-fluid">
        <div class="col-sm-12">
          <h3>Visualize Course Prerequisite Structure</h3>
          <p>This query generates a visualization of course prerequisites to help understand dependencies.</p>
          <figure>
            <pre class="code runnable">
// Visualize prerequisite structure for courses in a degree program
MATCH (degree:Degree {id: 'BS-ComputerScience-1'})  // Update with an actual degree ID
MATCH (course:Course)-[:FULFILLS]->(:RequirementGroup)-[:PART_OF]->(degree)
OPTIONAL MATCH prereqPath = (course)<-[:PREREQUISITE_FOR*1..3]-(prereq:Course)
RETURN course, prereqPath, prereq
LIMIT 50 // Limit to prevent overwhelming visualization
            </pre>
          </figure>
        </div>
      </slide>
      
      <slide class="row-fluid">
        <div class="col-sm-12">
          <h3>Find Students with Similar Learning Styles</h3>
          <p>This query helps identify students with similar learning preferences who might benefit from similar course pathways.</p>
          <figure>
            <pre class="code runnable">
// Find students with similar learning styles and their course histories
MATCH (student:Student {id: 'AB12345'})  // Update with actual student ID
MATCH (student)-[sim:SIMILAR_LEARNING_STYLE]->(similar:Student)
WHERE sim.similarity > 0.8
OPTIONAL MATCH (similar)-[comp:COMPLETED]->(course:Course)
WHERE comp.grade IN ['A', 'A-', 'B+']
WITH similar, 
     COUNT(DISTINCT course) AS successfulCourseCount,
     COLLECT(DISTINCT {course: course.name, grade: comp.grade}) AS coursesTaken
RETURN similar.id AS similarStudentId,
       similar.learningStyle,
       successfulCourseCount,
       similar.preferredCourseLoad,
       similar.preferredPace,
       coursesTaken
ORDER BY successfulCourseCount DESC
LIMIT 10
            </pre>
          </figure>
        </div>
      </slide>
      
      <slide class="row-fluid">
        <div class="col-sm-12">
          <h3>Analyze Course Centrality</h3>
          <p>Use Graph Data Science to identify key courses in the curriculum based on their centrality in the prerequisite network.</p>
          <figure>
            <pre class="code runnable">
// Create a graph projection
CALL gds.graph.project(
  'prereqGraph',
  ['Course'],
  {
    PREREQ: {
      type: 'PREREQUISITE_FOR',
      orientation: 'REVERSE'
    }
  }
)

// Run PageRank to find central courses
CALL gds.pageRank.stream('prereqGraph')
YIELD nodeId, score
WITH gds.util.asNode(nodeId) AS course, score
WHERE course.department = 'Computer Science'  // Change to analyze a specific department
RETURN course.id, course.name, score AS centralityScore
ORDER BY centralityScore DESC
LIMIT 20

// Drop the graph projection when done
// CALL gds.graph.drop('prereqGraph')
            </pre>
          </figure>
        </div>
      </slide>
    </carousel>
  </article>
</body>
</html>
""")

# =============================================================================
#                           MAIN FUNCTION
# =============================================================================

def main():
    """
    Main function to run the data generation process.
    """
    print("UMBC Neo4j Graph Database Generator")
    print("===================================")
    print(f"Generating synthetic data with:")
    print(f"- {NUM_STUDENTS} students")
    print(f"- {NUM_COURSES} courses")
    print(f"- {NUM_FACULTY} faculty")
    print(f"- {NUM_DEGREES} degree programs")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate the data
    print("\nGenerating terms...")
    terms = generate_terms()
    
    print("Generating students...")
    students = generate_students()
    
    print("Generating faculty...")
    faculty, faculty_by_dept = generate_faculty()
    
    print("Generating courses...")
    courses, dept_courses = generate_courses(faculty_by_dept)
    
    print("Generating textbooks...")
    textbooks, course_textbooks = generate_textbooks(courses)
    
    print("Generating degrees and requirement groups...")
    degrees, requirement_groups = generate_degrees(dept_courses)
    
    print("Generating prerequisites...")
    prerequisites = generate_prerequisites(courses)
    
    print("Generating leads_to relationships...")
    leads_to = generate_leads_to_relationships(courses, prerequisites)
    
    print("Generating course similarity...")
    similarity_content, similarity_difficulty = generate_course_similarity(courses)
    
    print("Generating student-degree relationships...")
    student_degree = generate_student_degree_relationships(students, degrees)
    
    print("Generating teaching relationships...")
    teaching = generate_teaching_relationships(faculty_by_dept, courses)
    
    print("Generating student course history...")
    completed_courses, enrolled_courses = generate_student_course_history(students, courses, terms, prerequisites)
    
    print("Generating textbook interactions...")
    textbook_interactions, page_views = generate_textbook_interactions(
        students, courses, textbooks, course_textbooks, terms, completed_courses
    )
    
    print("Generating student similarity...")
    learning_style_similarity, performance_similarity = generate_student_similarity(students, completed_courses)
    
    # Combine all data
    data = {
        "students": students,
        "faculty": faculty,
        "courses": courses,
        "textbooks": textbooks,
        "course_textbooks": course_textbooks,
        "textbook_interactions": textbook_interactions,
        "page_views": page_views,
        "degrees": degrees,
        "terms": terms,
        "requirement_groups": requirement_groups,
        "prerequisites": prerequisites,
        "leads_to": leads_to,
        "similarity_content": similarity_content,
        "similarity_difficulty": similarity_difficulty,
        "student_degree": student_degree,
        "teaching": teaching,
        "completed_courses": completed_courses,
        "enrolled_courses": enrolled_courses,
        "learning_style_similarity": learning_style_similarity,
        "performance_similarity": performance_similarity
    }
    
    # Export the data
    print("\nExporting data...")
    
    cypher_dir = os.path.join(OUTPUT_DIR, "cypher")
    csv_dir = os.path.join(OUTPUT_DIR, "csv")
    
    print("Exporting Cypher scripts...")
    export_to_cypher(data, cypher_dir)
    
    print("Exporting CSV files...")
    export_to_csv(data, csv_dir)
    
    print("Generating Neo4j import script...")
    generate_neo4j_import_script(csv_dir)
    
    print("Creating README...")
    create_readme(OUTPUT_DIR)
    
    print("Creating Neo4j Browser guide...")
    create_neo4j_browser_guide(OUTPUT_DIR)
    
    # Summary statistics
    print("\nGenerated Data Summary:")
    print(f"- {len(students)} students")
    print(f"- {len(courses)} courses")
    print(f"- {len(faculty)} faculty")
    print(f"- {len(textbooks)} textbooks")
    print(f"- {len(textbook_interactions)} textbook interactions")
    print(f"- {len(page_views)} page views")
    print(f"- {len(degrees)} degree programs")
    print(f"- {len(requirement_groups)} requirement groups")
    print(f"- {len(terms)} academic terms")
    print(f"- {len(prerequisites)} prerequisite relationships")
    print(f"- {len(completed_courses)} completed course records")
    print(f"- {len(enrolled_courses)} enrolled course records")
    
    print(f"\nOutput files written to {OUTPUT_DIR}")
    print("- Cypher scripts: ./cypher/")
    print("- CSV files: ./csv/")
    print("- Import script: ./csv/import_to_neo4j.sh")
    print("- README: ./README.md")
    print("- Browser Guide: ./umbc_guide.html")
    
    print("\nDone!")

if __name__ == "__main__":
    main()

#%%
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import random
from bson import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

uri = 'mongodb+srv://delightogwor:Desax123@altschool.tpn4wc7.mongodb.net/?retryWrites=true&w=majority'

# Connect to MongoDB Atlas
client = MongoClient(uri)

# Use or create the database
db = client['eduhub_db']

#%%
# Only create collection if it doesn't exist

db.create_collection(
    'users',
     validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['userId', 'email', 'firstName', 'lastName', 'role'],
            'properties': {
                'userId': {'bsonType': 'string'},
                'email': {'bsonType': 'string'},
                'firstName': {'bsonType': 'string'},
                'lastName': {'bsonType': 'string'},
                'role': {'enum': ['student', 'instructor']},
                'dateJoined': {'bsonType': 'date'},
                'profile': {
                    'bsonType': 'object',
                    'properties': {
                        'bio': {'bsonType': 'string'},
                        'avatar': {'bsonType': 'string'},
                        'skills': {'bsonType': 'array', 
                                   'items': {'bsonType': 'string'}}
                    }
                },
                'isActive': {'bsonType': 'bool'}
            }
        }
    },
    )
db.users.create_index("userId", unique=True)
db.users.create_index("email", unique=True)  # if not done already
print("Connected and collection created.")

# %%
sample_users = [
    # --- Students ---
    {
        "userId": "U001", "email": "alice@example.com", "firstName": "Alice", "lastName": "Johnson",
        "role": "student", "dateJoined": datetime(2024, 7, 12),
        "profile": {"bio": "Aspiring data scientist.", "avatar": "https://example.com/avatar1.jpg", "skills": ["python", "data analysis"]},
        "isActive": True
    },
    {
        "userId": "U002", "email": "bob@example.com", "firstName": "Bob", "lastName": "Smith",
        "role": "student", "dateJoined": datetime(2024, 8, 3),
        "profile": {"bio": "Front-end enthusiast.", "avatar": "https://example.com/avatar2.jpg", "skills": ["html", "css", "javascript"]},
        "isActive": True
    },
    {
        "userId": "U003", "email": "carla@example.com", "firstName": "Carla", "lastName": "Lee",
        "role": "student", "dateJoined": datetime(2024, 6, 25),
        "profile": {"bio": "Learning backend systems.", "avatar": "https://example.com/avatar3.jpg", "skills": ["java", "spring boot"]},
        "isActive": True
    },
    {
        "userId": "U004", "email": "daniel@example.com", "firstName": "Daniel", "lastName": "Miller",
        "role": "student", "dateJoined": datetime(2024, 9, 1),
        "profile": {"bio": "Beginner in web dev.", "avatar": "https://example.com/avatar4.jpg", "skills": ["html", "css"]},
        "isActive": True
    },
    {
        "userId": "U005", "email": "emily@example.com", "firstName": "Emily", "lastName": "Wright",
        "role": "student", "dateJoined": datetime(2024, 9, 10),
        "profile": {"bio": "UI/UX learner.", "avatar": "https://example.com/avatar5.jpg", "skills": ["figma", "ux research"]},
        "isActive": True
    },
    {
        "userId": "U006", "email": "frank@example.com", "firstName": "Frank", "lastName": "Lopez",
        "role": "student", "dateJoined": datetime(2024, 10, 2),
        "profile": {"bio": "Fullstack dev in training.", "avatar": "https://example.com/avatar6.jpg", "skills": ["node.js", "react"]},
        "isActive": False
    },
    {
        "userId": "U007", "email": "grace@example.com", "firstName": "Grace", "lastName": "Patel",
        "role": "student", "dateJoined": datetime(2024, 11, 5),
        "profile": {"bio": "Cloud enthusiast.", "avatar": "https://example.com/avatar7.jpg", "skills": ["aws", "terraform"]},
        "isActive": True
    },
    {
        "userId": "U008", "email": "hank@example.com", "firstName": "Hank", "lastName": "Nguyen",
        "role": "student", "dateJoined": datetime(2024, 11, 15),
        "profile": {"bio": "Exploring DevOps.", "avatar": "https://example.com/avatar8.jpg", "skills": ["linux", "docker"]},
        "isActive": True
    },
    {
        "userId": "U009", "email": "irene@example.com", "firstName": "Irene", "lastName": "Choi",
        "role": "student", "dateJoined": datetime(2024, 12, 1),
        "profile": {"bio": "Love clean code.", "avatar": "https://example.com/avatar9.jpg", "skills": ["clean architecture", "oop"]},
        "isActive": False
    },
    {
        "userId": "U010", "email": "jason@example.com", "firstName": "Jason", "lastName": "Adams",
        "role": "student", "dateJoined": datetime(2024, 12, 12),
        "profile": {"bio": "Cybersecurity beginner.", "avatar": "https://example.com/avatar10.jpg", "skills": ["networking", "linux"]},
        "isActive": True
    },

    # --- Instructors ---
    {
        "userId": "U011", "email": "karen@example.com", "firstName": "Karen", "lastName": "Zhang",
        "role": "instructor", "dateJoined": datetime(2023, 6, 15),
        "profile": {"bio": "JavaScript specialist.", "avatar": "https://example.com/avatar11.jpg", "skills": ["javascript", "vue", "node.js"]},
        "isActive": True
    },
    {
        "userId": "U012", "email": "leo@example.com", "firstName": "Leo", "lastName": "Martinez",
        "role": "instructor", "dateJoined": datetime(2023, 7, 8),
        "profile": {"bio": "Loves teaching beginners.", "avatar": "https://example.com/avatar12.jpg", "skills": ["html", "css", "bootstrap"]},
        "isActive": True
    },
    {
        "userId": "U013", "email": "mia@example.com", "firstName": "Mia", "lastName": "Singh",
        "role": "instructor", "dateJoined": datetime(2023, 8, 3),
        "profile": {"bio": "Specialist in data science.", "avatar": "https://example.com/avatar13.jpg", "skills": ["pandas", "numpy", "scikit-learn"]},
        "isActive": True
    },
    {
        "userId": "U014", "email": "nate@example.com", "firstName": "Nate", "lastName": "O'Connell",
        "role": "instructor", "dateJoined": datetime(2023, 9, 18),
        "profile": {"bio": "DevOps engineer.", "avatar": "https://example.com/avatar14.jpg", "skills": ["docker", "kubernetes", "ci/cd"]},
        "isActive": True
    },
    {
        "userId": "U015", "email": "olivia@example.com", "firstName": "Olivia", "lastName": "Williams",
        "role": "instructor", "dateJoined": datetime(2023, 10, 22),
        "profile": {"bio": "AI researcher and ML coach.", "avatar": "https://example.com/avatar15.jpg", "skills": ["tensorflow", "keras", "deep learning"]},
        "isActive": True
    },
    {
        "userId": "U016", "email": "paul@example.com", "firstName": "Paul", "lastName": "Adams",
        "role": "instructor", "dateJoined": datetime(2023, 11, 5),
        "profile": {"bio": "Cloud solutions architect.", "avatar": "https://example.com/avatar16.jpg", "skills": ["aws", "azure", "gcp"]},
        "isActive": True
    },
    {
        "userId": "U017", "email": "quinn@example.com", "firstName": "Quinn", "lastName": "Brooks",
        "role": "instructor", "dateJoined": datetime(2023, 12, 10),
        "profile": {"bio": "Security consultant and instructor.", "avatar": "https://example.com/avatar17.jpg", "skills": ["cybersecurity", "network security"]},
        "isActive": True
    },
    {
        "userId": "U018", "email": "rachel@example.com", "firstName": "Rachel", "lastName": "Kim",
        "role": "instructor", "dateJoined": datetime(2024, 1, 9),
        "profile": {"bio": "Blockchain developer.", "avatar": "https://example.com/avatar18.jpg", "skills": ["solidity", "ethereum", "smart contracts"]},
        "isActive": False
    },
    {
        "userId": "U019", "email": "steve@example.com", "firstName": "Steve", "lastName": "Green",
        "role": "instructor", "dateJoined": datetime(2024, 2, 4),
        "profile": {"bio": "Software architect and mentor.", "avatar": "https://example.com/avatar19.jpg", "skills": ["system design", "architecture"]},
        "isActive": True
    },
    {
        "userId": "U020", "email": "tina@example.com", "firstName": "Tina", "lastName": "Ford",
        "role": "instructor", "dateJoined": datetime(2024, 3, 1),
        "profile": {"bio": "Mobile app dev expert.", "avatar": "https://example.com/avatar20.jpg", "skills": ["flutter", "kotlin", "android"]},
        "isActive": True
    }
]

# Insert into MongoDB
db.users.insert_many(sample_users)

print("Sample users inserted into the database.")

#%%
db.create_collection(
    'courses',
    validator={
        '$jsonSchema': {
            'bsonType': 'object',
            "required": ["courseId", "title", "instructorId", "level", "isPublished"],
            'properties': {
                'courseId': {'bsonType': 'string'},
                'title': {'bsonType': 'string'},
                'description': {'bsonType': 'string'},
                'instructorId': {'bsonType': 'string'},
                'category': {'bsonType': 'string'},
                'level': {
                    'enum': ['beginner', 'intermediate', 'advanced']
                },
                "duration": {"bsonType": "number"},
                "price": {"bsonType": "number"},
                "tags": {
                    "bsonType": "array",
                    "items": {"bsonType": "string"}
                },
                "createdAt": {"bsonType": "date"},
                "updatedAt": {"bsonType": "date"},
                "isPublished": {"bsonType": "bool"}
            }
        }
    },
    validationLevel='moderate'
)
db.courses.create_index("courseId", unique=True)

print("Courses collection created.")

#%%
sample_courses = [
    {
        "courseId": "C001",
        "title": "Introduction to Python",
        "description": "Learn Python from scratch with real coding exercises.",
        "instructorId": "U012",
        "category": "Programming",
        "level": "beginner",
        "duration": 12,
        "price": 49.99,
        "tags": ["python", "programming", "beginner"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C002",
        "title": "Advanced Machine Learning",
        "description": "Explore deep learning, NLP, and real-world projects.",
        "instructorId": "U015",
        "category": "AI & ML",
        "level": "advanced",
        "duration": 28,
        "price": 179.99,
        "tags": ["machine learning", "deep learning", "AI"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C003",
        "title": "DevOps with Docker & Kubernetes",
        "description": "Master containerization and orchestration tools.",
        "instructorId": "U014",
        "category": "DevOps",
        "level": "intermediate",
        "duration": 15,
        "price": 99.00,
        "tags": ["devops", "docker", "kubernetes"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C004",
        "title": "Web Development with Node.js and Vue",
        "description": "Build full-stack web apps using modern JS frameworks.",
        "instructorId": "U011",
        "category": "Web Development",
        "level": "intermediate",
        "duration": 20,
        "price": 129.99,
        "tags": ["node.js", "vue", "javascript"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C005",
        "title": "Secure Coding Practices",
        "description": "Learn how to write secure and robust code.",
        "instructorId": "U017",
        "category": "Cybersecurity",
        "level": "intermediate",
        "duration": 14,
        "price": 89.00,
        "tags": ["security", "code safety", "vulnerabilities"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C006",
        "title": "Spring Boot for Java Developers",
        "description": "Create robust APIs using Spring Boot and PostgreSQL.",
        "instructorId": "U019",
        "category": "Backend Development",
        "level": "advanced",
        "duration": 25,
        "price": 149.00,
        "tags": ["java", "spring", "backend"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C007",
        "title": "Cloud & Serverless Computing",
        "description": "Design scalable apps using AWS Lambda and Cloudflare.",
        "instructorId": "U016",
        "category": "Cloud Computing",
        "level": "intermediate",
        "duration": 18,
        "price": 139.00,
        "tags": ["serverless", "aws", "cloudflare"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    },
    {
        "courseId": "C008",
        "title": "Figma to HTML: UI Prototyping to Production",
        "description": "Turn designs into responsive HTML/CSS layouts.",
        "instructorId": "U020",
        "category": "Design & Frontend",
        "level": "beginner",
        "duration": 10,
        "price": 39.99,
        "tags": ["figma", "html", "css", "responsive design"],
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
        "isPublished": True
    }
]

db['courses'].insert_many(sample_courses)
#%%
db.create_collection(
    "enrollments",
    validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["enrollmentId", "studentId", "courseId", "enrolledAt", "progress", "isCompleted"],
            "properties": {
                "enrollmentId": {"bsonType": "string"},
                "studentId": {"bsonType": "string"},
                "courseId": {"bsonType": "string"},
                "enrolledAt": {"bsonType": "date"},
                "progress": {"bsonType": "int"},
                "isCompleted": {"bsonType": "bool"}
            }
        }
    }
)

db.enrollments.create_index("enrollmentId", unique=True)
print("Enrollments collection created.")

#%%
# Assume these are valid student userIds
student_ids = ["U001", "U002", "U003", "U004"]

# Assume these are valid courseIds
course_ids = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"]

# Generate 15 valid enrollments
sample_enrollments = []
for i in range(1, 16):
    enrollment = {
        "enrollmentId": f"E{str(i).zfill(3)}",
        "studentId": random.choice(student_ids),   # reference to users collection
        "courseId": random.choice(course_ids),     # reference to courses collection
        "enrolledAt": datetime.utcnow(),
        "progress": random.randint(0, 100),
        "isCompleted": random.choice([True, False])
    }
    sample_enrollments.append(enrollment)

db.enrollments.insert_many(sample_enrollments)

# %%
db.create_collection(
    'lessons',
    validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['lessonId', 'courseId', 'title', 'content'],
            'properties': {
                'lessonId': {'bsonType': 'string'},         # Unique lesson identifier
                'courseId': {'bsonType': 'string'},         # Reference to the course
                'title': {'bsonType': 'string'},            # Lesson title
                'content': {'bsonType': 'string'},          # Main lesson content (text/HTML)
                'videoUrl': {'bsonType': 'string'},         # Optional video URL
                'resources': {
                    'bsonType': 'array',
                    'items': {'bsonType': 'string'}         # Links or material names
                },
                'order': {'bsonType': 'int'},               # Order within the course
                'createdAt': {'bsonType': 'date'},
                'updatedAt': {'bsonType': 'date'}
            }
        }
    },
    validationLevel='moderate'
)
db.lessons.create_index("lessonId", unique=True)
print("Lessons collection created.")
# %%
import datetime
sample_lessons = [
    {'lessonId': 'L001',
  'courseId': 'C005',
  'title': 'Getting Started',
  'content': 'This is the content for Getting Started.',
  'videoUrl': 'https://videos.eduhub.com/gettingstarted',
  'resources': ['https://resources.eduhub.com/gettingstarted_notes.pdf'],
  'order': 1,
  'createdAt': datetime.datetime(2025, 5, 19, 10, 23, 6, 778914),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778938)},
 {'lessonId': 'L002',
  'courseId': 'C005',
  'title': 'Basic Syntax',
  'content': 'This is the content for Basic Syntax.',
  'videoUrl': 'https://videos.eduhub.com/basicsyntax',
  'resources': ['https://resources.eduhub.com/basicsyntax_notes.pdf'],
  'order': 2,
  'createdAt': datetime.datetime(2025, 5, 27, 10, 23, 6, 778949),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778952)},
 {'lessonId': 'L003',
  'courseId': 'C006',
  'title': 'Data Types',
  'content': 'This is the content for Data Types.',
  'videoUrl': 'https://videos.eduhub.com/datatypes',
  'resources': ['https://resources.eduhub.com/datatypes_notes.pdf'],
  'order': 3,
  'createdAt': datetime.datetime(2025, 6, 6, 10, 23, 6, 778957),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778959)},
 {'lessonId': 'L004',
  'courseId': 'C008',
  'title': 'Control Flow',
  'content': 'This is the content for Control Flow.',
  'videoUrl': 'https://videos.eduhub.com/controlflow',
  'resources': ['https://resources.eduhub.com/controlflow_notes.pdf'],
  'order': 4,
  'createdAt': datetime.datetime(2025, 5, 27, 10, 23, 6, 778964),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778966)},
 {'lessonId': 'L005',
  'courseId': 'C003',
  'title': 'Functions',
  'content': 'This is the content for Functions.',
  'videoUrl': 'https://videos.eduhub.com/functions',
  'resources': ['https://resources.eduhub.com/functions_notes.pdf'],
  'order': 5,
  'createdAt': datetime.datetime(2025, 4, 30, 10, 23, 6, 778970),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778972)},
 {'lessonId': 'L006',
  'courseId': 'C002',
  'title': 'Modules',
  'content': 'This is the content for Modules.',
  'videoUrl': 'https://videos.eduhub.com/modules',
  'resources': ['https://resources.eduhub.com/modules_notes.pdf'],
  'order': 6,
  'createdAt': datetime.datetime(2025, 5, 30, 10, 23, 6, 778976),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778978)},
 {'lessonId': 'L007',
  'courseId': 'C004',
  'title': 'File Handling',
  'content': 'This is the content for File Handling.',
  'videoUrl': 'https://videos.eduhub.com/filehandling',
  'resources': ['https://resources.eduhub.com/filehandling_notes.pdf'],
  'order': 7,
  'createdAt': datetime.datetime(2025, 6, 11, 10, 23, 6, 778981),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778984)},
 {'lessonId': 'L008',
  'courseId': 'C006',
  'title': 'Error Handling',
  'content': 'This is the content for Error Handling.',
  'videoUrl': 'https://videos.eduhub.com/errorhandling',
  'resources': ['https://resources.eduhub.com/errorhandling_notes.pdf'],
  'order': 8,
  'createdAt': datetime.datetime(2025, 5, 21, 10, 23, 6, 778990),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 778997)},
 {'lessonId': 'L009',
  'courseId': 'C004',
  'title': 'OOP Basics',
  'content': 'This is the content for OOP Basics.',
  'videoUrl': 'https://videos.eduhub.com/oopbasics',
  'resources': ['https://resources.eduhub.com/oopbasics_notes.pdf'],
  'order': 9,
  'createdAt': datetime.datetime(2025, 4, 17, 10, 23, 6, 779001),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779003)},
 {'lessonId': 'L010',
  'courseId': 'C007',
  'title': 'Advanced OOP',
  'content': 'This is the content for Advanced OOP.',
  'videoUrl': 'https://videos.eduhub.com/advancedoop',
  'resources': ['https://resources.eduhub.com/advancedoop_notes.pdf'],
  'order': 10,
  'createdAt': datetime.datetime(2025, 6, 9, 10, 23, 6, 779006),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779008)},
 {'lessonId': 'L011',
  'courseId': 'C005',
  'title': 'Decorators',
  'content': 'This is the content for Decorators.',
  'videoUrl': 'https://videos.eduhub.com/decorators',
  'resources': ['https://resources.eduhub.com/decorators_notes.pdf'],
  'order': 11,
  'createdAt': datetime.datetime(2025, 4, 23, 10, 23, 6, 779011),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779013)},
 {'lessonId': 'L012',
  'courseId': 'C002',
  'title': 'Generators',
  'content': 'This is the content for Generators.',
  'videoUrl': 'https://videos.eduhub.com/generators',
  'resources': ['https://resources.eduhub.com/generators_notes.pdf'],
  'order': 12,
  'createdAt': datetime.datetime(2025, 5, 30, 10, 23, 6, 779016),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779018)},
 {'lessonId': 'L013',
  'courseId': 'C001',
  'title': 'Comprehensions',
  'content': 'This is the content for Comprehensions.',
  'videoUrl': 'https://videos.eduhub.com/comprehensions',
  'resources': ['https://resources.eduhub.com/comprehensions_notes.pdf'],
  'order': 13,
  'createdAt': datetime.datetime(2025, 4, 25, 10, 23, 6, 779021),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779023)},
 {'lessonId': 'L014',
  'courseId': 'C002',
  'title': 'Working with APIs',
  'content': 'This is the content for Working with APIs.',
  'videoUrl': 'https://videos.eduhub.com/workingwithapis',
  'resources': ['https://resources.eduhub.com/workingwithapis_notes.pdf'],
  'order': 14,
  'createdAt': datetime.datetime(2025, 6, 10, 10, 23, 6, 779026),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779028)},
 {'lessonId': 'L015',
  'courseId': 'C008',
  'title': 'Database Access',
  'content': 'This is the content for Database Access.',
  'videoUrl': 'https://videos.eduhub.com/databaseaccess',
  'resources': ['https://resources.eduhub.com/databaseaccess_notes.pdf'],
  'order': 15,
  'createdAt': datetime.datetime(2025, 6, 1, 10, 23, 6, 779030),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 779050)},
 {'lessonId': 'L016',
  'courseId': 'C003',
  'title': 'Testing',
  'content': 'This is the content for Testing.',
  'videoUrl': 'https://videos.eduhub.com/testing',
  'resources': ['https://resources.eduhub.com/testing_notes.pdf'],
  'order': 16,
  'createdAt': datetime.datetime(2025, 5, 27, 10, 23, 6, 780338),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 780358)},
 {'lessonId': 'L017',
  'courseId': 'C004',
  'title': 'Debugging',
  'content': 'This is the content for Debugging.',
  'videoUrl': 'https://videos.eduhub.com/debugging',
  'resources': ['https://resources.eduhub.com/debugging_notes.pdf'],
  'order': 17,
  'createdAt': datetime.datetime(2025, 5, 25, 10, 23, 6, 780370),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 780378)},
 {'lessonId': 'L018',
  'courseId': 'C005',
  'title': 'CI/CD Basics',
  'content': 'This is the content for CI/CD Basics.',
  'videoUrl': 'https://videos.eduhub.com/ci/cdbasics',
  'resources': ['https://resources.eduhub.com/ci/cdbasics_notes.pdf'],
  'order': 18,
  'createdAt': datetime.datetime(2025, 5, 30, 10, 23, 6, 780386),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 780389)},
 {'lessonId': 'L019',
  'courseId': 'C006',
  'title': 'Docker Intro',
  'content': 'This is the content for Docker Intro.',
  'videoUrl': 'https://videos.eduhub.com/dockerintro',
  'resources': ['https://resources.eduhub.com/dockerintro_notes.pdf'],
  'order': 19,
  'createdAt': datetime.datetime(2025, 4, 23, 10, 23, 6, 780395),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 780400)},
 {'lessonId': 'L020',
  'courseId': 'C003',
  'title': 'Kubernetes Intro',
  'content': 'This is the content for Kubernetes Intro.',
  'videoUrl': 'https://videos.eduhub.com/kubernetesintro',
  'resources': ['https://resources.eduhub.com/kubernetesintro_notes.pdf'],
  'order': 20,
  'createdAt': datetime.datetime(2025, 4, 30, 10, 23, 6, 780406),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 780410)},
 {'lessonId': 'L021',
  'courseId': 'C005',
  'title': 'Final Project',
  'content': 'This is the content for Final Project.',
  'videoUrl': 'https://videos.eduhub.com/finalproject',
  'resources': ['https://resources.eduhub.com/finalproject_notes.pdf'],
  'order': 21,
  'createdAt': datetime.datetime(2025, 6, 12, 10, 23, 6, 781544),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 781565)},
 {'lessonId': 'L022',
  'courseId': 'C008',
  'title': 'Review Session',
  'content': 'This is the content for Review Session.',
  'videoUrl': 'https://videos.eduhub.com/reviewsession',
  'resources': ['https://resources.eduhub.com/reviewsession_notes.pdf'],
  'order': 22,
  'createdAt': datetime.datetime(2025, 5, 4, 10, 23, 6, 781579),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 781585)},
 {'lessonId': 'L023',
  'courseId': 'C008',
  'title': 'Capstone Prep',
  'content': 'This is the content for Capstone Prep.',
  'videoUrl': 'https://videos.eduhub.com/capstoneprep',
  'resources': ['https://resources.eduhub.com/capstoneprep_notes.pdf'],
  'order': 23,
  'createdAt': datetime.datetime(2025, 5, 11, 10, 23, 6, 781614),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 781620)},
 {'lessonId': 'L024',
  'courseId': 'C004',
  'title': 'Deployment',
  'content': 'This is the content for Deployment.',
  'videoUrl': 'https://videos.eduhub.com/deployment',
  'resources': ['https://resources.eduhub.com/deployment_notes.pdf'],
  'order': 24,
  'createdAt': datetime.datetime(2025, 5, 20, 10, 23, 6, 781626),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 781629)},
 {'lessonId': 'L025',
  'courseId': 'C007',
  'title': 'Wrap Up',
  'content': 'This is the content for Wrap Up.',
  'videoUrl': 'https://videos.eduhub.com/wrapup',
  'resources': ['https://resources.eduhub.com/wrapup_notes.pdf'],
  'order': 25,
  'createdAt': datetime.datetime(2025, 4, 16, 10, 23, 6, 781634),
  'updatedAt': datetime.datetime(2025, 6, 13, 10, 23, 6, 781638)}]

db.lessons.insert_many(sample_lessons)
#%%

db.create_collection(
    'assignments',
    validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['assignmentId', 'courseId', 'title', 'dueDate'],
            'properties': {
                'assignmentId': {'bsonType': 'string'},     # Unique assignment identifier
                'courseId': {'bsonType': 'string'},         # Reference to the course
                'lessonId': {'bsonType': 'string'},         # Optional reference to lesson
                'title': {'bsonType': 'string'},            # Assignment title
                'description': {'bsonType': 'string'},      # Assignment details
                'dueDate': {'bsonType': 'date'},            # Deadline
                'maxScore': {'bsonType': 'int'},            # Total marks
                'createdAt': {'bsonType': 'date'},
                'updatedAt': {'bsonType': 'date'}
            }
        }
    },
    validationLevel='moderate'
)

db.assignments.create_index("assignmentId", unique=True)
print("Assignments collection created.")
#%%
from datetime import datetime, timedelta

sample_assignments = []

for i in range(1, 11):
    course_id = f"C00{random.randint(1, 8)}"
    lesson_id = f"L{str(random.randint(1, 25)).zfill(3)}"
    created = datetime.utcnow() - timedelta(days=random.randint(10, 30))
    updated = datetime.utcnow()

    sample_assignments.append({
        "assignmentId": f"A{str(i).zfill(3)}",
        "courseId": course_id,
        "lessonId": lesson_id,
        "title": f"Assignment {i}",
        "description": f"Complete the task described in Assignment {i}.",
        "dueDate": updated + timedelta(days=random.randint(5, 15)),
        "maxScore": random.randint(50, 100),
        "createdAt": created,
        "updatedAt": updated
    })

sample_assignments

db.assignments.insert_many(sample_assignments)

# %%
db.create_collection(
    'submissions',
    validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': [
                'submissionId',
                'assignmentId',
                'studentId',
                'submittedAt'
            ],
            'properties': {
                'submissionId': {'bsonType': 'string'},   # Unique submission ID
                'assignmentId': {'bsonType': 'string'},   # Reference to assignment
                'studentId': {'bsonType': 'string'},      # Reference to user
                'courseId': {'bsonType': 'string'},       # Optional course reference
                'lessonId': {'bsonType': 'string'},       # Optional lesson reference
                'content': {'bsonType': 'string'},        # Link or text
                'score': {'bsonType': 'int'},             # Score awarded
                'feedback': {'bsonType': 'string'},       # Feedback/comments
                'submittedAt': {'bsonType': 'date'},      # Submission time
                'gradedAt': {'bsonType': 'date'}          # Optional grading timestamp
            }
        }
    },
    validationLevel='moderate'
)
db.submissions.create_index("submissionId", unique=True)
print("Submissions collection created.")

#%%
sample_submissions = [
    {
        "submissionId": "S001",
        "assignmentId": "A001",
        "courseId": "C006",
        "lessonId": "L015",
        "studentId": "U002",
        "content": "https://example.com/submissions/1",
        "score": 75,
        "feedback": "Well done.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S002",
        "assignmentId": "A001",
        "courseId": "C006",
        "lessonId": "L015",
        "studentId": "U004",
        "content": "https://example.com/submissions/2",
        "score": 60,
        "feedback": "Needs improvement.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S003",
        "assignmentId": "A002",
        "courseId": "C006",
        "lessonId": "L008",
        "studentId": "U003",
        "content": "https://example.com/submissions/3",
        "score": 85,
        "feedback": "Excellent work!",
        "submittedAt": datetime(2025, 6, 12),
        "gradedAt": datetime(2025, 6, 13)
    },
    {
        "submissionId": "S004",
        "assignmentId": "A003",
        "courseId": "C008",
        "lessonId": "L013",
        "studentId": "U001",
        "content": "https://example.com/submissions/4",
        "score": 90,
        "feedback": "Great submission.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S005",
        "assignmentId": "A003",
        "courseId": "C008",
        "lessonId": "L013",
        "studentId": "U004",
        "content": "https://example.com/submissions/5",
        "score": 65,
        "feedback": "Good effort.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S006",
        "assignmentId": "A004",
        "courseId": "C001",
        "lessonId": "L006",
        "studentId": "U002",
        "content": "https://example.com/submissions/6",
        "score": 80,
        "feedback": "Solid work.",
        "submittedAt": datetime(2025, 6, 12),
        "gradedAt": datetime(2025, 6, 13)
    },
    {
        "submissionId": "S007",
        "assignmentId": "A005",
        "courseId": "C007",
        "lessonId": "L017",
        "studentId": "U003",
        "content": "https://example.com/submissions/7",
        "score": 70,
        "feedback": "Well structured.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S008",
        "assignmentId": "A006",
        "courseId": "C003",
        "lessonId": "L018",
        "studentId": "U001",
        "content": "https://example.com/submissions/8",
        "score": 77,
        "feedback": "Good use of examples.",
        "submittedAt": datetime(2025, 6, 12),
        "gradedAt": datetime(2025, 6, 13)
    },
    {
        "submissionId": "S009",
        "assignmentId": "A007",
        "courseId": "C002",
        "lessonId": "L019",
        "studentId": "U004",
        "content": "https://example.com/submissions/9",
        "score": 92,
        "feedback": "Outstanding job.",
        "submittedAt": datetime(2025, 6, 11),
        "gradedAt": datetime(2025, 6, 12)
    },
    {
        "submissionId": "S010",
        "assignmentId": "A008",
        "courseId": "C003",
        "lessonId": "L007",
        "studentId": "U002",
        "content": "https://example.com/submissions/10",
        "score": 88,
        "feedback": "Impressive depth.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S011",
        "assignmentId": "A009",
        "courseId": "C001",
        "lessonId": "L020",
        "studentId": "U003",
        "content": "https://example.com/submissions/11",
        "score": 66,
        "feedback": "Meets expectations.",
        "submittedAt": datetime(2025, 6, 13),
        "gradedAt": datetime(2025, 6, 14)
    },
    {
        "submissionId": "S012",
        "assignmentId": "A010",
        "courseId": "C003",
        "lessonId": "L019",
        "studentId": "U004",
        "content": "https://example.com/submissions/12",
        "score": 94,
        "feedback": "Brilliant analysis.",
        "submittedAt": datetime(2025, 6, 12),
        "gradedAt": datetime(2025, 6, 13)
    }
]
db.submissions.insert_many(sample_submissions)
# %%

# 1. Add a new student user
new_student = {
    "userId": "U021",
    "email": "jane.doe@example.com",
    "firstName": "Jane",
    "lastName": "Doe",
    "role": "student",
    "dateJoined": datetime.utcnow(),
    "profile": {
        "bio": "Enthusiastic learner.",
        "avatar": "",
        "skills": ["python"]
    },
    "isActive": True
}
db.users.insert_one(new_student)
print("New student added.")

# 2. Create a new course
new_course = {
    "courseId": "C009",
    "title": "Data Structures in Python",
    "description": "Learn common data structures using Python.",
    "instructorId": "U015",  # ensure this instructor exists
    "category": "Computer Science",
    "level": "intermediate",
    "duration": 16,
    "price": 79.99,
    "tags": ["data structures", "python", "algorithms"],
    "createdAt": datetime.utcnow(),
    "updatedAt": datetime.utcnow(),
    "isPublished": True
}
db.courses.insert_one(new_course)
print("New course created.")

# 3. Enroll the student in the course
enrollment = {
    "enrollmentId": "E016",
    "studentId": "U021",
    "courseId": "C009",
    "enrolledAt": datetime.utcnow(),
    "progress": 0,
    "isCompleted": False
}
db.enrollments.insert_one(enrollment)
print("Student enrolled in course.")

# 4. Add a new lesson to an existing course
lesson = {
    "lessonId": "L026",
    "courseId": "C009",
    "title": "Introduction to Lists",
    "content": "This lesson covers list basics, operations, and use cases.",
    "videoUrl": "https://example.com/videos/lists",
    "duration": 25,  # minutes
    "createdAt": datetime.utcnow(),
    "updatedAt": datetime.utcnow()
}
db.lessons.insert_one(lesson)
print("Lesson added to course.")

# %%
# Find all active students
active_students = db.users.find({
    "role": "student",
    "isActive": True
})

for student in active_students:
    print(student)

#%%
#  Retrieve course details with instructor information
course_details = db.courses.aggregate([
    {
        "$lookup": {
            "from": "users",
            "localField": "instructorId",
            "foreignField": "userId",
            "as": "instructor"
        }
    },
    {
        "$unwind": "$instructor"
    }
])

for course in course_details:
    print(course)
#%%
#  Get all courses in a specific category
category = "Programming"  # Example category
courses_in_category = db.courses.find({"category": category})

for course in courses_in_category:
    print(course)
#%%
#  Find students enrolled in a particular course
course_id = "C007"  # Example courseId

students_in_course = db.enrollments.aggregate([
    {
        "$match": {"courseId": course_id}
    },
    {
        "$lookup": {
            "from": "users",
            "localField": "studentId",
            "foreignField": "userId",
            "as": "studentDetails"
        }
    },
    {
        "$unwind": "$studentDetails"
    }
])

for student in students_in_course:
    print(student["studentDetails"])

#%%

# Search courses by title (case-insensitive, partial match)
search_term = "python"  # Example search term

matching_courses = db.courses.find({
    "title": {"$regex": search_term, "$options": "i"}
})

for course in matching_courses:
    print(course)

# %%
from collections import Counter

def check_duplicates(collection, field):
    values = [doc[field] for doc in db[collection].find({}, {field: 1}) if field in doc]
    counter = Counter(values)
    duplicates = [val for val, count in counter.items() if count > 1]
    return duplicates

collections_fields = {
    "users": ["userId", "email"],
    "courses": ["courseId"],
    "enrollments": ["enrollmentId"],
    "lessons": ["lessonId"],
    "assignments": ["assignmentId"],
    "submissions": ["submissionId"]
}

for collection, fields in collections_fields.items():
    for field in fields:
        duplicates = check_duplicates(collection, field)
        if duplicates:
            print(f"⚠️ Duplicates found in '{collection}.{field}': {duplicates}")
        else:
            print(f"✅ No duplicates in '{collection}.{field}', creating index...")
            db[collection].create_index(field, unique=True)


# %%
# Update a user’s profile information
db.users.update_one(
    {"userId": "U001"},
    {
        "$set": {
            "profile.bio": "Data Science enthusiast and Python developer.",
            "profile.avatar": "https://example.com/avatar.jpg",
            "profile.skills": ["Python", "Data Analysis", "MongoDB"]
        }
    }
)
# Mark a course as published
db.courses.update_one(
    {"courseId": "C001"},
    {
        "$set": {
            "isPublished": True,
            "updatedAt": datetime.utcnow()
        }
    }
)

# Update assignment grades
db.submissions.update_one(
    {"submissionId": "S001"},
    {
        "$set": {
            "score": 88,
            "gradedAt": datetime.utcnow()
        }
    }
)

# Add tags to an existing course 
db.courses.update_one(
    {"courseId": "C002"},
    {
        "$addToSet": {
            "tags": {"$each": ["project-based", "certificate"]}
        },
        "$set": {"updatedAt": datetime.utcnow()}
    }
)


# 1. Remove a user (soft delete by setting isActive to false)
db.users.update_one(
    {"userId": "U003"},
    {"$set": {"isActive": False}}
)

# 2. Delete an enrollment
db.enrollments.delete_one(
    {"enrollmentId": "E007"}
)

# 3. Remove a lesson from a course
db.lessons.delete_one(
    {"lessonId": "L010"}
)
# %%

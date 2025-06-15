
# EduHub MongoDB Project

This project is part of the AltSchool of Data Engineering (2024 Second Semester) and demonstrates how to design, implement, and optimize a NoSQL database using MongoDB for an online e-learning platform named **EduHub**.

---

## Project Setup Instructions

### Requirements

- Python 3.8+
- MongoDB Atlas or local MongoDB server
- Required Libraries:
  - `pymongo`
  - `pandas`
  - `datetime`

### Setup

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/your-username/mongodb-eduhub-project.git
   cd mongodb-eduhub-project
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # or `env\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. Set up your MongoDB URI inside your Python script:
   ```python
   uri = "mongodb+srv://<username>:<password>@<cluster-url>"
   client = MongoClient(uri)
   ```

4. Run the script or notebook to initialize the database:
   - `src/eduhub_queries.py`
   - `notebooks/eduhub_main.ipynb`

---

## Database Schema Documentation

### Collections and Key Fields

- **users**
  - `userId`, `email`, `firstName`, `lastName`, `role`, `profile`, `isActive`, `dateJoined`

- **courses**
  - `courseId`, `title`, `description`, `instructorId`, `tags`, `level`, `price`, `createdAt`

- **enrollments**
  - `enrollmentId`, `studentId`, `courseId`, `enrolledAt`, `progress`, `isCompleted`

- **lessons**
  - `lessonId`, `courseId`, `title`, `content`, `videoUrl`, `resources`, `order`

- **assignments**
  - `assignmentId`, `courseId`, `lessonId`, `title`, `description`, `dueDate`, `maxScore`

- **submissions**
  - `submissionId`, `assignmentId`, `studentId`, `score`, `submittedAt`, `gradedAt`, `feedback`

---

## 🔍 Query Explanations

### CRUD Operations
- Create new users, courses, lessons, enrollments
- Retrieve active students, courses by category, instructor info
- Update user profiles, mark courses published, update grades
- Delete (soft or hard) users, enrollments, lessons

### Aggregation Queries
- Enrollment stats per course
- Average scores by student and instructor
- Monthly trends and category popularity
- Revenue per instructor and completion rates

Refer to `src/eduhub_aggregation_queries.py` for complete query logic with comments.

---

## 🚀 Performance Analysis Results

### Indexes Created:
- `userId`, `email` on users
- `courseId` on courses
- `dueDate` on assignments
- `studentId`, `courseId` on enrollments and submissions

### Optimization Process
- Used `explain()` to identify slow queries
- Indexed fields used in filters and regex
- Time comparisons before/after optimization:
  - Course search reduced from 0.08s → 0.02s
  - Enrollment lookup improved with compound index

---

##  Challenges Faced and Solutions

| Challenge | Solution |
|----------|----------|
| Avoiding duplicate keys | Created unique indexes and added validation scripts |
| Enforcing schema rules | Used `$jsonSchema` validators for all collections |
| Aggregating across collections | Used `$lookup` and `$unwind` efficiently |
| MongoDB connection issues | Used MongoDB Atlas with correct URI parameters |

---

## Project Structure

```
mongodb-eduhub-project/
├── README.md
├── notebooks/
│   └── eduhub_main.ipynb
├── src/
│   └── eduhub_queries.py
│   └── eduhub_aggregation_queries.py
├── data/
│   ├── sample_data.json
│   └── schema_validation.json
├── docs/
│   ├── performance_analysis.md
│   └── presentation.pptx
├── test_results.md
└── .gitignore
```

---

## License

This project is licensed under the MIT License.

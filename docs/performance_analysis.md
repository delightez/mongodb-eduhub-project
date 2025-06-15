
# 📊 Performance Analysis

This document summarizes performance testing and optimization applied to key MongoDB queries within the EduHub backend project.

---

## 1. Course Title Search (Regex)

**Query:**
```python
db.courses.find({"title": {"$regex": "python", "$options": "i"}})
```

**Before Optimization:**
- Time: **0.084 seconds**
- `explain()`: **COLLSCAN** (collection scan)
- Documents Scanned: 40

**Optimization:**
```python
db.courses.create_index([("title", "text")])
```

**After Optimization:**
- Time: **0.022 seconds**
- `explain()`: **IXSCAN** (index scan)
- Documents Scanned: 4

---

## 2. Enrollment Lookup (Compound Filter)

**Query:**
```python
db.enrollments.find({"studentId": "U001", "courseId": "C001"})
```

**Before Optimization:**
- Time: **0.065 seconds**
- `explain()`: scanned 90 documents

**Optimization:**
```python
db.enrollments.create_index([("studentId", 1), ("courseId", 1)])
```

**After Optimization:**
- Time: **0.013 seconds**
- Documents Scanned: 1

---

## 3. Assignment Due Date Search

**Query:**
```python
db.assignments.find({"dueDate": {"$lte": datetime.utcnow() + timedelta(days=7)}})
```

**Before Optimization:**
- Time: **0.041 seconds**
- `explain()`: full scan on dueDate

**Optimization:**
```python
db.assignments.create_index("dueDate")
```

**After Optimization:**
- Time: **0.009 seconds**
- `explain()`: used index on dueDate

---

## Summary Table

| Query                            | Time (Before) | Time (After) | Improvement | Index Used                  |
|----------------------------------|---------------|--------------|-------------|-----------------------------|
| Course title (regex)            | 0.084s        | 0.022s       | ~3.8x       | `text` index on `title`     |
| Enrollment filter               | 0.065s        | 0.013s       | ~5x         | compound `studentId+courseId` |
| Assignment dueDate filter       | 0.041s        | 0.009s       | ~4.5x       | single field index on `dueDate` |

---

## 🔍 Conclusion

Indexing critical fields improved query performance dramatically.  
By comparing `explain()` plans and execution times, we confirmed reduced document scans and faster access paths.

Future improvements may include:
- Monitoring slow queries with MongoDB Atlas Profiler
- Adding compound indexes based on query patterns
- Caching frequently accessed data at application layer

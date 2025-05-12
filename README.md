# Student Course Management API

A simple FastAPI project to manage students, courses, and enrollments. This API allows you to:
- Create students and courses
- Enroll students in courses
- Retrieve student or course data 

---

## 📁 Project Structure

```
student-course-api/
│
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── database.py       # Database connection
│   ├── crud.py           # Business logic
│   ├── __init__.py       
│
├── .gitignore
├── requirements.txt
├── README.md
└── VirtualEnv/           # Virtual environment (should is excluded from Git)
```

---

## ▶️ How to Run the Project

1. **Create virtual environment**
   ```bash
   python -m venv VirtualEnv
   source VirtualEnv/bin/activate  # Linux/macOS
   VirtualEnv\Scripts\activate     # Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run FastAPI server[from root directory]**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 📡 API Usage via `curl`

Below are sample `curl` commands to test the API from **Windows CMD**, **PowerShell**, and **Linux/macOS Bash**.

---

### 🔍 GET Requests

#### Windows CMD / PowerShell / Linux/macOS
```bash
curl -X GET "http://localhost:8000/students/1?skip=0&limit=2"
curl -X GET "http://localhost:8000/courses/1?skip=0&limit=2"
```

---

### 📝 POST Requests

#### ➕ Create a Student

##### Windows CMD
```cmd
curl -X POST http://localhost:8000/students/ -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"email\":\"allen@example.com\",\"id\":\"15\"}"
```

##### PowerShell
```powershell
curl -X POST http://localhost:8000/students/ -H "Content-Type: application/json" -d '{\"name\":\"Alice\",\"email\":\"allen@example.com\",\"id\":\"15\"}'
```

##### Linux / macOS
```bash
curl -X POST http://localhost:8000/students/ -H "Content-Type: application/json" -d '{"name":"Alice","email":"allen@example.com","id":"15"}'
```

---

#### ➕ Create a Course

##### Windows CMD
```cmd
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d "{\"title\":\"php\",\"description\":\"complete basic to advance\",\"id\":\"22\"}"
```

##### PowerShell
```powershell
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d '{\"title\":\"php\",\"description\":\"complete basic to advance\",\"id\":\"22\"}'
```

##### Linux / macOS
```bash
curl -X POST http://localhost:8000/courses/ -H "Content-Type: application/json" -d '{"title":"php","description":"complete basic to advance","id":"22"}'
```

---

#### ✅ Enroll a Student in a Course

##### Windows CMD
```cmd
curl -X POST http://localhost:8000/enroll/ -H "Content-Type: application/json" -d "{\"student_id\":\"10\",\"course_id\":\"22\"}"
```

##### PowerShell
```powershell
curl -X POST http://localhost:8000/enroll/ -H "Content-Type: application/json" -d '{\"student_id\":\"10\",\"course_id\":\"22\"}'
```

##### Linux / macOS
```bash
curl -X POST http://localhost:8000/enroll/ -H "Content-Type: application/json" -d '{"student_id":"10","course_id":"22"}'
```

---

## ⚠️ Error Handling Tips

If a student or course is created with a duplicate `id` or `email` (which should be unique), the database raises an integrity error. This may return a **500 Internal Server Error**.  
To present clearer feedback to users, wrap your DB calls like this:

```python
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

try:
    db.add(student)
    db.commit()
except IntegrityError:
    db.rollback()
    raise HTTPException(status_code=400, detail="Student with this email or ID already exists.")
```

---

## 📦 Dependencies

See `requirements.txt`. To freeze new dependencies:

```bash
pip freeze > requirements.txt
```

---

## 🧾 .gitignore

Make sure your `.gitignore` includes:

```
# Ignore virtual environment
VirtualEnv/
__pycache__/
*.pyc
.env
```

---

## 🛠️ To Do (Optional)

- Add Alembic for migrations
- Add API docs description (`/docs`)
- Add test cases under `tests/`

---

## 📞 Contact

For any questions or improvements, feel free to open an issue or pull request.
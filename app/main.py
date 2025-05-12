from fastapi import FastAPI, Depends, HTTPException,Query
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)
 
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/students/", response_model=schemas.StudentCreate)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.post("/courses/", response_model=schemas.CourseCreate)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, course)

@app.post("/enroll/")
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    return crud.enroll_student(db, enrollment)



@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db),skip: int = Query(0, ge=0),limit: int = Query(10, le=100)):
    
    student = crud.get_student(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    total = len(student.courses)
    paginated_courses = student.courses[skip : skip + limit]

    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "total_course_enrolled_in": total,
        "courses": paginated_courses
    }



@app.get("/courses/{course_id}", response_model=schemas.CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db),skip: int = Query(0, ge=0),limit: int = Query(10, le=100)):
    course = crud.get_course(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    

    total =len(course.students)
    paginated_students = course.students[skip : skip + limit]


    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "total_student_enrolled_in": total,
        "students": paginated_students
    }


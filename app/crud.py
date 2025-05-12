from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)

    try:
        db.commit()
        db.refresh(db_student)
        return db_student
    except IntegrityError as e:
        db.rollback()

        # PostgreSQL's specific error attributes
        constraint = getattr(e.orig.diag, "constraint_name", "")
        if constraint == "students_email_key":
            raise HTTPException(status_code=409, detail="Email already exists.")
        elif constraint == "students_pkey":
            raise HTTPException(status_code=409, detail="Student ID already exists.")
        else:
            raise HTTPException(status_code=400, detail="Database integrity error.")





def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    
    

    try:
        db.commit()
        db.refresh(db_course)
        return db_course
    
    except IntegrityError as e:
        db.rollback()

        # PostgreSQL's specific error attributes
        constraint = getattr(e.orig.diag, "constraint_name", "")
        if constraint == "courses_pkey":
            raise HTTPException(status_code=409, detail="Course ID already exists.")
        else:
            raise HTTPException(status_code=400, detail="Database integrity error.")






def enroll_student(db: Session, enrollment: schemas.EnrollmentCreate):
    student = db.query(models.Student).get(enrollment.student_id)
    course = db.query(models.Course).get(enrollment.course_id)
    if course not in student.courses:
        student.courses.append(course)
        db.commit()
    return student



def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()



def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


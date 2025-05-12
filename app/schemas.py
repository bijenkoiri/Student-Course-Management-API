from pydantic import BaseModel, EmailStr
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime





class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    id: int


class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase): 
    id: int





class CourseSimple(CourseBase):
    pass

class StudentSimple(StudentBase):
    pass



class CourseResponse(CourseBase):
    id: int
    total_student_enrolled_in: int
    students: List[StudentSimple]
    class Config:
        orm_mode = True




class StudentResponse(StudentBase):
    id: int
    total_course_enrolled_in: int
    courses: List[CourseSimple]
    class Config:
        orm_mode = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int




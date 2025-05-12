from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base





enrollments_table = Table(
    'enrollments',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('enrolled_on', DateTime, default=datetime.now())
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    courses = relationship('Course', secondary=enrollments_table, back_populates='students')



class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    students = relationship('Student', secondary=enrollments_table, back_populates='courses')

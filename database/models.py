from sqlalchemy import BigInteger, Boolean, Column, Float, ForeignKey, Integer, PrimaryKeyConstraint, String, Table, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    or_, create_engine, DateTime
)


engine=create_engine("sqlite:///LMS.db",connect_args={'check_same_thread': False}, echo=True)
Session = sessionmaker(bind=engine)
seshion = Session()
Base = declarative_base()

class Student(Base):
    __tablename__="student"
    name=Column(String(100),nullable=False)
    email = Column(String(70), primary_key=True, nullable=False)
    password=Column(String(50),nullable=False)
    contact=Column(String(15),nullable=False, unique=True)
    def __repr__(self):
        return f"email : {self.email}"
    
class Instructor(Base):
    __tablename__="instructor"
    email = Column(String(70), primary_key=True, nullable=False)
    password=Column(String(50),nullable=False)
    contact=Column(String(15),nullable=False, unique=True)
    def __repr__(self):
        return f"email : {self.email}"
    
class Course(Base):
    __tablename__="course"
    code=Column(String(20),nullable=False, primary_key=True)
    name=Column(String)
    credits=Column(Float)
    overview=Column(String(200))
    course = relationship("Assignment", back_populates="assignment")
    course_content = relationship("Content", back_populates="content_course")
    course_history = relationship("Content", back_populates="history_course")

class Assignment(Base):
    __tablename__="assignment"
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    code_fk=Column(String(20), ForeignKey("course.code"))
    uploadAt=Column(DateTime(timezone=True), server_default=func.now())
    endedAt=Column(DateTime(timezone=True))
    totalMarks=Column(Float)
    obtmarks=Column(Float)
    submittedAt=Column(DateTime(timezone=True), server_default=func.now())
    assignment = relationship("Course", back_populates="course")

association_table=Table(
"std_crs",
Base.metadata,
Column("lid",ForeignKey("student.email")),
Column("rid",ForeignKey("course.code"))
)

association_table=Table(
"ins_crs",
Base.metadata,
Column("lid",ForeignKey("instructor.email")),
Column("rid",ForeignKey("course.code"))
)

class Content(Base):
    __tablename__="content"
    code_fk=Column(String(20),ForeignKey("course.code"))
    path=Column(String(1000))
    content_course = relationship("Course", back_populates="course_content")
    __table_args__=(
        PrimaryKeyConstraint(code_fk,path)

    )

class History(Base):
    __tablename__="history"
    code_fk=Column(String(20),ForeignKey("course.code"))
    date=Column(DateTime(timezone=True), server_default=func.now())
    history_course = relationship("Course", back_populates="course_history")
    __table_args__=(
        PrimaryKeyConstraint(code_fk,date)

    )



from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

STUDENTS_ROUTE = "/students"

@app.post(f"{STUDENTS_ROUTE}/insert", response_model=schemas.Student)
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


@app.get(f"{STUDENTS_ROUTE}", response_model=List[schemas.Student])
def read_student(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@app.put(f"{STUDENTS_ROUTE}/update/{{student_id}}", response_model=schemas.Student)
def update_student(student: schemas.StudentUpdate, student_id: int, db: Session = Depends(get_db)):
    student = crud.update_student(db, student_id, student)
    return student


@app.delete(f"{STUDENTS_ROUTE}/update/{{student_id}}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    response = crud.delete_student(db, student_id)
    return response

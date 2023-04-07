from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from student import schemas, crud

router = APIRouter()

STUDENTS_ROUTE = "/students"

@router.post(f"{STUDENTS_ROUTE}/insert", response_model=schemas.Students)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)


@router.get(f"{STUDENTS_ROUTE}", response_model=List[schemas.Students])
def read_student(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students


@router.put(f"{STUDENTS_ROUTE}/update/{{student_id}}", response_model=schemas.Students)
def update_student(student: schemas.StudentUpdate, student_id: int, db: Session = Depends(get_db)):
    student = crud.update_student(db, student_id, student)
    return student


@router.delete(f"{STUDENTS_ROUTE}/delete/{{student_id}}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    response = crud.delete_student(db, student_id)
    return response
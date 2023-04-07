from sqlalchemy.orm import Session
from fastapi import HTTPException

import student.models as models
import student.schemas as schemas


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Test(name=student.name, dept_name=student.dept_name, tot_cred=student.tot_cred)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student: schemas.Students):
    db_student = db.query(models.Test).filter(models.Test.id == student_id).first()
    if db_student:
        db_student.name = student.name if student.name is not None else db_student.name
        db_student.dept_name = student.dept_name if student.dept_name is not None else db_student.dept_name
        db_student.tot_cred = student.tot_cred if student.tot_cred is not None else db_student.tot_cred
        db.commit()
        db.refresh(db_student)
        return db_student
    else:
        raise HTTPException(status_code=404, detail="Student not found")


def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Test).filter(models.Test.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")


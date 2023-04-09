from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from database import get_db
from sweater import schemas, crud

router = APIRouter()

SWEATER_ROUTE = "/sweater"

@router.post(f"{SWEATER_ROUTE}/insert", response_model=schemas.Sweater)
def create_sweater(sweater: schemas.SweaterCreate, db: Session = Depends(get_db)):
    return crud.create_sweater(db, sweater)


@router.get(f"{SWEATER_ROUTE}", response_model=List[schemas.Sweater])
def read_sweater(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coat = crud.get_sweater(db, skip=skip, limit=limit)
    return coat


@router.put(f"{SWEATER_ROUTE}/update/{{sweater_id}}", response_model=schemas.Sweater)
def update_coat(sweater: schemas.SweaterUpdate, sweater_id: int, db: Session = Depends(get_db)):
    sweater = crud.update_sweater(db, sweater_id, sweater)
    return sweater


@router.delete(f"{SWEATER_ROUTE}/delete/{{sweater_id}}")
def delete_sweater(sweater_id: int, db: Session = Depends(get_db)):
    response = crud.delete_sweater(db, sweater_id)
    return response
from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from database import get_db
from jumper import schemas, crud

router = APIRouter()

JUMPER_ROUTE = "/jumper"

@router.post(f"{JUMPER_ROUTE}/insert", response_model=schemas.Jumper)
def create_jumper(jumper: schemas.JumperCreate, db: Session = Depends(get_db)):
    return crud.create_jumper(db, jumper)


@router.get(f"{JUMPER_ROUTE}", response_model=List[schemas.Jumper])
def read_jumper(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jumper = crud.get_jumper(db, skip=skip, limit=limit)
    return jumper


@router.put(f"{JUMPER_ROUTE}/update/{{jumper_id}}", response_model=schemas.Jumper)
def update_jumper(jumper: schemas.JumperUpdate, jumper_id: int, db: Session = Depends(get_db)):
    jumper = crud.update_jumper(db, jumper_id, jumper)
    return jumper


@router.delete(f"{JUMPER_ROUTE}/delete/{{jumper_id}}")
def delete_jumper(jumper_id: int, db: Session = Depends(get_db)):
    response = crud.delete_jumper(db, jumper_id)
    return response
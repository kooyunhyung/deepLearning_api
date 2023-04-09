from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from database import get_db
from coat import schemas, crud

router = APIRouter()

COAT_ROUTE = "/coat"

@router.post(f"{COAT_ROUTE}/insert", response_model=schemas.Coat)
def create_coat(coat: schemas.CoatCreate, db: Session = Depends(get_db)):
    return crud.create_coat(db, coat)


@router.get(f"{COAT_ROUTE}", response_model=List[schemas.Coat])
def read_coat(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coat = crud.get_coat(db, skip=skip, limit=limit)
    return coat


@router.put(f"{COAT_ROUTE}/update/{{coat_id}}", response_model=schemas.Coat)
def update_coat(coat: schemas.CoatUpdate, coat_id: int, db: Session = Depends(get_db)):
    coat = crud.update_coat(db, coat_id, coat)
    return coat


@router.delete(f"{COAT_ROUTE}/delete/{{coat_id}}")
def delete_coat(coat_id: int, db: Session = Depends(get_db)):
    response = crud.delete_coat(db, coat_id)
    return response
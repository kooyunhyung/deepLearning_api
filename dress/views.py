from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from database import get_db
from dress import schemas, crud

router = APIRouter()

DRESS_ROUTE = "/dress"

@router.post(f"{DRESS_ROUTE}/insert", response_model=schemas.Dress)
def create_dress(dress: schemas.DressCreate, db: Session = Depends(get_db)):
    return crud.create_dress(db, dress)


@router.get(f"{DRESS_ROUTE}", response_model=List[schemas.Dress])
def read_dress(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dress = crud.get_dress(db, skip=skip, limit=limit)
    return dress


@router.put(f"{DRESS_ROUTE}/update/{{dress_id}}", response_model=schemas.Dress)
def update_dress(dress: schemas.DressUpdate, dress_id: int, db: Session = Depends(get_db)):
    dress = crud.update_dress(db, dress_id, dress)
    return dress


@router.delete(f"{DRESS_ROUTE}/delete/{{dress_id}}")
def delete_dress(dress_id: int, db: Session = Depends(get_db)):
    response = crud.delete_dress(db, dress_id)
    return response
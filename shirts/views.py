from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from database import get_db
from shirts import schemas, crud

router = APIRouter()

SHIRTS_ROUTE = "/shirts"

@router.post(f"{SHIRTS_ROUTE}/insert", response_model=schemas.Shirts)
def create_shirts(shirts: schemas.Shirts, db: Session = Depends(get_db)):
    return crud.create_shirts(db, shirts)


@router.get(f"{SHIRTS_ROUTE}", response_model=List[schemas.Shirts])
def read_shirts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shirts = crud.get_shirts(db, skip=skip, limit=limit)
    return shirts


@router.put(f"{SHIRTS_ROUTE}/update/{{shirts_id}}", response_model=schemas.Shirts)
def update_shirts(shirts: schemas.ShirtsUpdate, shirts_id: int, db: Session = Depends(get_db)):
    shirts = crud.update_shirts(db, shirts_id, shirts)
    return shirts


@router.delete(f"{SHIRTS_ROUTE}/delete/{{shirts_id}}")
def delete_shirts(shirts_id: int, db: Session = Depends(get_db)):
    response = crud.delete_shirts(db, shirts_id)
    return response
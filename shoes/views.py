from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from shoes import schemas, crud

router = APIRouter()

SHOES_ROUTE = "/shoes"

@router.post(f"{SHOES_ROUTE}/insert", response_model=schemas.Shoes)
def create_shoes(shoes: schemas.Shoes, db: Session = Depends(get_db)):
    return crud.create_shoes(db, shoes)


@router.get(f"{SHOES_ROUTE}", response_model=List[schemas.Shoes])
def read_shoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shoes = crud.get_shoes(db, skip=skip, limit=limit)
    return shoes


@router.put(f"{SHOES_ROUTE}/update/{{shoes_id}}", response_model=schemas.Shoes)
def update_shoes(shoes: schemas.ShoesUpdate, shoes_id: int, db: Session = Depends(get_db)):
    shoes = crud.update_shoes(db, shoes_id, shoes)
    return shoes


@router.delete(f"{SHOES_ROUTE}/delete/{{shoes_id}}")
def delete_shoes(shoes_id: int, db: Session = Depends(get_db)):
    response = crud.delete_shoes(db, shoes_id)
    return response
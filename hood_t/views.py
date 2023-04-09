from fastapi import APIRouter, Depends
from typing import List

from sqlalchemy.orm import Session

from database import get_db
from hood_t import schemas, crud

router = APIRouter()

HOODT_ROUTE = "/hood-t"

@router.post(f"{HOODT_ROUTE}/insert", response_model=schemas.HoodT)
def create_hood_t(hood_t: schemas.HoodTCreate, db: Session = Depends(get_db)):
    return crud.create_hood_t(db, hood_t)


@router.get(f"{HOODT_ROUTE}", response_model=List[schemas.HoodT])
def read_hood_t(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coat = crud.get_hood_t(db, skip=skip, limit=limit)
    return coat


@router.put(f"{HOODT_ROUTE}/update/{{hood_t_id}}", response_model=schemas.HoodT)
def update_hood_t(hood_t: schemas.HoodTUpdate, hood_t_id: int, db: Session = Depends(get_db)):
    hood_t = crud.update_hood_t(db, hood_t_id, hood_t)
    return hood_t


@router.delete(f"{HOODT_ROUTE}/delete/{{hood_t_id}}")
def delete_coat(hood_t_id: int, db: Session = Depends(get_db)):
    response = crud.delete_hood_t(db, hood_t_id)
    return response
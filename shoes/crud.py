from sqlalchemy.orm import Session
from fastapi import HTTPException

import shoes.models as models
import shoes.schemas as schemas


def get_shoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_shoes(db: Session, shoes: schemas.ShoesCreate):
    db_shoes = models.Test(img_file=shoes.img_file, label=shoes.label)
    db.add(db_shoes)
    db.commit()
    db.refresh(db_shoes)
    return db_shoes


def update_shoes(db: Session, shoes_id: int, shoes: schemas.Shoes):
    db_shoes = db.query(models.Test).filter(models.Test.id == shoes_id).first()
    if db_shoes:
        db_shoes.img_file = shoes.img_file if shoes.img_file is not None else db_shoes.img_file
        db_shoes.label = shoes.label if shoes.label is not None else db_shoes.label
        db.commit()
        db.refresh(db_shoes)
        return db_shoes
    else:
        raise HTTPException(status_code=404, detail="Student not found")


def delete_shoes(db: Session, shoes_id: int):
    db_shoes = db.query(models.Test).filter(models.Test.id == shoes_id).first()
    if db_shoes:
        db.delete(db_shoes)
        db.commit()
        return {"message": "Shoes deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Shoes not found")


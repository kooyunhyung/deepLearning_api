from sqlalchemy.orm import Session
from fastapi import HTTPException

import shirts.models as models
import shirts.schemas as schemas


def get_shirts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_shirts(db: Session, shirts: schemas.Shirts):
    db_shirts = models.Test(img_file=shirts.img_file, label=shirts.label)
    db.add(db_shirts)
    db.commit()
    db.refresh(db_shirts)
    return db_shirts


def update_shirts(db: Session, shirts_id: int, shirts: schemas.Shirts):
    db_shirts = db.query(models.Test).filter(models.Test.id == shirts_id).first()
    if db_shirts:
        db_shirts.img_file = shirts.img_file if shirts.img_file is not None else db_shirts.img_file
        db_shirts.label = shirts.label if shirts.label is not None else db_shirts.label
        db.commit()
        db.refresh(db_shirts)
        return db_shirts
    else:
        raise HTTPException(status_code=404, detail="Shirts not found")


def delete_shirts(db: Session, shirts_id: int):
    db_shirts = db.query(models.Test).filter(models.Test.id == shirts_id).first()
    if db_shirts:
        db.delete(db_shirts)
        db.commit()
        return {"message": "Shirts deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Shirts not found")


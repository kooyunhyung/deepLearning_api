from sqlalchemy.orm import Session
from fastapi import HTTPException

import dress.models as models
import dress.schemas as schemas


def get_dress(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_dress(db: Session, dress: schemas.Dress):
    db_dress = models.Test(img_file=dress.img_file, label=dress.label)
    db.add(db_dress)
    db.commit()
    db.refresh(db_dress)
    return db_dress


def update_dress(db: Session, dress_id: int, dress: schemas.Dress):
    db_dress = db.query(models.Test).filter(models.Test.id == dress_id).first()
    if db_dress:
        db_dress.img_file = dress.img_file if dress.img_file is not None else db_dress.img_file
        db_dress.label = dress.label if dress.label is not None else db_dress.label
        db.commit()
        db.refresh(db_dress)
        return db_dress
    else:
        raise HTTPException(status_code=404, detail="Dress not found")


def delete_dress(db: Session, dress_id: int):
    db_dress = db.query(models.Test).filter(models.Test.id == dress_id).first()
    if db_dress:
        db.delete(db_dress)
        db.commit()
        return {"message": "Dress deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Dress not found")


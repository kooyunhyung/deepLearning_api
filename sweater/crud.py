from sqlalchemy.orm import Session
from fastapi import HTTPException

import sweater.models as models
import sweater.schemas as schemas


def get_sweater(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_sweater(db: Session, sweater: schemas.Sweater):
    db_sweater = models.Test(img_file=sweater.img_file, label=sweater.label)
    db.add(db_sweater)
    db.commit()
    db.refresh(db_sweater)
    return db_sweater


def update_sweater(db: Session, sweater_id: int, sweater: schemas.Sweater):
    db_sweater = db.query(models.Test).filter(models.Test.id == sweater_id).first()
    if db_sweater:
        db_sweater.img_file = sweater.img_file if sweater.img_file is not None else db_sweater.img_file
        db_sweater.label = sweater.label if sweater.label is not None else db_sweater.label
        db.commit()
        db.refresh(db_sweater)
        return db_sweater
    else:
        raise HTTPException(status_code=404, detail="Sweater not found")


def delete_sweater(db: Session, sweater_id: int):
    db_sweater = db.query(models.Test).filter(models.Test.id == sweater_id).first()
    if db_sweater:
        db.delete(db_sweater)
        db.commit()
        return {"message": "Sweater deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Sweater not found")


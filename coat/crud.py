from sqlalchemy.orm import Session
from fastapi import HTTPException

import coat.models as models
import coat.schemas as schemas


def get_coat(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_coat(db: Session, coat: schemas.Coat):
    db_coat = models.Test(img_file=coat.img_file, label=coat.label)
    db.add(db_coat)
    db.commit()
    db.refresh(db_coat)
    return db_coat


def update_coat(db: Session, coat_id: int, coat: schemas.Coat):
    db_coat = db.query(models.Test).filter(models.Test.id == coat_id).first()
    if db_coat:
        db_coat.img_file = coat.img_file if coat.img_file is not None else db_coat.img_file
        db_coat.label = coat.label if coat.label is not None else db_coat.label
        db.commit()
        db.refresh(db_coat)
        return db_coat
    else:
        raise HTTPException(status_code=404, detail="Coat not found")


def delete_coat(db: Session, coat_id: int):
    db_coat = db.query(models.Test).filter(models.Test.id == coat_id).first()
    if db_coat:
        db.delete(db_coat)
        db.commit()
        return {"message": "Coat deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Coat not found")


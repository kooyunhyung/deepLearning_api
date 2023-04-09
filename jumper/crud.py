from sqlalchemy.orm import Session
from fastapi import HTTPException

import jumper.models as models
import jumper.schemas as schemas


def get_jumper(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_jumper(db: Session, jumper: schemas.Jumper):
    db_jumper = models.Test(img_file=jumper.img_file, label=jumper.label)
    db.add(db_jumper)
    db.commit()
    db.refresh(db_jumper)
    return db_jumper


def update_jumper(db: Session, jumper_id: int, jumper: schemas.Jumper):
    db_jumper = db.query(models.Test).filter(models.Test.id == jumper_id).first()
    if db_jumper:
        db_jumper.img_file = jumper.img_file if jumper.img_file is not None else db_jumper.img_file
        db_jumper.label = jumper.label if jumper.label is not None else db_jumper.label
        db.commit()
        db.refresh(db_jumper)
        return db_jumper
    else:
        raise HTTPException(status_code=404, detail="Jumper not found")


def delete_jumper(db: Session, jumper_id: int):
    db_jumper = db.query(models.Test).filter(models.Test.id == jumper_id).first()
    if db_jumper:
        db.delete(db_jumper)
        db.commit()
        return {"message": "Jumper deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Jumper not found")


from sqlalchemy.orm import Session
from fastapi import HTTPException

import hood_t.models as models
import hood_t.schemas as schemas


def get_hood_t(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def create_hood_t(db: Session, hood_t: schemas.HoodT):
    db_hood_t = models.Test(img_file=hood_t.img_file, label=hood_t.label)
    db.add(db_hood_t)
    db.commit()
    db.refresh(db_hood_t)
    return db_hood_t


def update_hood_t(db: Session, hood_t_id: int, hood_t: schemas.HoodT):
    db_hood_t = db.query(models.Test).filter(models.Test.id == hood_t_id).first()
    if db_hood_t:
        db_hood_t.img_file = hood_t.img_file if hood_t.img_file is not None else db_hood_t.img_file
        db_hood_t.label = hood_t.label if hood_t.label is not None else db_hood_t.label
        db.commit()
        db.refresh(db_hood_t)
        return db_hood_t
    else:
        raise HTTPException(status_code=404, detail="Hood_t not found")


def delete_hood_t(db: Session, hood_t_id: int):
    db_hood_t = db.query(models.Test).filter(models.Test.id == hood_t_id).first()
    if db_hood_t:
        db.delete(db_hood_t)
        db.commit()
        return {"message": "Hood_t deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Hood_t not found")


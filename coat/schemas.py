from pydantic import BaseModel
from typing import Optional


class Coat(BaseModel):
    id: int
    img_file: str
    label: str

    class Config:
        orm_mode = True

class CoatCreate(BaseModel):
    img_file: str
    label: str

    class Config:
        orm_mode = True

class CoatUpdate(BaseModel):
    img_file: Optional[str] = None
    label: Optional[str] = None

    class Config:
        orm_mode = True



from pydantic import BaseModel
from typing import Optional


class Sweater(BaseModel):
    id: int
    img_file: str
    label: str

    class Config:
        orm_mode = True

class SweaterCreate(BaseModel):
    img_file: str
    label: str

    class Config:
        orm_mode = True

class SweaterUpdate(BaseModel):
    img_file: Optional[str] = None
    label: Optional[str] = None

    class Config:
        orm_mode = True



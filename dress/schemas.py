from pydantic import BaseModel
from typing import Optional


class Dress(BaseModel):
    id: int
    img_file: str
    label: str

    class Config:
        orm_mode = True

class DressCreate(BaseModel):
    img_file: str
    label: str

    class Config:
        orm_mode = True

class DressUpdate(BaseModel):
    img_file: Optional[str] = None
    label: Optional[str] = None

    class Config:
        orm_mode = True



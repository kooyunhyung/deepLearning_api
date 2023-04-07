from pydantic import BaseModel
from typing import Optional


class Shoes(BaseModel):
    id: int
    img_file: str
    label: str

    class Config:
        orm_mode = True

class ShoesCreate(BaseModel):
    img_file: str
    label: str

    class Config:
        orm_mode = True

class ShoesUpdate(BaseModel):
    img_file: Optional[str] = None
    label: Optional[str] = None

    class Config:
        orm_mode = True



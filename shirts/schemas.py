from pydantic import BaseModel
from typing import Optional


class Shirts(BaseModel):
    id: int
    img_file: str
    label: str

    class Config:
        orm_mode = True

class ShirtsCreate(BaseModel):
    img_file: str
    label: str

    class Config:
        orm_mode = True

class ShirtsUpdate(BaseModel):
    img_file: Optional[str] = None
    label: Optional[str] = None

    class Config:
        orm_mode = True



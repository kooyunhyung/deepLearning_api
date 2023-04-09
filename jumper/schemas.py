from pydantic import BaseModel
from typing import Optional


class Jumper(BaseModel):
    id: int
    img_file: str
    label: str

    class Config:
        orm_mode = True

class JumperCreate(BaseModel):
    img_file: str
    label: str

    class Config:
        orm_mode = True

class JumperUpdate(BaseModel):
    img_file: Optional[str] = None
    label: Optional[str] = None

    class Config:
        orm_mode = True



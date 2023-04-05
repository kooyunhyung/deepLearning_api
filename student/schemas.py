from pydantic import BaseModel
from typing import Optional


class Shirts(BaseModel):
    name: str
    dept_name: str
    tot_cred: int

    class Config:
        orm_mode = True

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    dept_name: Optional[str] = None
    tot_cred: Optional[int] = None

    class Config:
        orm_mode = True



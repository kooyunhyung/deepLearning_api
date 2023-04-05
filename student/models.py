from sqlalchemy import Column, TEXT, INT, BIGINT
from database import Base


class Test(Base):
    __tablename__ = "student"

    id = Column(BIGINT, nullable=False, primary_key=True, autoincrement=True, default=1)
    name = Column(TEXT, nullable=False, unique=True)
    dept_name = Column(TEXT, nullable=False)
    tot_cred = Column(INT, nullable=False)

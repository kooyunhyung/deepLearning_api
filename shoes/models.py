from sqlalchemy import Column, TEXT, INT, BIGINT
from database import Base


class Test(Base):
    __tablename__ = "shoes"

    id = Column(BIGINT, nullable=False, primary_key=True, autoincrement=True, default=1)
    img_file = Column(TEXT, nullable=False, unique=True)
    label = Column(TEXT, nullable=False)
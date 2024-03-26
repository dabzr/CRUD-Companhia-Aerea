from sqlalchemy import Integer, Column
from infra.configs import Base
from abc import ABC

class Aviao(ABC, Base):

    __tablename__ = "aviao"

    id = Column(Integer, primary_key=True)

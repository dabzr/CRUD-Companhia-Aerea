from sqlalchemy import Column, String
from infra.configs import Base

class Aeroporto(Base):

    __tablename__ = "aeroporto"

    id = Column(Integer, primary_key=True)
    nome = Column(String)

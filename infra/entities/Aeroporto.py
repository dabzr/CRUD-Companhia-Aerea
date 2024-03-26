from infra.configs import Base
from sqlalchemy import Column, Integer, String

class Aeroporto(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String)

from sqlalchemy import Column, Integer
from infra.entities.Aviao import Aviao
from infra.configs import Base

class Embraer(Base):

    __tablename__ = "embraer"

    id = Column(Integer, primary_key = True)
    quantidade_de_assentos = Column(Integer, default = 44)


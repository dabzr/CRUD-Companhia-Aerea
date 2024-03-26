from sqlalchemy import Column, Integer
from infra.entities.Aviao import Aviao

class Embraer(Aviao):

    __tablename__ = "embraer"

    id = Column(Integer, primary_key = True)
    quantidade_de_assentos = Column(Integer, default = 44)


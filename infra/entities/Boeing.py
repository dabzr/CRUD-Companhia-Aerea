from sqlalchemy import Column, Integer
from infra.entities.Aviao import Aviao

class Boeing(Aviao):

    __tablename__ = "boeing"

    id = Column(Integer, primary_key = True)
    quantidade_de_assentos = Column(Integer, default = 189)

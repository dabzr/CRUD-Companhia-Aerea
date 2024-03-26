from sqlalchemy import Column, Integer
from infra.entities.Aviao import Aviao

class Airbus(Aviao):

    __tablename__ = "airbus"

    id = Column(Integer, primary_key=True)
    quantidade_de_assentos = Columns(Integer, default = 280)



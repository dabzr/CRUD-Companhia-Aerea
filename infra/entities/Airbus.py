from sqlalchemy import Column, Integer
from infra.entities.Aviao import Aviao
from infra.configs import Base

class Airbus(Base):

    __tablename__ = "airbus"

    id = Column(Integer, primary_key=True)
    quantidade_de_assentos = Columns(Integer, default = 280)



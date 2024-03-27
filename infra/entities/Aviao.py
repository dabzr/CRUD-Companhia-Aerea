from sqlalchemy import String, Integer, Column
from infra.configs import Base

class Aviao(Base):

    __tablename__ = "aviao"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    quantidade_de_assentos = Column(Integer)


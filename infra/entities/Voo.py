from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from ..entities.Aeroporto import Aeroporto
from sqlalchemy.orm import relationship
from ..entities.Aviao import Aviao
from ..configs.base import Base

class Voo(Base):

    __tablename__ = "voo"

    id = Column(Integer, primary_key=True)
    id_aeroporto_de_saida = Column(Integer, ForeignKey('aeroporto.id'))
    id_aeroporto_de_chegada =  Column(Integer, ForeignKey('aeroporto.id')) 
    horario = Column(DateTime)
    id_aviao = Column(Integer, ForeignKey('aviao.id')) 
    
    aeroporto_de_saida = relationship("Aeroporto", back_populates="voo")
    aeroporto_de_chegada = relationship("Aeroporto", back_populates="voo")
    aviao = relationship("Aviao", back_populates="voo")

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())


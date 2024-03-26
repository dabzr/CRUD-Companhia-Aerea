from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from infra.entities.Aeroporto import Aeroporto
from infra.entities.Aviao import Aviao
from infra.configs import Base

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

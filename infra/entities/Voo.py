from infra.entities import Aeroporto, Aviao
from typing import Type
from datetime import datetime 
from infra.configs import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

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

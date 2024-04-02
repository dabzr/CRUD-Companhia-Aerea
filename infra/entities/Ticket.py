import sys
sys.path.append('../..')

from infra.entities.Passageiro import Passageiro
from infra.entities.Assento import Assento
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from infra.entities.Voo import Voo
from infra.configs.base import Base

class Ticket(Base):
    
    __tablename__ = "ticket"

    id = Column(Integer, primary_key = True)
    id_assento = Column(Integer, ForeignKey('assento.id'))
    assento = relationship("Assento", back_populates="ticket")
    id_voo = Column(Integer, ForeignKey('voo.id'))
    voo = relationship("Voo", back_populates="ticket")
    id_passageiro = Column(Integer, ForeignKey('passageiro.id'))
    passageiro = relationship("Passageiro", back_populates="ticket")

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.clear
        Base.metadata.create_all(db.get_engine())


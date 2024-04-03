from ..entities.Passageiro import Passageiro
from ..entities.Assento import Assento
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..entities.Voo import Voo
from ..configs.base import Base, mapper_registry

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
        mapper_registry.configure()
        Base.metadata.clear
        Base.metadata.create_all(db.get_engine())


from infra.entities.Assento import Assento
from sqlalchemy import Column, ForeignKey
from infra.entities.Voo import Voo
from infra.configs import Base

class Ticket(Base):
    
    __tablename__ = "ticket"

    id = Column(Integer, primary_key = True)
    id_assento = Column(Integer, ForeignKey('assento.id'))
    assento = relationship("Assento", back_populates("ticket"))
    id_voo = Column(Integer, ForeignKey('voo.id'))
    voo = relationship("Voo", back_populates("ticket"))


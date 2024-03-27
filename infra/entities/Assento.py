from sqlalchemy import Column, Boolean, ForeignKey, String
from infra.entities.Aviao import Aviao
from infra.configs import Base

class Assento(Base):

    __tablename__ = "assento"

    id = Column(Integer, primary_key = True)
    assento_id = Column(String)
    id_aviao = Column(Integer, ForeignKey('aviao.id'))
    aviao = realtionship("Aviao", back_populates="assento")
    ocupado = Column(Boolean, default = False)

import sys
sys.path.append('../..')

from sqlalchemy import Column, Boolean, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from Aviao import Aviao
from infra.configs.base import Base

class Assento(Base):

    __tablename__ = "assento"

    id = Column(Integer, primary_key = True)
    assento_id = Column(String(50))
    id_aviao = Column(Integer, ForeignKey('aviao.id'))
    aviao = relationship("Aviao", back_populates="assento")
    ocupado = Column(Boolean, default = False)

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())


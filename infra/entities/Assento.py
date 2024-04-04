from sqlalchemy import Column, Boolean, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from ..entities.Aviao import Aviao
from ..configs.base import Base, mapper_registry
#import sys
#sys.path.append('../..')
#from infra.configs.base import Base, mapper_registry    
#from infra.entities.Aviao import Aviao
 
#from infra.configs.connection import DBConnectionHandler 
class Assento(Base):

    __tablename__ = "assento"

    id = Column(Integer, primary_key = True)
    assento_id = Column(String(50))
    id_aviao = Column(Integer, ForeignKey('aviao.id'))
    aviao = relationship("Aviao", back_populates="assento")
    ticket = relationship("Ticket", back_populates="assento")
    ocupado = Column(Boolean, default = False)

if __name__ == "__main__":

    with DBConnectionHandler() as db:
        mapper_registry.configure()
        Base.metadata.create_all(db.get_engine())


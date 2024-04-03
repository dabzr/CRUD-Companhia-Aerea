from sqlalchemy import String, Integer, Column
from ..configs.base import Base, mapper_registry
from sqlalchemy.orm import relationship
class Aviao(Base):

    __tablename__ = "aviao"
   # __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    quantidade_de_assentos = Column(Integer)
    assento = relationship("Assento", back_populates="aviao")
    voo = relationship("Voo", back_populates="aviao")


if __name__ == "__main__":
    import sys
    sys.path.append('../..')
    from infra.configs.base import Base, mapper_registry
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        mapper_registry.configure()
        Base.metadata.clear()
        Base.metadata.create_all(db.get_engine())


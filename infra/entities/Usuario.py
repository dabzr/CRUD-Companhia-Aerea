import sys
sys.path.append('../..')

from sqlalchemy import Column, Integer, String, MetaData
from ..configs.base import Base, mapper_registry
from sqlalchemy.orm import relationship

class Usuario(Base):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key = True)
    user = Column(String(50))
    senha = Column(String(60))
    salt = Column(String(60))
    passageiro = relationship("Passageiro", back_populates="usuario")

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        mapper_registry.configure()
        metadata = MetaData()
        metadata.reflect(bind=db.get_engine())
        tabela = metadata.tables['usuario']
        if(tabela == 'usuario'):
            tabela.drop(db.get_engine())
        Base.metadata.create_all(db.get_engine())


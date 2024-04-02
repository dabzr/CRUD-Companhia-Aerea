import sys
sys.path.append('../..')

from sqlalchemy import Column, Integer, String, MetaData
from infra.configs.base import Base

class Usuario(Base):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key = True)
    user = Column(String(50))
    senha = Column(String(60))
    salt = Column(String(60))

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        metadata = MetaData()
        metadata.reflect(bind=db.get_engine())
        tabela = metadata.tables['usuario']
        if(tabela == 'usuario'):
            tabela.drop(db.get_engine())
        Base.metadata.create_all(db.get_engine())


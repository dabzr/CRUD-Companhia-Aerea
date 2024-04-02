import sys
sys.path.append('../..')

from sqlalchemy import String, Integer, Column
from infra.configs.base import Base

class Aviao(Base):

    __tablename__ = "aviao"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    quantidade_de_assentos = Column(Integer)

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.clear()
        Base.metadata.create_all(db.get_engine())


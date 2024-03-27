import sys
sys.path.append('../..')

from sqlalchemy import Column, Integer, String
from infra.configs.base import Base

class Usuario(Base):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key = True)
    user = Column(String(50))
    senha = Column(String(50))

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())


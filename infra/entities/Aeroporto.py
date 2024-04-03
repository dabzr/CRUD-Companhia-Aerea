from sqlalchemy import Column, String, Integer
from ..configs.base import Base

class Aeroporto(Base):

    __tablename__ = "aeroporto"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())


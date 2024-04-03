from sqlalchemy import Column, String, Integer
from ..configs.base import Base, mapper_registry
from sqlalchemy.orm import relationship

class Aeroporto(Base):

    __tablename__ = "aeroporto"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    voo_saida = relationship("Voo", foreign_keys="[Voo.id_aeroporto_de_saida]")
    voo_chegada = relationship("Voo", foreign_keys="[Voo.id_aeroporto_de_chegada]")

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        mapper_registry.configure()
        Base.metadata.create_all(db.get_engine())


from sqlalchemy import String, Integer, ForeignKey, Column
from ..entities.Usuario import Usuario
from ..configs.base import Base, mapper_registry
from sqlalchemy.orm import relationship

class Passageiro(Base):

    __tablename__ = "passageiro"

    id = Column(Integer, primary_key = True)
    nome = Column(String(50))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="passageiro")
    ticket = relationship("Ticket", back_populates="passageiro")

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        mapper_registry.configure()
        Base.metadata.create_all(db.get_engine())


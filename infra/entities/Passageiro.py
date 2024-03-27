import sys
sys.path.append('../..')

from sqlalchemy import String, Integer, ForeignKey, Column
from infra.entities.Usuario import Usuario
from infra.configs.base import Base
from sqlalchemy.orm import relationship
class Passageiro(Base):

    __tablename__ = "passageiro"

    id = Column(Integer, primary_key = True)
    nome = Column(String(50))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="passageiro")

if __name__ == "__main__":
    from infra.configs.connection import DBConnectionHandler 
    with DBConnectionHandler() as db:
        Base.metadata.create_all(db.get_engine())


from sqlalchemy import String, Integer, ForeignKey
from infra.entities.Usuario import Usuario
from infra.configs import Base

class Passageiro(Base):

    __tablename__ = "passageiro"

    id = Column(Integer, primary_key = True)
    nome = Column(String)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship("Usuario", back_populates="passageiro")

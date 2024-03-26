from sqlalchemy import Column, Integer, String
from infra.configs import Base

class Usuario(Base):

    __tablename__ = "usuario"

    id = Column(Integer, primary_key = True)
    user = Column(String)
    senha = Column(String)


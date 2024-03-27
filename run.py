"""from infra.entities.Usuario import Usuario
from infra.repository.user_repository import UserRepository
cond = input("Você deseja logar ou criar usuário?[1/2] ")
user = input("Digite seu usuário: ")
senha = input("Digite sua senha:")
if(cond != 1):
    print("Criando usuário...")
    repo = UserRepository()
    repo.insert(user, senha) 
else:

"""

from sqlalchemy import MetaData
from infra.entities import *
from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler 
with DBConnectionHandler() as db:
    Base.metadata.create_all(db.get_engine())

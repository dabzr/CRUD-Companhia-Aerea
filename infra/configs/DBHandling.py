from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base
class DBHandling:
    def __init__(self, dbstring):
        self.engine = create_engine(dbstring)

a = 'mysql+pymysql://root:senha@localhost:3306/bancoaviao'

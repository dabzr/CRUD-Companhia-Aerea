from infra.configs.connection import DBConnectionHandler
from infra.entities.Voo import Voo
frominfra.entities.Aviao import Aviao
from infra.entities.Aeroporto import Aeroporto
from typing import Type
from datetime import datetime

class VooRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Voo).all()
            return data

    def insert(self, aviao:Type[Aviao], aeroporto_de_chegada:Type[Aeroporto], aeroporto_de_saida:Type[Aeroporto], horario:datetime):
        with DBConnectionHandler() as db:
            data_insert = Voo(id_aviao=aviao.id, id_aeroporto_de_chegada=aeroporto_de_chegada.id, id_aeroporto_de_saida=aeroporto_de_saida.id, horario=horario)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Voo).filter(Voo.id == id).delete()
            db.session.commit()

    def update_horario(self, id, horario:datetime):
        with DBConnectionHandler() as db:
            data = db.session.query(Voo).filter(Voo.id == id).update(horario = horario)
            db.session.commit()







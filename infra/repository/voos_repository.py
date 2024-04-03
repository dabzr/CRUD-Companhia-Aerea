from ..configs.connection import DBConnectionHandler
from ..entities.Voo import Voo
from ..entities.Aviao import Aviao
from ..entities.Aeroporto import Aeroporto
from typing import Type
from datetime import datetime

class VooRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
                .query(Voo, Aeroporto)\
                .join(Voo, Aeroporto.id == Voo.id_aeroporto_de_saida, Aeroporto.id == Voo.id_aeroporto_de_chegada)\
                .with_entities(Voo.horario, Aeroporto.nome, Aeroporto.nome)\
                .all()
            return data

    def insert(self, aviao:Type[Aviao], aeroporto_de_chegada:Type[Aeroporto], aeroporto_de_saida:Type[Aeroporto], horario:datetime):
        with DBConnectionHandler() as db:
            try:
                data_insert = Voo(id_aviao=aviao.id, 
                                  id_aeroporto_de_chegada=aeroporto_de_chegada.id, 
                                  id_aeroporto_de_saida=aeroporto_de_saida.id, 
                                  horario=horario)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Voo).filter(Voo.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def update_horario(self, id, horario: Type[datetime]):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Voo).filter(Voo.id == id).update(horario = horario)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

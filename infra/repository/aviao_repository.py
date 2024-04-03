from ..configs.connection import DBConnectionHandler
from ..entities.Aviao import Aviao
from typing import Type

class AviaoRepository:

    def select(self) -> Type[DBConnectionHandler]:
        with DBConnectionHandler() as db:
            data = db.session.query(Aviao).all()
        return data

    def insert(self, nome: str, quantidade_de_assentos: int) -> None:
        with DBConnectionHandler() as db:
            try:
                data_insert = Aviao(nome = nome, 
                        quantidade_de_assentos = quantidade_de_assentos)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Aviao).filter(Aviao.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()

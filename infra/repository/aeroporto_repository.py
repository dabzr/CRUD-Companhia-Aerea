from ..configs.connection import DBConnectionHandler
from ..entities.Aeroporto import Aeroporto

class AeroportoRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Aeroporto).all()
            return data

    def insert(self, nome):
        with DBConnectionHandler() as db:
            try:
                data_insert = Aeroporto(nome=nome)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def delete(self, nome):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Aeroporto).filter(Aeroporto.nome == nome).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def update_nome(self, nome):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Aeroporto).filter(Aeroporto.nome == nome).update(nome=nome)
                db.session.commit()
            except Exception as e:
                db.session.rollback()



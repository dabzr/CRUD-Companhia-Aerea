from infra.configs.connection import DBConnectionHandler
from infra.entities.Passageiro import Passageiro

class PassageiroRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
            .query(Passageiro, Usuario)\
            .with_entities(Passageiro.nome,
                           Usuario.user,
                           Usuario.senha)\
            .all()
            return data

    def insert(self, nome):
        with DBConnectionHandler() as db:
            data_insert = Passageiro(nome=nome)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, nome):
        with DBConnectionHandler() as db:
            data = db.session.query(Passageiro).filter(Passageiro.nome == nome).delete()
            db.session.commit()

    def update_nome(self, nome):
        with DBConnectionHandler() as db:
            data = db.session.query(Passageiro).filter(Passageiro.nome == nome).update(nome=nome)
            db.session.commit()

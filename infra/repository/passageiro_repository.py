from infra.configs.connection import DBConnectionHandler
from infra.entities.Passageiro import Passageiro
from infra.entities.Usuario import Usuario
from typing import Type

class PassageiroRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
            .query(Passageiro, Usuario)\
            .join(Passageiro, Usuario.id == Passageiro.id_usuario)
            .with_entities(Passageiro.nome,
                           Usuario.user,
                           Usuario.senha)\
            .all()
            return data

    def insert(self, nome, usuario:Type[Usuario]):
        with DBConnectionHandler() as db:
            try:
                data_insert = Passageiro(nome=nome,
                                         id_usuario=usuario.id)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def delete(self, nome):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Passageiro).filter(Passageiro.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()

    def update_nome(self, nome):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Passageiro).filter(Passageiro.id == id).update(nome=nome)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

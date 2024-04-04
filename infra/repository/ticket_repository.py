from ..configs.connection import DBConnectionHandler
from ..entities.Ticket import Ticket
from ..entities.Assento import Assento
from ..entities.Passageiro import Passageiro
from ..entities.Voo import Voo
from typing import Type

class TicketRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
            .query(Ticket)\
            .all()
            return data

    def insert(self, passageiro:Type[Passageiro], assento:Type[Assento], voo:Type[Voo]): 
        with DBConnectionHandler() as db:
            try:
                data_insert = Ticket(id_passageiro = passeiro.id,
                                     id_assento = assento.id,
                                     id_voo = voo.id)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Ticket).filter(Ticket.id == id).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()

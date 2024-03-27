from infra.configs.connection import DBConnectionHandler
from infra.entities.Ticket import Ticket
from infra.entities.Assento import Assento
from infra.entities.Passageiro import Passageiro
from infra.entities.Voo import Voo

class TicketRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
            .query(Ticket, Passageiro, Assento, Voo)\
            .join(Ticket, Passageiro.id == Ticket.id_passageiro, Assento.id == Ticket.id_assento, Voo.id == Ticket.id_voo)\
            .with_entities(Ticket.id,
                           Passageiro.nome,
                           Assento.ocupado,
                           Assento.assento_id,
                           Voo.horario)\
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

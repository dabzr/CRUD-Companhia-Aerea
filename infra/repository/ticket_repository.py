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
            .with_entities(Ticket.id,
                           Passageiro.nome,
                           Assento.ocupado,
                           Assento.assento_id,
                           Voo.horario)\
            .all()
            return data

    def insert(self, passageiro:Type[Passageiro], assento:Type[Assento], voo:Type[Voo]):
        with DBConnectionHandler() as db:
            data_insert = Ticket(id_passageiro = passeiro.id,
                                 id_assento = assento.id,
                                 id_voo = voo.id
                                 )
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Ticket).filter(Ticket.id == id).delete()
            db.session.commit()

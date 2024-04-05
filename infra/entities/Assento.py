from ..entities.Aviao import Aviao
from __main__ import db

class Assento(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    assento_id = db.Column(db.String(50), nullable=False)
    id_aviao = Column(db.Integer, db.ForeignKey('aviao.id'))
    aviao = db.relationship("Aviao", back_populates="assento")
    ticket = db.relationship("Ticket", back_populates="assento")
    ocupado = db.Column(Boolean, default = False)

    def __repr__(self):
        return f"Assento('{self.aviao}', '{self.ocupado}')"




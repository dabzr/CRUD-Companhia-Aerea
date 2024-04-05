from __main__ import db
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_assento = db.Column(db.Integer, db.ForeignKey('assento.id'))
    assento = db.relationship("Assento", back_populates="ticket")
    id_voo = db.Column(db.Integer, db.ForeignKey('voo.id'))
    voo = db.relationship("Voo", back_populates="ticket")
    id_passageiro = db.Column(db.Integer, db.ForeignKey('passageiro.id'))
    passageiro = db.relationship("Passageiro", back_populates="ticket")
    
    def __repr__(self):
        return f"Ticket('{self.assento}', '{self.voo}', '{self.passageiro}')"




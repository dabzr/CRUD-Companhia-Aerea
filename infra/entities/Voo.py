from __main__ import db
class Voo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_aeroporto_de_saida = db.Column(db.Integer, db.ForeignKey('aeroporto.id'))
    id_aeroporto_de_chegada =  db.Column(db.Integer, db.ForeignKey('aeroporto.id')) 
    horario = db.Column(db.DateTime, nullable=False)
    id_aviao = db.Column(db.Integer, db.ForeignKey('aviao.id')) 
    aviao = db.relationship("Aviao", back_populates="voo")
    ticket = db.relationship("Ticket", back_populates="voo")
    aeroporto_de_saida = db.relationship("Aeroporto", back_populates="voo")

    def __repr__(self):
        return f"Voo('{self.aviao}', '{self.horario}', '{self.voo_chegada}')"



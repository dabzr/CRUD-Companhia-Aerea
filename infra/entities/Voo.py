from ...app import db

association_table = db.Table('association',
    db.Column('aeroporto_id', db.Integer, db.ForeignKey('aeroporto.id')),
    db.Column('voo_id', db.Integer, db.ForeignKey('voo.id'))
)

class Voo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.DateTime, nullable=False)
    id_aviao = db.Column(db.Integer, db.ForeignKey('aviao.id')) 
    aviao = db.relationship("Aviao", back_populates="voo")
    ticket = db.relationship("Ticket", back_populates="voo")
    aeroporto_saida_id = db.Column(db.Integer, db.ForeignKey('aeroporto.id'))
    aeroporto_chegada_id = db.Column(db.Integer, db.ForeignKey('aeroporto.id'))
    def __repr__(self):
        return f"Voo('{self.aviao}', '{self.horario}', '{self.voo_chegada}')"



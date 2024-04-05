from ...app import db 

class Aeroporto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    voos_de_saida = db.relationship("Voo", foreign_keys="[Voo.aeroporto_saida_id]", backref="aeroporto_de_saida", lazy=True)
    voos_de_chegada = db.relationship("Voo", foreign_keys="[Voo.aeroporto_chegada_id]", backref="aeroporto_de_chegada", lazy=True)
 
    def __repr__(self):
        return f"Aeroporto('{self.nome}')"



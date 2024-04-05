from __main__ import db 

class Aeroporto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    voo_saida = db.relationship("Voo", foreign_keys="[Voo.id_aeroporto_de_saida]", nullable=False, lazy=True)
    voo_chegada = db.relationship("Voo", foreign_keys="[Voo.id_aeroporto_de_chegada]", nullable=False, lazy=True, )

    def __repr__(self):
        return f"Aeroporto('{self.nome}')"



from __main__ import db
class Aviao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    quantidade_de_assentos = db.Column(db.Integer)
    assento = db.relationship("Assento", back_populates="aviao")
    voo = db.relationship("Voo", back_populates="aviao")
    def __repr__(self):
        return f"Aviao('{self.nome}', '{self.quantidade_de_assentos}')"




from __main__ import db
class Passageiro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    id_usuario = db.Column(Integer, ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", back_populates="passageiro")
    ticket = db.relationship("Ticket", back_populates="passageiro")
    def __repr__(self):
        return f"Passageiro('{self.nome}', '{self.usuario}')"



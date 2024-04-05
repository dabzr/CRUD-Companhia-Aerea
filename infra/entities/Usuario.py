from ...app import db
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)
    salt = db.Column(db.String(60), nullable=False)
    passageiro = db.relationship("Passageiro", back_populates="usuario")
    def __repr__(self):
        return f"Usuario('{self.user}')"



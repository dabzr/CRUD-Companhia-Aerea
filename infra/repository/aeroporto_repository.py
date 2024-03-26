
class AeroportoRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Aeroporto).all()
            return data

    def insert(self, nome):
        with DBConnectionHandler() as db:
            data_insert = Aeroporto(nome=nome)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, nome):
        with DBConnectionHandler() as db:
            data = db.session.query(Aeroporto).filter(Aeroporto.nome == nome).delete()
            db.session.commit()



from infra.configs.connection import DBConnectionHandler
from infra.entities.User import User
from infra.entities.password import create_hash_password
class UserRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(User).all()
            return data

    def insert(self, user, password):
        hashed_password = create_hash_password(password)
        with DBConnectionHandler() as db:
            data_insert = User(user=user, senha=hashed_password)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, user):
        with DBConnectionHandler() as db:
            data = db.session.query(User).filter(User.user == user).delete()
            db.session.commit()

    def update_user(self, user):
        with DBConnectionHandler() as db:
            data = db.session.query(User).filter(User.user == user).update(user=user)
            db.session.commit()
    
    def update_senha(self, senha):
        hashed_password = create_hash_password(senha)
        with DBConnectionHandler() as db:
            data = db.session.query(User).filter(User.user == user).update(senha=hashed_password)
            db.session.commit()


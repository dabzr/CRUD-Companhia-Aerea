from infra.configs.connection import DBConnectionHandler
from infra.entities.User import User
from infra.repository.password import create_hash_password
class UserRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(User).all()
            return data

    def insert(self, user, password):
        hashed_password = create_hash_password(password)
        with DBConnectionHandler() as db:
            try:
                data_insert = User(user=user, senha=hashed_password)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

    def delete(self, user):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(User).filter(User.user == user).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def update_user(self, user):
        with DBConnectionHandler() as db:
            try:    
                data = db.session.query(User).filter(User.user == user).update(user=user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()


   
    def update_senha(self, senha):
        hashed_password = create_hash_password(senha)
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(User).filter(User.user == user).update(senha=hashed_password)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

                   


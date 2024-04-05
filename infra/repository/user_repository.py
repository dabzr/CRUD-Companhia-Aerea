from ..entities.Usuario import Usuario
from ...app import db
from ..repository.password import create_hash_password
class UserRepository:
    def insert(self, user, password):
        allusers = self.select()
        for i in allusers:
            if i.user == user:
                print("usuario ja existe")
                return
        hashed_password = create_hash_password(password)
            try:
                data_insert = Usuario(user=user, senha=hashed_password[0], salt=hashed_password[1])
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()

    def delete(self, user):
            try:
                data = db.session.query(Usuario).filter(Usuario.user == user).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def update_user(self, user):
            try:    
                data = db.session.query(Usuario).filter(Usuario.user == user).update(user=user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()

   
    def update_senha(self, senha):
        hashed_password = create_hash_password(senha)
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Usuario).filter(Usuario.user == user).update(senha=hashed_password[0], salt=hashed_password[1])
                db.session.commit()
            except Exception as e:
                db.session.rollback()


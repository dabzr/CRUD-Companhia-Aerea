from infra.configs.connection import DBConnectionHandler
from infra.entities.Usuario import Usuario
from infra.repository.password import create_hash_password
class UserRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Usuario).all()
            return data

    def insert(self, user, password):
        allusers = self.select()
        for i in allusers:
            if i.user == user:
                print("usuario ja existe")
                return
        hashed_password = create_hash_password(password)
        with DBConnectionHandler() as db:
            try:
                data_insert = Usuario(user=user, senha=hashed_password[0], salt=hashed_password[1])
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()

    def delete(self, user):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Usuario).filter(Usuario.user == user).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()


    def update_user(self, user):
        with DBConnectionHandler() as db:
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


from bcrypt import hashpw, gensalt, checkpw
import binascii                  
def verify_password(user, password):
    b = None
    repo = UserRepository()
    users = repo.select()
    for usuario in users:
        if usuario.user == user:
            b = usuario 
            break
    if b is None:
        return False
    
    bpassword = password.encode('utf-8')
    hashed_password = hashpw(bpassword, b.salt.encode('utf-8'))
    if hashed_password.decode('utf-8') == b.senha:
        return True
    return False



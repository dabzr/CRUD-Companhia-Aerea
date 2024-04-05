from bcrypt import hashpw, gensalt, checkpw
import binascii
from ..entities.Usuario import Usuario

def verify_password(usuario:Type[Usuario], password):
    bpassword = password.encode('utf-8')
    hashed_password = hashpw(bpassword, usuario.salt.encode('utf-8'))
    if hashed_password.decode('utf-8') == usuario.senha:
        return True
    return False

def create_hash_password(password):
    salt = gensalt(rounds=10)
    bpassword = password.encode('utf-8')
    hashed_password = hashpw(bpassword, salt)
    return hashed_password.decode('utf-8'), salt.decode('utf-8')

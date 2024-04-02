from bcrypt import hashpw, gensalt, checkpw
import binascii

def create_hash_password(password):
    salt = gensalt(rounds=10)
    bpassword = password.encode('utf-8')
    hashed_password = hashpw(bpassword, salt)
    return hashed_password.decode('utf-8'), salt.decode('utf-8')

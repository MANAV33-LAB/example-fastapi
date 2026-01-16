from passlib.context import CryptContext
hash_pw = CryptContext(schemes=['bcrypt'],deprecated = 'auto')
def hashi(password):
    return hash_pw.hash(password)

def verify(plain_pass,hashed_pass): #ek plain original hoga and sura hashed hoga
    return hash_pw.verify(plain_pass,hashed_pass)

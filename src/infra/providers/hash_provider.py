from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def generateHash(texto):
    return pwd_context.hash(texto)

def verifyHash(texto, hash):
    return pwd_context.verify(texto, hash)

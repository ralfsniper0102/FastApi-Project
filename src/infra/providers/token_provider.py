from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from jose import jwt

load_dotenv()

secretKey = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
expires = int(os.getenv("EXPIRES_IN_MIN"))

def createToken():
    exp = datetime.utcnow() + timedelta(minutes=expires)
    data = {
        'exp': exp
    }
    
    token_jwt = jwt.encode(data, secretKey, algorithm=algorithm)
    return token_jwt


def verifyToken(token: str):
    carga = jwt.decode(token, secretKey, algorithms=[algorithm])
    return carga.get('sub')

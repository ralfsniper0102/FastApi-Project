from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from jose import ExpiredSignatureError, JWTError, jwt

load_dotenv()

secretKey = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
expires = int(os.getenv("EXPIRES_IN_MIN"))

def createToken():
    exp = datetime.utcnow() + timedelta(minutes=expires)
    data = { 'exp': exp }
    
    token_jwt = jwt.encode(data, secretKey, algorithm=algorithm)
    return token_jwt

def verifyToken(token: str):
    try:
        carga = jwt.decode(token.replace("Bearer ", ""), secretKey, algorithms=[algorithm])
        return carga
    except ExpiredSignatureError:
        return False
    except JWTError:
        return False
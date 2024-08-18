from sqlalchemy import select
from sqlalchemy.orm import Session
from src.helpers.jwtHelper import createToken, verifyToken
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from passlib.context import CryptContext

bcrypt = CryptContext(schemes=['bcrypt'])

class RepositoryUser():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.UserCreateViewModel):
        userBD = models.User(name=user.name,
                                    email=user.email,
                                    password=user.password,
                                    birthDay=user.birthDay
                                    )
        
        try:
            userBD.password = bcrypt.hash(userBD.password)
        except Exception as e:
            print(f"Error hashing password: {str(e)}")
            
        self.session.add(userBD)
        self.session.commit()
        self.session.refresh(userBD)
        return userBD

    def listAll(self):
        query = select(models.User)
        users = self.session.execute(query).scalars().all()
        return users 

    def getByEmail(self, email) -> models.User:
        query = select(models.User).where(
            models.User.email == email)
        return self.session.execute(query).scalars().first()
    
    def searchById(self, id):
        query = select(models.User).where(models.User.id == id)
        user = self.session.execute(query).scalars().first()
        return user
    
    def checkPassword(self, email, password):
        user = self.getByEmail(email)
        if not user:
            return False
        if not bcrypt.verify(password, user.password):
            return False
        return createToken()
    
    def validToken(self, token):
        user = verifyToken(token)
        if not user:
            return False
        return True
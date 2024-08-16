from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositoryUser():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: schemas.UserCreate):
        usuario_bd = models.Usuario(nome=usuario.nome,
                                    email=usuario.email,
                                    senha=usuario.senha,
                                    nascimento=usuario.nascimento
                                    )
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd

    def listAll(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios 

    def getByEmail(self, email) -> models.Usuario:
        query = select(models.Usuario).where(
            models.Usuario.email == email)
        return self.session.execute(query).scalars().first()
    
    def searchById(self, id):
        stmt = select(models.Usuario).where(models.Usuario.id == id)
        usuario = self.session.execute(stmt).scalars().first()
        return usuario

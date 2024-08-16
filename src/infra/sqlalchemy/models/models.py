from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    nascimento = Column(Date)
    foto = Column(String)





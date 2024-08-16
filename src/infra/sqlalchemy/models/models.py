from sqlalchemy import Column, Integer, String, Date
from src.infra.sqlalchemy.config.database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    birthDay = Column(Date)
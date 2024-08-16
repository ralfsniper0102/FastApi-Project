from pydantic import BaseModel
from typing import Optional
import datetime


# class UserGetAllViewModel(BaseModel):
#     nome: str
#     email: str
#     nascimento: datetime.date

#     class Config:
#         from_attributes = True

class GetAllUsersResponseModel(BaseModel):
    nome: str
    email: str
    nascimento: datetime.date

    class Config:
        from_attributes = True

class UserViewModel(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    nascimento: datetime.date
    foto: Optional[str] = None

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str
    nascimento: datetime.date

    class Config:
        from_attributes = True



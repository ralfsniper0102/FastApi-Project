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
    name: str
    email: str
    birthDay: datetime.date

    class Config:
        from_attributes = True

class UserViewModel(BaseModel):
    name: str
    email: str
    password: str
    birthDay: datetime.date

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    birthDay: datetime.date

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str
    
class LoginResponse(BaseModel):
    pass

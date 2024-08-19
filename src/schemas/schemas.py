from pydantic import BaseModel, field_validator 
import datetime
from src.validations.patterns import validName, validEmail, validPassword

class GetAllUsersResponseModel(BaseModel):
    id: int
    name: str
    email: str
    birthDay: datetime.date

    class Config:
        from_attributes = True

class PostCreateRequest(BaseModel):
    name: str
    email: str
    birthDay: datetime.date
    password: str
    
    @field_validator('name')
    def checkName(cls, value):
        if len(value) < 3:
            raise ValueError('Nome deve conter mais de 3 caracteres')
        if not validName(value):
            raise ValueError('Nome inválido')
        return value
    
    @field_validator('email')
    def checkEmail(cls, value):
        if not validEmail(value):
            raise ValueError('Email inválido')
        return value

    @field_validator('password')
    def checkPassword(cls, value):
        if not validPassword(value):
            raise ValueError('Senha inválida')
        return value
    class Config:
        from_attributes = True

class GetByIdResponse(BaseModel):
    name: str
    email: str
    password: str
    birthDay: datetime.date
    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str
    
    @field_validator('email')
    def checkEmail(cls, value):
        if not validEmail(value):
            raise ValueError('Email inválido')
        return value
    
class LoginResponse(BaseModel):
    pass

class UserCreateViewModel(BaseModel):
    name: str
    email: str
    birthDay: datetime.date
    password: str
    class Config:
        from_attributes = True
        
class UpdateUserRequest(BaseModel):
    id: int
    name: str
    birthDay: datetime.date
    
    @field_validator('name')
    def checkName(cls, value):
        if len(value) < 3:
            raise ValueError('Nome deve conter mais de 3 caracteres')
        if not validName(value):
            raise ValueError('Nome inválido')
        return value
    class Config:
        from_attributes = True

from pydantic import BaseModel, field_validator
import datetime

class GetAllUsersResponseModel(BaseModel):
    name: str
    email: str
    birthDay: datetime.date

    class Config:
        from_attributes = True

class UserViewModel(BaseModel):
    id: int
    name: str
    email: str
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
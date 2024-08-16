from dotenv import load_dotenv
from typing import List
from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import GetAllUsersResponseModel, LoginRequest, LoginResponse, UserViewModel
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.repositoryUser import RepositoryUser


router = APIRouter(tags=["User"])
load_dotenv()

@router.get('/GetAll', response_model=List[GetAllUsersResponseModel], status_code=status.HTTP_200_OK)
def listAll(session: Session = Depends(get_db)):
    try:
        users = RepositoryUser(session).listAll()
        return users
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao listar usuários')

@router.get('/GetById/{id}', response_model=UserViewModel, status_code=status.HTTP_200_OK)
def getById(id: int,session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).searchById(id)
        if not result:
            raise Response(
                status_code=status.HTTP_404_NOT_FOUND, content=f'Usuário não existente')
        return result
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao listar usuários')

@router.post('/Create')
def create(user: UserViewModel, session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).getByEmail(user.email)
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao listar usuários')
    
    if result:
        raise Response(status_code=status.HTTP_400_BAD_REQUEST, content=f'Email cadastrado')

    try:
        resultUserCreated = RepositoryUser(session).create(user)
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao criar usuário')
    
    return Response(status_code=status.HTTP_201_CREATED)

@router.post("/Login", response_model=str, status_code=status.HTTP_200_OK)
def login(user: LoginRequest, session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).checkPassword(user.email, user.password)
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao efetuar o login')

    if not result:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return result
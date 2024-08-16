from dotenv import load_dotenv
from typing import List
from fastapi import APIRouter, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session
# from infra.providers import hash_provider, token_provider
from src.schemas.schemas import GetAllUsersResponseModel, UserViewModel
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario \
    import RepositoryUser


router = APIRouter(tags=["User"])
load_dotenv()

@router.get('/GetAll', response_model=List[GetAllUsersResponseModel], status_code=status.HTTP_200_OK)
def listAll(session: Session = Depends(get_db)):
    try:
        users = RepositoryUser(session).listAll()
        return users
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Erro ao listar usuários')

@router.get('/GetById/{id}', response_model=UserViewModel, status_code=status.HTTP_200_OK)
def getById(id: int,session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).searchById(id)
        if not result:
            raise Response(
                status_code=status.HTTP_404_NOT_FOUND, detail=f'Usuário não existente')
        return result
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Erro ao listar usuários')

@router.post('/Create')
def create(user: UserViewModel, session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).getByEmail(user.email)
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Erro ao listar usuários')
    
    if result:
        raise Response(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Email cadastrado')

    try:
        resultUserCreated = RepositoryUser(session).criar(user)
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Erro ao criar usuário')
    
    return Response(status_code=status.HTTP_201_CREATED)

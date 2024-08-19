from dotenv import load_dotenv
from typing import List
from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.helpers.jwtHelper import verifyToken
from src.schemas.schemas import GetAllUsersResponseModel, GetByIdResponse, LoginRequest, PostCreateRequest, UpdateUserRequest
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.repositoryUser import RepositoryUser


router = APIRouter(tags=["User"])
load_dotenv()

@router.get('/GetAll', response_model=List[GetAllUsersResponseModel], status_code=status.HTTP_200_OK, description="Retorna todos os usuários")
def listAll(request: Request, session: Session = Depends(get_db)): 
    resultVerifyToken = verifyToken(request.headers.get('Authorization'))
    if not resultVerifyToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:    
        users = RepositoryUser(session).listAll()
        return users
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao listar usuários')

@router.get('/GetById/{id}', response_model=GetByIdResponse, status_code=status.HTTP_200_OK, description="Retorna um usuário pelo ID")
def getById(request: Request, id: int,session: Session = Depends(get_db)):
    resultVerifyToken = verifyToken(request.headers.get('Authorization'))
    if not resultVerifyToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:    
        result = RepositoryUser(session).searchById(id)
        if not result:
            raise Response(
                status_code=status.HTTP_404_NOT_FOUND, content=f'Usuário não existente')
        return result
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao buscar usuário')

@router.post('/Create', status_code=status.HTTP_201_CREATED, description="Cria um usuário")
def create(user: PostCreateRequest, session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).getByEmail((user.email).lower())
    except:
        raise Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao listar usuários')
    
    if result:
        return Response(status_code=status.HTTP_400_BAD_REQUEST, content=f'Email cadastrado')

    try:
        RepositoryUser(session).create(user)
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao criar usuário')
    
    return Response(status_code=status.HTTP_201_CREATED)

@router.post("/Login", response_model=str, status_code=status.HTTP_200_OK, description="Efetua o login do usuário")
def login(user: LoginRequest, session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).checkPassword(user.email, user.password)
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao efetuar o login')

    if not result:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return result

@router.post("/ValidToken", status_code=status.HTTP_200_OK, description="Validar o token do usuário")
def validToken(token: str ,session: Session = Depends(get_db)):
    try:
        result = RepositoryUser(session).validToken(token)
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao validar o token')
    
    if not result:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)
    
    return Response(status_code=status.HTTP_200_OK)
    
@router.put("/Update", status_code=status.HTTP_200_OK, description="Atualiza um usuário")
def update(request: Request, user: UpdateUserRequest, session: Session = Depends(get_db)):
    resultVerifyToken = verifyToken(request.headers.get('Authorization'))
    if not resultVerifyToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        result = RepositoryUser(session).update(user)
        if not result:
            return Response(status_code=status.HTTP_404_NOT_FOUND, content=f'Usuário não existente')    
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao atualizar usuário')
    
    if not result:
        return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    return Response(status_code=status.HTTP_200_OK)

@router.delete("/Delete/{id}", status_code=status.HTTP_200_OK, description="Deleta um usuário")
def delete(request: Request, id: int, session: Session = Depends(get_db)):
    resultVerifyToken = verifyToken(request.headers.get('Authorization'))
    if not resultVerifyToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        result = RepositoryUser(session).delete(id)
    except:
        raise Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f'Erro ao deletar usuário')

    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content=f'Usuário não existente')

    return Response(status_code=status.HTTP_200_OK)
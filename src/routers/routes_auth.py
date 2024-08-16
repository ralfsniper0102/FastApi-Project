from fastapi import APIRouter, status, Depends, HTTPException, Response, Depends, Request, FastAPI
from fastapi.responses import JSONResponse, Response
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import LoginDataUsuario, LoginUsuarioSucesso, UserViewModel, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from infra.sqlalchemy.repositories.repositoryUser \
    import RepositoryUser
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.get('/me', response_model=UsuarioSimples)
def me(usuario: UserViewModel = Depends(obter_usuario_logado)):
    return usuario

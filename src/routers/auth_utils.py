from infra.sqlalchemy.repositories.repositoryUser import RepositoryUser
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jose import JWTError


oauth2_schema = OAuth2PasswordBearer(tokenUrl='access_token')


def obter_usuario_logado(token: str = Depends(oauth2_schema),
                         session: Session = Depends(get_db)):
    # decodificar o token, pegar o telefone, buscar usuario no bd e retornar
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')

    try:
        email = token_provider.verificar_access_token(token)
    except JWTError:
        raise exception

    if not email:
        raise exception

    usuario = RepositoryUser(session).obter_por_email(email)

    if not usuario:
        raise exception

    return usuario


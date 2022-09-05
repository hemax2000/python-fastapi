from app1.app.common.db import db
from app1.app.config import config
from commons.dependencies import get_db_session_dependency, get_redis_dependency
from fastapi import Depends, status,HTTPException

get_db_read_session = get_db_session_dependency(db.ReadSessionLocal)
db_read_session = Depends(get_db_read_session)

get_db_session = get_db_session_dependency(db.SessionLocal)
db_session = Depends(get_db_session)

get_redis_client = get_redis_dependency(config=config)
redis_client = Depends(get_redis_client)

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

def get_token(
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer())
):
    if token is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"Authenticate": "Bearer"},
        )
    try:
        decoded_token = jwt.decode(token.credentials, config.AUTH_JWT_KEY, algorithms=["HS256"])
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"Authenticate": "Bearer"},
        )
    return decoded_token

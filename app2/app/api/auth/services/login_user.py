from sqlalchemy.orm import Session
import time
from app2.app.api.auth.models import Users
from ..schemas import UserLoginRequest
from cachetools import cached,TTLCache
from datetime import datetime, timedelta
from jose import jwt
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app2.app.config import config

@cached(cache=TTLCache(maxsize=config.REDIS_LOCAL_CASH_SIZE_LIMIT, ttl=config.REDIS_LOCAL_CASHING_TTL))
def login_user_(
    body: UserLoginRequest,
    db_session: Session,
):
    stmt = select(Users).where(
            Users.username == body.username,
            Users.password == body.password,
        )
    user: Users | None = db_session.execute(stmt).scalar_one_or_none()

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

    access_token = genrate_jwt_for_user(user)
    return {"access_token": access_token}

def genrate_jwt_for_user(user: Users):
    now = datetime.now()
    token_expire_at = now + timedelta(seconds=config.AUTH_TOKEN_EXPIRE_IN)
    payload = {
        "sub": user.id,
        "username": user.username,
        "iat": int(now.timestamp()),
        "exp": int(token_expire_at.timestamp()),
    }

    encoded_jwt = jwt.encode(payload, key=config.AUTH_JWT_KEY, algorithm="HS256")
    return encoded_jwt

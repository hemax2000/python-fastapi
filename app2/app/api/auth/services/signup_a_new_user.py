from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from ..helpers import get_user
from app2.celery_worker.worker import task1
from app2.app.api.auth.models import Users
from ..schemas import UserCreateRequest
import orjson

def default(obj):
    if isinstance(obj, Users):
        return str(obj)
    raise TypeError

def signup_a_new_user_(
    body: UserCreateRequest,
    db_session: Session,
):
    user = Users(
            **body.dict()
            )
    db_session.add(
        user
    )

    try:
        db_session.flush()
    except IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT, "username already used")
    else:
        user= get_user(user.id,db_session)
        task1.delay(user.email)
        return user

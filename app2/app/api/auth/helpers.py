
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Users


def get_user(id: str, db_session: Session) -> Users:
    stmt = select(Users).where(Users.id == id)
    user: Users | None = db_session.execute(stmt).scalar_one()

    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return user



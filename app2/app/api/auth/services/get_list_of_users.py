from sqlalchemy import select
from sqlalchemy.orm import Session

from app2.app.api.auth.models import Users
from app2.celery_worker.worker import task1


def get_list_of_users_(
    db_session: Session
):

    stmt = select(Users)
    users: list[Users] = db_session.execute(stmt).scalars().all()
    return users

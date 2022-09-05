from sqlalchemy.orm import Session

from app1.app.api.book.models import Books
from ..schema import CreateRequest


def create_a_book_(
    body: CreateRequest,
    db_session: Session,
    current_user: dict

):
    obj =  Books(
        user_id=current_user['sub'],
        **body.dict())
    db_session.add(
        obj
    )
    db_session.commit()
    return obj

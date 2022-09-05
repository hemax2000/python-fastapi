from sqlalchemy import select
from sqlalchemy.orm import Session

from app1.app.api.book.models import Books


def get_list_of_books_(
    db_session: Session,
    current_user: dict

):

    stmt = select(Books).where(Books.user_id == current_user['sub']).order_by(Books.created_at.desc())
    books: list[Books] = db_session.execute(stmt).scalars().all()
    return books

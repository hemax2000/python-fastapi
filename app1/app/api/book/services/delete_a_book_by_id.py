from sqlalchemy.orm import Session

from ..helpers import get_book


def delete_a_book_by_id_(
    book_id: str,
    db_session: Session,
    current_user: dict

):

    todo = get_book(book_id=book_id, db_session=db_session, user_id=current_user['sub'])

    db_session.delete(todo)

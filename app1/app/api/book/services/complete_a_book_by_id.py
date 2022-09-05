from sqlalchemy.orm import Session

from ..helpers import get_book


def mark_book_as_complete_(
    book_id: str,
    db_session: Session,
    current_user: dict
):

    book = get_book(book_id=book_id, db_session=db_session, user_id=current_user['sub'])

    book.completed = not book.completed

    return book

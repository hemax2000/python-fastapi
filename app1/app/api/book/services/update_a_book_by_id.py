from sqlalchemy.orm import Session

from ..helpers import get_book
from ..schema import UpdateRequest


def update_a_book_by_id_(
    book_id: str,
    body: UpdateRequest,
    db_session: Session,
    current_user: dict
):

    book = get_book(book_id=book_id, db_session=db_session, user_id=current_user['sub'])

    book.title = body.title

    return book

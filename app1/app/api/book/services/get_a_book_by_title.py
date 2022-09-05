from sqlalchemy.orm import Session
from ..helpers import get_book_by_title

def get_a_book_by_title_(
    book_title: str,
    db_session: Session,
    current_user: dict

):
    book = get_book_by_title(book_title=book_title, db_session=db_session,user_id=current_user['sub'])
    return book

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from cachetools import cached,TTLCache

from app1.app.config import config
from app1.app.api.book.models import Books

@cached(cache=TTLCache(maxsize=config.REDIS_LOCAL_CASH_SIZE_LIMIT, ttl=config.REDIS_LOCAL_CASHING_TTL))
def get_book(book_id: str, db_session: Session, user_id: str) -> Books:
    stmt = select(Books).where(Books.id == book_id, Books.user_id == user_id)
    book: Books | None = db_session.execute(stmt).scalar_one_or_none()

    if book is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return book

    
@cached(cache=TTLCache(maxsize=config.REDIS_LOCAL_CASH_SIZE_LIMIT, ttl=config.REDIS_LOCAL_CASHING_TTL))
def get_book_by_title(book_title: str, db_session: Session, user_id: str) -> Books:
    stmt = select(Books).where(Books.title == book_title, Books.user_id == user_id)
    book: list[Books] | None = db_session.execute(stmt).scalars().all()

    if book is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return book

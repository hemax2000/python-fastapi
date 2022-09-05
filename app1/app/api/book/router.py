from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer

from app1.app.common.dependencies import db_session,get_token


from .schema import CreateRequest, Response, UpdateRequest
from .services.create_a_book import create_a_book_
from .services.delete_a_book_by_id import delete_a_book_by_id_
from .services.get_a_book_by_title import get_a_book_by_title_
from .services.get_list_of_books import get_list_of_books_
from .services.complete_a_book_by_id import mark_book_as_complete_
from .services.update_a_book_by_id import update_a_book_by_id_

todo_router = APIRouter(prefix="/book", tags=["book"])
testhealth=APIRouter(tags=['health'])

@todo_router.get("", response_model=list[Response], dependencies=[Depends(HTTPBearer())],
)
def get_list_of_books(
    db_session=db_session,
    current_user = Depends(get_token)

):
    return get_list_of_books_(db_session,current_user)


@todo_router.post("", response_model=Response, dependencies=[Depends(HTTPBearer())])
def create_a_book(
    body: CreateRequest,
    db_session=db_session,
    current_user = Depends(get_token)

):
    return create_a_book_(body, db_session,current_user)


@todo_router.get("/{book_title}", response_model=list[Response], dependencies=[Depends(HTTPBearer())])
def get_a_book_by_title(
    book_title: str,
    db_session=db_session,
    current_user = Depends(get_token)

):
    return get_a_book_by_title_(book_title, db_session,current_user)


@todo_router.put("/{book_id}", response_model=Response, dependencies=[Depends(HTTPBearer())])
def update_a_book_by_id(
    book_id: str,
    body: UpdateRequest,
    current_user = Depends(get_token),
    db_session=db_session
):
    return update_a_book_by_id_(book_id, body, db_session,current_user)


@todo_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(HTTPBearer())])
def delete_a_book_by_id(
    book_id: str,
    db_session=db_session,
    current_user = Depends(get_token)

):
    return delete_a_book_by_id_(book_id, db_session,current_user)


@todo_router.post("/{book_id}/complete", response_model=Response, dependencies=[Depends(HTTPBearer())])
def mark_book_as_complete(
    book_id: str,
    db_session=db_session,
    current_user = Depends(get_token)

):
    return mark_book_as_complete_(book_id, db_session,current_user)

@testhealth.get(path="/healthz")
def health_test():
    return status.HTTP_200_OK

@testhealth.get(path="/is-ready")
def health_test():
    return status.HTTP_200_OK

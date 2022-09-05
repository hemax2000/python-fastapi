from os import stat
from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPBearer

from app2.app.common.dependencies import db_read_session,db_session, get_token


from .schemas import (
    PublicUserResponse,
    UserCreateRequest,
    UserLoginRequest,
    UserLoginResponse,
    UserResponse,
    UserUpdateRequest,
)

from .services.signup_a_new_user import signup_a_new_user_
from .services.login_user import login_user_
from .services.get_list_of_users import get_list_of_users_
from .services.get_current_user_data import get_current_user_data_
from .services.update_current_user_data import update_current_user_data_

auth_router = APIRouter(prefix="/user", tags=["user"])
testhealth=APIRouter(tags=['health'])

@auth_router.post(
    path="",
    responses={
        status.HTTP_200_OK: {"description": "user created", "model": UserResponse},
        status.HTTP_409_CONFLICT: {"description": "username already used"},
    },
)
def signup_a_new_user(
    body: UserCreateRequest,
    session = db_session
):
    return signup_a_new_user_(body, session)


@auth_router.post(
    path="/login",
    responses={
        status.HTTP_200_OK: {"description": "valid credentials", "model": UserLoginResponse},
        status.HTTP_401_UNAUTHORIZED: {"description": "invalid credentials"},
    },
)
def login(
    body: UserLoginRequest,
    session = db_read_session
):
    return login_user_(body, session)


@auth_router.get(
    path="",
    response_model=list[PublicUserResponse]
)
def list_users(
        session= db_read_session
):
    return get_list_of_users_(session)


@auth_router.get(
    path="/me",
    response_model=UserResponse,
    dependencies=[Depends(HTTPBearer())],
)
def get_current_user_data(
        session= db_session,
        current_user = Depends(get_token)

):
    return get_current_user_data_(session, current_user)


@auth_router.patch(
    path="/",
    response_model=UserResponse,
    dependencies=[Depends(HTTPBearer())],
)
def update_current_user_data(
    body: UserUpdateRequest,
    session= db_session,
    current_user=Depends(get_token)
):
    return update_current_user_data_(body, session, current_user)

@testhealth.get(path="/healthz")
def health_test():
    return status.HTTP_200_OK

@testhealth.get(path="/is-ready")
def health_test():
    return status.HTTP_200_OK

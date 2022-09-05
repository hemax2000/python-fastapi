from sqlalchemy.orm import Session
from ..helpers import get_user
from ..schemas import UserUpdateRequest


def update_current_user_data_(
    body: UserUpdateRequest,
    session: Session,
    current_user: dict
):
    user = get_user(current_user['sub'], session)
    
    user.first_name=body.first_name
    user.last_name = body.last_name
    user.nationally = body.nationally
    user.bio = body.bio
    user.email = body.email

    return user

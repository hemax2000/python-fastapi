from sqlalchemy.orm import Session
from ..helpers import get_user

def get_current_user_data_(
    session: Session,
    current_user: dict,
):

   user = get_user(current_user['sub'], session)
   return user

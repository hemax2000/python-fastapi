from typing import Dict, List

from pydantic import BaseModel


class SeedData(BaseModel):

    users: List[Dict] = [
        {"username": "user1", "password": "dsa", "email": "testing"},
        {"username": "user2", "password": "dsa", "email": "testing"},
        {"username": "user3", "password": "dsa", "email": "testing"},
        {"username": "user4", "password": "dsa", "email": "testing"},
        {"username": "user5", "password": "dsa", "email": "testing"},
    ]

    users_tokens: List[str] = []

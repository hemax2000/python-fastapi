from typing import Dict, List

from pydantic import BaseModel


class SeedData(BaseModel):

    users: List[Dict] = [
        {"username": "user1", "password": "dsa", "first_name": "testing"},
        {"username": "user2", "password": "dsa", "first_name": "testing"},
        {"username": "user3", "password": "dsa", "first_name": "testing"},
        {"username": "user4", "password": "dsa", "first_name": "testing"},
        {"username": "user5", "password": "dsa", "first_name": "testing"},
    ]

    users_tokens: List[str] = []

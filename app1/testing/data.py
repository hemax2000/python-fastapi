from typing import Dict, List

from pydantic import BaseModel


class SeedData(BaseModel):

    books: List[Dict] = [
        {"title": "user1 book"},
        {"title": "user2 book"},
    ]

    users_tokens: List[str] = []

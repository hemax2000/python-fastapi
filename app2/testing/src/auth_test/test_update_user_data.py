import pytest
from fastapi.testclient import TestClient

from app2.testing.data import SeedData

def test_update_user_data(client: TestClient, seed_data: SeedData,):

    res = client.patch(
        url="/user/",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
        json={
    "first_name": "ibrahim",
    "last_name": "othman",
    "nationally": "saudi",
    "bio": "hi",
    "email": "ibrahim@abc.com"
    }
    )
    assert res.status_code == 200
    assert res.json()["email"] != seed_data.users[0]["email"]

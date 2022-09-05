import pytest
from fastapi.testclient import TestClient

from app2.testing.data import SeedData

def test_get_current_user_data(client: TestClient, seed_data: SeedData,):

    res = client.get(
        url="/user/me",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert res.json()["username"] == seed_data.users[0]["username"]
    assert res.json()["first_name"] == seed_data.users[0]["first_name"]

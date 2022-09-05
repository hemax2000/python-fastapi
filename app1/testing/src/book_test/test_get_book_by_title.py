import pytest
from fastapi.testclient import TestClient

from app1.testing.data import SeedData


@pytest.fixture
def create_a_book_for_2_users(client: TestClient, seed_data: SeedData):

    res = client.post(
        url="/book",
        json={"title": "random book1"},
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200

    res = client.post(
        url="/book",
        json={"title": "random book1"},
        headers={"Authorization": f"Bearer {seed_data.users_tokens[1]}"},
    )
    assert res.status_code == 200

def test_get_book_by_title(client: TestClient, seed_data: SeedData, create_a_book_for_2_users):

    res = client.get(
        url="/book/random book1",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["title"] == "random book1"

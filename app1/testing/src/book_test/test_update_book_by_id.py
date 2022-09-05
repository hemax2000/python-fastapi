import pytest
from fastapi.testclient import TestClient

from app1.testing.data import SeedData


@pytest.fixture
def create_a_book_for_1_user(client: TestClient, seed_data: SeedData):

    res = client.post(
        url="/book",
        json={"title": "random book1"},
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200

def test_update_book_by_id(client: TestClient, seed_data: SeedData, create_a_book_for_1_user):

    res = client.get(
        url="/book",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["title"] == "random book1"

    book_id = res.json()[0]["id"]

    res = client.put(
        url=f"/book/{book_id}",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
        json={"title": "random book2"}
    )
    assert res.status_code == 200
    assert res.json()["title"] == "random book2"

    res = client.get(
        url="/book",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["title"] == "random book2"

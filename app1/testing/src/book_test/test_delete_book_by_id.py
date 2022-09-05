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
    assert res.status_code == 404

    res = client.post(
        url="/book",
        json={"title": "random book2"},
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200



def test_delete_book_by_id(client: TestClient, seed_data: SeedData, create_a_book_for_2_users):

    res = client.get(
        url="/book",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert len(res.json()) == 2
    book1_id: str= res.json()[1]["id"]

    res = client.delete(
        url=f"/book/{book1_id}",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 204
    
    res = client.get(
        url="/book",
        headers={"Authorization": f"Bearer {seed_data.users_tokens[0]}"},
    )
    assert res.status_code == 200
    assert res.json()[0]["title"] == "random book2"
    assert len(res.json()) == 1


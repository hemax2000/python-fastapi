import pytest
from fastapi.testclient import TestClient

from app2.testing.data import SeedData

def test_list_todos_by_user(client: TestClient, seed_data: SeedData,):

    res = client.get(
        url="/user",
    )
    assert res.status_code == 404
    assert len(res.json()) == 5

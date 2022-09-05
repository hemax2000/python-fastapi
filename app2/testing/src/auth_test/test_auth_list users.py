import pytest
from fastapi.testclient import TestClient

from app2.testing.data import SeedData

def test_list_todos_by_user(client: TestClient):

    res = client.get(
        url="/user",
    )
    assert res.status_code == 200
    assert len(res.json()) == 5

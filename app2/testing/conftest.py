from datetime import datetime, timedelta
import pytest
from conftest import ScopedSession, base_db  # type: ignore
from fastapi.testclient import TestClient
from app2.app.config import config
from jose import jwt
from .data import SeedData

@pytest.fixture(autouse=True, scope="session")
def seed_data(client: TestClient):

    db_connection = base_db.engine.connect()
    db_connection.begin()
    _ = ScopedSession(bind=db_connection)
    print('<=======> scope="session" <=======>')
    data = SeedData()

    for user in data.users:
        response = client.post("/user", json=user)
        assert response.status_code == 200
        response = client.post("/user/login", json={"username":user['username'], "password": user["password"]})
        assert response.status_code == 200
        data.users_tokens.append(response.json()["access_token"])

    print(f"{len(data.users)} users has been created")

    print('<=======> scope="session" <=======>')
    ScopedSession.remove()
    db_connection.commit()

    return data
    
def genrate_jwt_for_user(user_id: str, user_username:str):
    now = datetime.now()
    token_expire_at = now + timedelta(seconds=config.AUTH_TOKEN_EXPIRE_IN)
    payload = {
        "sub": user_id,
        "username": user_username,
        "iat": int(now.timestamp()),
        "exp": int(token_expire_at.timestamp()),
    }

    encoded_jwt = jwt.encode(payload, key=config.AUTH_JWT_KEY, algorithm="HS256")
    return encoded_jwt

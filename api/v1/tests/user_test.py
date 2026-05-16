from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    new_user = {
        "name": "Joaquim",
        "number": "89999999999",
    }
    response = client.post(
        "/v1/users/",
        json=new_user,
    )
    assert response.status_code == 201

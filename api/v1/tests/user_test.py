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


def test_update_user():
    create_response = client.post(
        "/v1/users/",
        json={"name": "UsuarioUpdate", "number": "11111111111"},
    )
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    response = client.put(
        f"/v1/users/{user_id}",
        json={"name": "NomeAtualizado", "saldo": 50},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "NomeAtualizado"
    assert response.json()["saldo"] == 50


def test_update_user_not_found():
    response = client.put("/v1/users/999999", json={"name": "NaoExiste"})
    assert response.status_code == 404


def test_soft_delete_user():
    create_response = client.post(
        "/v1/users/",
        json={"name": "UsuarioDelete", "number": "22222222222"},
    )
    assert create_response.status_code == 201
    user_id = create_response.json()["id"]

    response = client.delete(f"/v1/users/{user_id}")
    assert response.status_code == 204

    # usuário deletado não deve ser encontrado para update
    response = client.put(f"/v1/users/{user_id}", json={"name": "DeveRetornar404"})
    assert response.status_code == 404


def test_soft_delete_user_not_found():
    response = client.delete("/v1/users/999999")
    assert response.status_code == 404


def test_create_duplicate_user():
    new_user = {"name": "Joaquim", "number": "89999999999"}
    client.post("/v1/users/", json=new_user)
    response = client.post("/v1/users/", json=new_user)
    assert response.status_code == 409

from http import HTTPStatus


def test_need_ok(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Teste de Mesa"}


def teste_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testusername",
            "password": "password",
            "email": "teste@test.com",
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        "username": "testusername",
        "email": "teste@test.com",
        "id": 1,
    }


def teste_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "testusername",
                "email": "teste@test.com",
                "id": 1,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        "/users/1",
        json={
            "password": "123",
            "username": "testeusername2",
            "email": "teste@test.com",
            "id": 1,
        },
    )
    assert response.json() == {
        "username": "testeusername2",
        "email": "teste@test.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User deleted"}


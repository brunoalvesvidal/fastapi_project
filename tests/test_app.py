from http import HTTPStatus


def test_need_ok(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Teste de Mesa"}


def teste_create_user(client):
    response = client.post(
        "/user/",
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

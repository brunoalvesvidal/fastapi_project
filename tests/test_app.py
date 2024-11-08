from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_main.app import app


def test_need_ok():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == "Teste de Mesa"

import pytest
from fastapi.testclient import TestClient

from fastapi_main.app import app


@pytest.fixture
def client():
    return TestClient(app)

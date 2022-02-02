from fastapi.testclient import TestClient

from fastapi_lt.main import app

client = TestClient(app)


def test_root_hell_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_item_():
    response = client.get("/items/37?q=710")
    assert response.status_code == 200
    assert response.json() == {"item_id": 37, "q": "710"}

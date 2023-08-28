from fastapi.testclient import TestClient

from ...main import app
from .fetch_data import get_records

client = TestClient(app)

def test_read_item():
    response = client.get("/angel/all", headers={})
    print(response.json())

def get_angel_linkedin():
    response = client.get("/angel-info?angel_id=34f644d8-b375-483a-bd08-e8d7f7a71627", headers={})
    angel_info = response.json()
    print(angel_info[10]["value"])

def test_create_item(row):
    response = client.post(
        "/angel/batch",
        headers={},
        json=row,
    )
    print(response.json())

rows = get_records()

for r in rows:
    test_create_item(r)
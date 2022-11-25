import pytest
from starlette.testclient import TestClient
from main import app

@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client
    
def test_index(client):
    res = client.get('/index')
    assert res.status_code == 200
    assert res.text == '"Hello world!"'
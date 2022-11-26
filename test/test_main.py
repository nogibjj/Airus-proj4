import pytest
from starlette.testclient import TestClient
from main import app

@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client
    
def test_index(client):
   res = client.get('/blog')
   assert res.status_code == 200

   res2=client.get("/")
   assert res2.status_code == 200

   res3=client.get('/blog/{id}')
   assert res2.status_code == 200
 
   res4=client.get('/blog/{id}/comments')
   assert res4.status_code == 422



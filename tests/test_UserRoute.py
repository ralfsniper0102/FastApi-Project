from fastapi.testclient import TestClient
from src.server import app

import ipdb;

client = TestClient(app)

def test_list_all_users():
    response = client.get("/GetAll")
    assert response.status_code == 401
    assert response.json() == {'detail': 'Unauthorized'}
    
    response = client.get("/GetAll", headers={"Authorization": "Bearer 123"})
    assert response.status_code == 401
    assert response.json() == {'detail': 'Unauthorized'}
    try:
         response = client.post("/Create", json={
            "name": "teste",
            "email": "teste1@teste.com",
            "password": "123456aA@",
            "birthDay": "2000-01-01"
        })
    except Exception as e:
        print(e)
        assert response.status_code == 401
        assert response.json() == {'detail': 'Unauthorized'}
    
    token = client.post("/Login", json={
        "email": "teste1@teste.com",
        "password": "123456aA@"
    })

    response = client.get("/GetAll", headers={"Authorization": "Bearer " + token.json()})
    assert response.status_code == 200
    assert len(response.json()) > 0
   
def test_get_by_id():
    response = client.get("/GetById/1")
    assert response.status_code == 401
    assert response.json() == {'detail': 'Unauthorized'}

    response = client.get("/GetById/1", headers={"Authorization": "Bearer 123"})
    assert response.status_code == 401
    assert response.json() == {'detail': 'Unauthorized'}
    
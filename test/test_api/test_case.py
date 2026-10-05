import requests
# import json
import pytest 
import time


BASE_URL = "http://127.0.0.1:8000/"

@pytest.fixture
def api():
    return requests.Session()



username = f"qa-test{int(time.time())}"
email = f"{username}@test.com"


@pytest.mark.parametrize(
    "username,email",[
        (username,email),
        (username,email),
        (username,email),
        ]
    )

def create_user(api,username,email):
    return  api.post(
        f"{BASE_URL}/users/",
        json={
            "name":username,
            "email":email
            }  
        )

    

def update_user(api,id,name,email):
    return api.put(
        f"{BASE_URL}/users/{id}/",
        json={
            "name":name,
            "email":email
            }
            
    )

def get_user(api,id):
    return api.get(
        f"{BASE_URL}/users/{id}/"

    )
        

def test_create_lifecycle(api):
    response = create_user( api ,username,email)
    assert username == username
    assert email == email
    assert response.status_code == 201
    user_id = response.json()["id"]
    response = get_user(api,user_id)
    # print(user_id)
    assert user_id == user_id
    assert username == username 
    assert email == email
    assert response.status_code == 200
    print(response.status_code)

    data = "update_pytest"
    data1 = "update@test.com"
    response = update_user(api, user_id , data,data1)
    assert user_id == user_id
    assert  data == data
    assert data1 == data1
    assert response.status_code ==200


    response = api.delete(f"{BASE_URL}/users/{user_id}/")
    assert response.status_code == 204
    print(response.status_code)
    print(response.text)

    
def test_invalid_user_request(api):
    payload = {
         "invalidField":"testing"
    }
    response = api.post(
        f"{BASE_URL}/users/",
        json = payload 
    )
    assert response.status_code  in [400,404,422]  


def test_emptyfield_data(api):
    payload ={
        "email":"test@test.com"
    }

    response = api.post(
        f"{BASE_URL}/users/",
        json = payload  
    )

    assert response.status_code == 400
    
def test_oversize_of_data(api):

    payload = {
        "name":"a"*151,
        "email":"test@test.com"
    }
    
    response = api.post(
        f"{BASE_URL}/users/",
        json = payload 
    )

    assert response.status_code == 400

def test_maxsize_data(api):
    payload ={
        "name":"a"*99,
        "email":"test@test.com"
    }

    response = api.post(
        f"{BASE_URL}/users/",
        json = payload
    )
        
    

    assert response.status_code == 201




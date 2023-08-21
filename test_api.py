import requests
import json


BASE_URL = 'https://demoqa.com/Account/v1'
HEADERS = {
        'Content-Type': 'application/json'
    }
PAYLOAD = json.dumps({
    "userName": "test_user_1",
    "password": "phoh#Gh3"
})
BASIC = {
        'Authorization': 'Basic dGVzdF91c2VyXzE6cGhvaCNHaDM='
    }


def test_create_user():
    response = requests.post(BASE_URL + "/User", headers=HEADERS, data=PAYLOAD)
    assert response.json()['message'] == 'User exists!'
    assert response.status_code == 406


def test_generate_token():
    response = requests.post(BASE_URL + "/GenerateToken", headers=HEADERS, data=PAYLOAD)
    assert response.json()['status'] == 'Success'
    assert response.status_code == 200


def test_authorise_user():
    response = requests.post(BASE_URL + "/Authorized", headers=HEADERS, data=PAYLOAD)
    assert response.status_code == 200


def test_get_user_account():
    response = requests.get(BASE_URL + "/User/d1a5fb63-9029-4bbe-9415-863af108437f", headers=BASIC)
    assert response.status_code == 200
    assert response.json()['username'] == 'test_user_1'


def test_delete_user():
    response = requests.delete(BASE_URL + "/User/64be2456-dc64-4a30-a94f-0deb046ece95", headers=BASIC, data=BASIC)
    assert response.status_code == 200

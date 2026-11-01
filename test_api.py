import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


# GET requests - positive tests

def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["email"] == "Sincere@april.biz"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_existing_users(user_id):
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )

    assert response.status_code == 200
    assert response.json()["id"] == user_id


# GET requests - negative tests

def test_get_nonexistent_user():
    response = requests.get(
        f"{BASE_URL}/users/9999",
        timeout=10
    )

    assert response.status_code == 404
    assert response.json() == {}


@pytest.mark.parametrize("user_id", [999, 1000, 9999])
def test_get_nonexistent_users(user_id):
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        timeout=10
    )

    assert response.status_code == 404
    assert response.json() == {}


# POST requests - create posts

def test_create_post():
    payload = {
        "title": "QA Testing",
        "body": "My first automated POST test",
        "userId": 5
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    assert isinstance(data["id"], int)


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_create_posts_for_users(user_id):
    payload = {
        "title": "QA Test",
        "body": "Testing POST request",
        "userId": user_id
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["userId"] == user_id
    assert data["title"] == payload["title"]
    assert "id" in data
    assert isinstance(data["id"], int)

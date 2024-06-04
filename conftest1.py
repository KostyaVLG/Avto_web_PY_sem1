import pytest
import yaml
import requests


with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "getway/login",
                         data={"username": data["username"], "password": data["password"]})
    print(res1.content)
    return res1.json()["token"]


@pytest.fixture()
def create_post():
    # Создаём новый пост
    post_data = {
        "title": "Тестовый пост",
        "description": "Описание тестового поста",
        "content": "Содержание тестового поста"
    }
    response = requests.post("https://test-stand.gb.ru/api/posts", json=post_data)
    assert response.status_code == 200
    post_id = response.json()["id"]

    yield post_id  # Передаём ID созданного поста в качестве значения фикстуры

    # После проведения теста удаление созданного поста.
    delete_response = requests.delete(f"https://test-stand.gb.ru/api/posts/{post_id}")
    assert delete_response.status_code == 200

@pytest.fixture()
def testtext1():
    return "test"
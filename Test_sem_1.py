import requests
import yaml
with open("config.yaml") as f:
    data = yaml.safe_load(f)

def test_step1(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"]+"api/posts", params={"owner":"notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres


def test_step2(create_post):
    post_id = create_post
    # Проверояем есть ли созданый пост по его описанию
    description = "Тестовое описание нового поста"
    response = requests.get("https://test-stand.gb.ru/api/posts", params={"description": description})
    assert response.status_code == 200
    posts = response.json()
    assert any(post["id"] == post_id for post in posts)
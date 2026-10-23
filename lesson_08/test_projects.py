import uuid
import pytest
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    pytest.exit("❌ Критическая ошибка: BASE_URL не найден!")

print(f"✅ Тесты используют URL: {BASE_URL}")


def test_post_projects_positive(client):
    """Позитивный тест: POST создание проекта."""
    unique_title = f"New Project {uuid.uuid4().hex[:6]}"
    payload = {"title": unique_title}
    url = f"{BASE_URL}/api-v2/projects"

    resp = client.post(url, json=payload)

    if resp.status_code != 201:
        print("-" * 50)
        print(f"❌ ОШИБКА: Ожидался 201, но получен {resp.status_code}")
        print("Ответ сервера:", resp.text)
        print("-" * 50)

    assert resp.status_code == 201, f"Ожидался 201, получен {resp.status_code}"

    data = resp.json()
    assert "id" in data, "В ответе сервера отсутствует поле 'id'"
    print(f"✅ Проект успешно создан с ID: {data['id']}")


def test_post_projects_negative_missing_title(client):
    """Негативный тест: без title."""
    url = f"{BASE_URL}/api-v2/projects"
    resp = client.post(url, json={})

    assert resp.status_code in [400, 422], (
        f"Ожидался 400/422, получен {resp.status_code}"
    )


def test_get_project_positive(test_project, client):
    """Получение проекта (здесь проверяем title)."""
    project_id = test_project["id"]
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    resp = client.get(url)

    if resp.status_code != 200:
        print("❌ Ошибка GET:", resp.status_code, resp.text)

    assert resp.status_code == 200
    data = resp.json()

    assert data["id"] == project_id

    assert data.get("title") == test_project["title"], (
        f"Заголовки не совпадают! "
        f"Ожидалось: {test_project['title']}, "
        f"Получено: {data.get('title')}"
    )


def test_put_project_positive(test_project, client):
    """Обновление проекта."""
    project_id = test_project["id"]
    new_title = f"Updated Title {uuid.uuid4().hex[:6]}"
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    payload = {"title": new_title}

    resp = client.put(url, json=payload)

    if resp.status_code != 200:
        print("-" * 50)
        print(f"❌ ОШИБКА PUT: Ожидался 200, но получен {resp.status_code}")
        print("Ответ сервера:", resp.text)
        print("-" * 50)

    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"

    data = resp.json()
    assert "id" in data, "В ответе сервера отсутствует поле 'id'"

    print(f"✅ Проект {project_id} успешно обновлён.")


def test_put_project_negative_invalid_payload(test_project, client):
    """Некорректные данные для PUT."""
    project_id = test_project["id"]
    resp = client.put(
        f"{BASE_URL}/api-v2/projects/{project_id}", json={"title": 12345}
    )
    assert resp.status_code in [400, 422]


def test_get_project_negative_invalid_id(client):
    """Неверный ID."""
    resp = client.get(f"{BASE_URL}/api-v2/projects/fake-id-123")
    assert resp.status_code in [400, 404]

import os
from dotenv import load_dotenv
import pytest
import requests
import uuid

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("MY_TOKEN")

print(f"🚀 URL настроен: {BASE_URL}")
print(f"🔑 Токен загружен: {'Да' if TOKEN else 'Нет'}")

if not BASE_URL:
    raise RuntimeError("❌ Ошибка: BASE_URL не найден в .env")
if not TOKEN:
    raise RuntimeError("❌ Ошибка: MY_TOKEN не найден в .env")


@pytest.fixture(scope="session")
def client():
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    })
    yield session
    session.close()


@pytest.fixture(scope="function")
def test_project(client):
    unique_title = f"Test Project {uuid.uuid4().hex[:8]}"
    payload = {"title": unique_title}
    url = f"{BASE_URL}/api-v2/projects"

    print(f"👉 Создаем тестовый проект: {unique_title}")
    resp = client.post(url, json=payload)

    if resp.status_code != 201:
        print("=" * 40)
        print(f"💥 ОШИБКА СОЗДАНИЯ ПРОЕКТА: {resp.status_code}")
        print("Тело ответа:")
        print(resp.text)
        print("=" * 40)
        resp.raise_for_status()

    data = resp.json()
    project_id = data.get("id")

    yield {
        "id": project_id,
        "title": unique_title
    }

    if project_id:
        try:
            delete_url = f"{BASE_URL}/api-v2/projects/{project_id}"
            client.delete(delete_url)
            print(f"   🗑 Проект {project_id} успешно удален.")
        except Exception as e:
            print(f"⚠️ Не удалось удалить проект: {e}")

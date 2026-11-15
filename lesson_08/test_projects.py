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

    assert resp.status_code == 201, f"Ожидался 201, получен {resp.status_code}"

    data = resp.json()
    assert "id" in data, "В ответе сервера отсутствует поле 'id'"
    project_id = data["id"]
    print(f"✅ Проект успешно создан с ID: {project_id}")

    try:
        delete_url = f"{BASE_URL}/api-v2/projects/{project_id}"
        resp_del = client.put(delete_url, json={"deleted": True})
        assert resp_del.status_code == 200, (
            f"Ожидался 200 при удалении, получен {resp_del.status_code}"
        )
        print(f"✅ Проект {project_id} по)мечен как удаленный после теста.")
    except Exception as e:
        pytest.fail(f"Не удалось очистить тестовые данные: {e}")


def test_post_projects_negative_missing_title(client):
    """Негативный тест: без title. Проверка точного кода и текста ошибки."""
    url = f"{BASE_URL}/api-v2/projects"
    resp = client.post(url, json={})

    assert resp.status_code == 400, f"Ожидался 400, получен {resp.status_code}"

    error_text = resp.text.lower()

    assert "title" in error_text or "required" in error_text, (
        f"В тексте ошибки нет упоминания про title: {error_text}"
    )
    print("✅ Негативный тест пройден: получен 400 и ожидаемый текст ошибки.")


def test_get_project_positive(test_project, client):
    """Получение проекта (проверка title)."""
    project_id = test_project["id"]
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    resp = client.get(url)

    assert resp.status_code == 200
    data = resp.json()

    assert data["id"] == project_id
    assert data.get("title") == test_project["title"], (
        f"Заголовки не совпадают! Ожидалось: {test_project['title']}, "
        f"Получено: {data.get('title')}"
    )


def test_put_project_positive(test_project, client):
    """Обновление проекта: PUT + последующий GET для проверки."""
    project_id = test_project["id"]
    new_title = f"Updated Title {uuid.uuid4().hex[:6]}"
    url = f"{BASE_URL}/api-v2/projects/{project_id}"
    payload = {"title": new_title}

    resp = client.put(url, json=payload)
    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"

    data_put = resp.json()
    assert "id" in data_put, "В ответе PUT отсутствует поле 'id'"

    get_url = f"{BASE_URL}/api-v2/projects/{project_id}"
    resp_get = client.get(get_url)
    assert resp_get.status_code == 200, (
        f"Ожидался 200 для GET, получен {resp_get.status_code}"
    )

    data_get = resp_get.json()
    assert data_get.get("title") == new_title, (
        f"Название не обновилось! Ожидалось: {new_title}, "
        f"Получено: {data_get.get('title')}"
    )

    print(
        "✅ Проект обновлён, проверка через GET подтвердила изменение title."
    )


def test_put_project_negative_invalid_payload(test_project, client):
    """Некорректные данные для PUT. Проверка текста ошибки."""
    project_id = test_project["id"]
    resp = client.put(
        f"{BASE_URL}/api-v2/projects/{project_id}", json={"title": 12345}
    )

    assert resp.status_code == 400, f"Ожидался 400, получен {resp.status_code}"

    error_text = resp.text.lower()
    assert "title must be a string" in error_text, (
        f"Неожиданный текст ошибки: {error_text}"
    )
    print(
        "✅ Тест на неверные данные пройден: получен 400 и верный текст ошибки."
    )


def test_get_project_negative_invalid_id(client):
    """Неверный ID: проверка 404 и текста."""
    resp = client.get(f"{BASE_URL}/api-v2/projects/fake-id-123")

    assert resp.status_code == 404, f"Ожидался 404, получен {resp.status_code}"

    assert "not found" in resp.text.lower() or "not_found" in resp.text, (
        f"Неверный текст ошибки для 404: {resp.text}"
    )
    print("✅ Тест на 404 пройден.")

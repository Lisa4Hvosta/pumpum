from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))

        all_links = driver.find_elements(By.TAG_NAME, "a")

        # Проверка количества ссылок
        assert len(all_links) == 9, (
            f"Ожидалось 9 ссылок, "
            f"но найдено: {len(all_links)}"
        )
        print("✅ Найдено ровно 9 ссылок.")

        for i, link in enumerate(all_links):
            assert link.is_displayed(), (
                f"Ссылка №{i} не отображается "
                f"на странице!"
            )
        print("✅ Все ссылки отображаются.")

        first_link_text = all_links[0].text.strip()
        assert "1" in first_link_text, (
            f"В тексте первой ссылки ожидалось '1', "
            f"но было: '{first_link_text}'"
        )
        print(f"✅ Текст первой ссылки корректен: '{first_link_text}'")

    finally:
        driver.quit()

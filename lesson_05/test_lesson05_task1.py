from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online")
        original_url = driver.current_url

        assert original_url == "https://httpbin.qa-territory.online/", (
            "Неверная главная страница"
        )

        link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "HTML Form"))
        )
        link.click()

        wait.until(lambda d: d.current_url != original_url)
        new_url = driver.current_url

        # Разбивка assert на две строки для соблюдения PEP8
        assert new_url.endswith("/forms/post"), (
            "URL не изменился на /forms/post"
        )

        print("✅ Навигация успешна.")

    finally:
        driver.quit()

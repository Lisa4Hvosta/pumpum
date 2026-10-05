from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")
        original_url = driver.current_url

        custname_field = wait.until(
            EC.element_to_be_clickable((By.NAME, "custname"))
        )
        custname_field.send_keys("Лиса")

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
                )
        )

        button_text = submit_button.text.strip()

        assert "Submit" in button_text, (
            f"На кнопке ожидалось слово 'Submit', "
            f"а было: '{button_text}'"
        )

        submit_button.click()

        wait.until(lambda d: d.current_url != original_url)
        new_url = driver.current_url

        assert new_url != original_url, (
            f"URL не изменился! "
            f"Текущий URL: {new_url}"
        )

        print("✅ Форма отправлена, URL изменился.")

    finally:
        driver.quit()

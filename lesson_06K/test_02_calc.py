from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1. Откройте страницу:
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)
# 2. В поле ввода по локатору #delay введите значение 45.
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
# 3. Нажмите на кнопки:
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        xpath = f"//span[text()='{button}']"
        browser.find_element(By.XPATH, xpath).click()
    result = WebDriverWait(browser, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
# 4. Проверьте (assert),
# что в окне отобразится результат 15 через 45 секунд.
    assert result

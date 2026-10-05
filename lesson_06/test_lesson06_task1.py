from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    wait = WebDriverWait(driver, 40)

    start_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    wait.until(EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))

    element = driver.find_element(By.ID, "finish")

    driver.save_screenshot("lesson_06/full_screen.png")

    assert element.text == "Hello World!"

    driver.quit()

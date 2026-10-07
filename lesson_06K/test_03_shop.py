from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    # 1. Открываем сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        driver.get("http://www.saucedemo.com/")
        # 2. Авторизуемся как пользователь standard_user
        user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")
        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "add-to-cart-sauce-labs-backpack")
            )
        )
        # 3. Добавляем в корзину товары:
        backpack = driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-backpack"
        )
        backpack.click()
        shirt = driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        shirt.click()
        onesie = driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-onesie"
        )
        onesie.click()
        # 4. Переходим в корзину.
        shopping_cart_container = driver.find_element(
            By.ID, "shopping_cart_container"
        )
        shopping_cart_container.click()
        # 5. Нажимаем Checkout.
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        # 6. Заполняем форму своими данными:
        wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Anastasia")
        last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Lisa")
        postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys("108302")
        # 7. Нажимаем кнопку Continue.
        continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()
        # 8. Прочитайте со страницы итоговую стоимость (Total).
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        print(f"Получена итоговая стоимость: {total_text}")
        # 9. Проверяем, что итоговая сумма равна $58.29.
        expected_total = "Total: $58.29"
        assert (
            total_text == expected_total
        ), f"Ошибка! Итоговая сумма не совпадает. Ожидалось: {
            expected_total
        }, Получено: {total_text}"
        print("Проверка пройдена: итоговая сумма = $58.29")

    except AssertionError as e:
        print(f"\n Ошибка проверки {e}")
        raise
    # 10. Закрываем браузер
    finally:
        driver.quit()

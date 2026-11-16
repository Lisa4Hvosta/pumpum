"""UI-тест магазина Sauce Demo с отчётом Allure."""

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from pages.shop_page import CartPage, ShopPage


@pytest.fixture
def driver() -> WebDriver:
    """Фикстура браузера: открывает Firefox перед тестом и закрывает после."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Покупка товаров с проверкой итоговой суммы")
@allure.description(
    "Авторизуемся под standard_user, добавляем в корзину рюкзак, футболку "
    "и слоубоди, заполняем данные покупателя и проверяем, что итоговая "
    "сумма заказа равна $58.29."
)
@allure.feature("Магазин Sauce Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver: WebDriver) -> None:
    """Проверяет полный сценарий покупки и итоговую сумму заказа."""
    shop_page: ShopPage = ShopPage(driver, "https://www.saucedemo.com/")

    with allure.step("Открываем сайт и авторизуемся"):
        shop_page.open()
        shop_page.authorization()

    with allure.step("Добавляем товары в корзину"):
        shop_page.get_add_product()

    cart_page: CartPage = CartPage(driver, "https://www.saucedemo.com/cart.html")
    with allure.step("Оформляем заказ"):
        cart_page.get_shopping_card()
        cart_page.get_checkout()
        cart_page.get_form()
        cart_page.get_continue()

    with allure.step("Проверяем итоговую сумму заказа"):
        total: str = cart_page.get_result()
        assert total == "Total: $58.29"

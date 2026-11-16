"""Page Object'ы магазина Sauce Demo: авторизация/каталог и корзина."""

from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = Tuple[str, str]
"""Тип локатора: пара (метод поиска, значение), например (By.ID, 'login-button')."""


class ShopPage:
    """Страница авторизации и каталога магазина Sauce Demo."""

    LOGIN_INPUT: Locator = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT: Locator = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON: Locator = (By.CSS_SELECTOR, "#login-button")
    ADD_BACKPACK_BUTTON: Locator = (By.NAME, "add-to-cart-sauce-labs-backpack")
    ADD_T_SHIRT_BUTTON: Locator = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_BUTTON: Locator = (By.NAME, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Инициализирует страницу, создаёт явное ожидание и открывает URL.

        :param driver: экземпляр веб-драйвера Selenium.
        :param url: адрес страницы, которую нужно открыть.
        """
        self.driver = driver
        self.url = url
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    @allure.step("Открываем страницу оформления заказа")
    def open(self) -> None:
        """Открывает страницу оформления заказа. Ничего не возвращает."""
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Авторизуемся под standard_user")
    def authorization(self) -> None:
        """Заполняет логин и пароль, нажимает кнопку входа. Ничего не возвращает."""
        login_input: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_INPUT)
        )
        login_input.clear()
        login_input.send_keys("standard_user")

        password_input: WebElement = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys("secret_sauce")

        login_button: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()

    @allure.step("Добавляем в корзину рюкзак, футболку и слоубоди")
    def get_add_product(self) -> None:
        """Кликает по кнопкам добавления трёх товаров в корзину. Ничего не возвращает."""
        self.wait.until(
            EC.presence_of_element_located(self.ADD_BACKPACK_BUTTON)
        ).click()
        self.wait.until(
            EC.presence_of_element_located(self.ADD_T_SHIRT_BUTTON)
        ).click()
        self.wait.until(
            EC.presence_of_element_located(self.ADD_ONESIE_BUTTON)
        ).click()


class CartPage:
    """Корзина и страницы оформления заказа магазина Sauce Demo."""

    SHOPPING_CART_BUTTON: Locator = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON: Locator = (By.ID, "checkout")
    FIRST_NAME_INPUT: Locator = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT: Locator = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT: Locator = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON: Locator = (By.CSS_SELECTOR, "#continue")
    TOTAL_VALUE: Locator = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Инициализирует страницу корзины и открывает URL.

        :param driver: экземпляр веб-драйвера Selenium.
        :param url: адрес страницы, которую нужно открыть.
        """
        self.driver = driver
        self.url = url
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    @allure.step("Открываем корзину")
    def get_shopping_card(self) -> None:
        """Кликает по иконке корзины. Ничего не возвращает."""
        self.wait.until(
            EC.presence_of_element_located(self.SHOPPING_CART_BUTTON)
        ).click()

    @allure.step("Нажимаем Checkout")
    def get_checkout(self) -> None:
        """Переходит к оформлению заказа. Ничего не возвращает."""
        self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BUTTON)
        ).click()

    @allure.step("Заполняем данные покупателя")
    def get_form(self) -> None:
        """Заполняет имя, фамилию и индекс. Ничего не возвращает."""
        first_name_input: WebElement = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_input.send_keys("Anastasia")

        last_name_input: WebElement = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        )
        last_name_input.send_keys("Lisa")

        postal_code_input: WebElement = self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE_INPUT)
        )
        postal_code_input.send_keys("108243")

    @allure.step("Подтверждаем данные заказа")
    def get_continue(self) -> None:
        """Нажимает кнопку Continue. Ничего не возвращает."""
        self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BUTTON)
        ).click()

    @allure.step("Получаем итоговую сумму заказа")
    def get_result(self) -> str:
        """Ждёт появления итоговой суммы и возвращает её текст.

        :return: строка вида 'Total: $58.29'.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.TOTAL_VALUE, "Total: $58.29")
        )
        result_element: WebElement = self.driver.find_element(*self.TOTAL_VALUE)
        return result_element.text

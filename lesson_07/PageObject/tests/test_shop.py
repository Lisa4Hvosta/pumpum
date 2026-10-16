import pytest
from selenium import webdriver
from pages.shop_page import ShopPage
from pages.shop_page import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    shop_page = ShopPage(driver, "https://www.saucedemo.com/")
    shop_page.open()
    shop_page.authorization()
    shop_page.get_add_product()
    shop_page = CartPage(driver, "https://www.saucedemo.com/cart.html")
    shop_page.get_shopping_card()
    shop_page.get_checkout()
    shop_page.get_form()
    shop_page.get_continue()
    shop_page.get_total()
    shop_page.get_result()
    assert shop_page.get_result() == "Total: $58.29"

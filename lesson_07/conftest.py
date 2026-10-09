import pytest
from driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер для тестов: chrome, firefox, safari, edge",
    )


@pytest.fixture(scope="session")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = create_driver(browser_name)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")
    driver.add_cookie(
        {
            "name": "SESSION",
            "value": "OWVmYTk4YjItMTVjYy00YzZiLTk4ZTEtOGJhYzE4NTM2NTM5",
            "domain": "gitflic.ru",
        }
    )
    driver.add_cookie(
        {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
    )
    driver.refresh()
    yield driver
    driver.quit()

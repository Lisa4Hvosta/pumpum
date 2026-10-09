from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    cookie_user1 = "YzI5YjVhMDYtMGFlNC00NjQ2LWIxNGQtMGZkOTBmMjE5OWIz"
    cookie_user2 = "MmQ0NzcyZjItNDY2YS00ZDkwLThkOWItNTQ5NzQ5NjE3ZWE2"
    url_user1 = "https://gitflic.ru/user/testpoiuytrewq"
    url_user2 = "https://gitflic.ru/user/testpoiuytrewq1"

    try:
        driver.get("https://gitflic.ru/")

        driver.add_cookie({
            "name": "SESSION",
            "value": cookie_user1,
            "domain": "gitflic.ru"
        })

        driver.refresh()

        driver.get(url_user1)
        url1 = driver.current_url
        print(f"URL пользователя 1: {url1}")

        driver.delete_all_cookies()

        driver.add_cookie({
            "name": "SESSION",
            "value": cookie_user2,
            "domain": "gitflic.ru"
        })

        driver.refresh()

        driver.get(url_user2)
        url2 = driver.current_url
        print(f"URL пользователя 2: {url2}")

        assert url1 != url2, (
            f"URL совпадают: {url1} == {url2}. "
            "Авторизация не сработала или профили идентичны."
        )
        print("✅ Тест пройден: URL пользователей различаются.")

    finally:
        driver.quit()

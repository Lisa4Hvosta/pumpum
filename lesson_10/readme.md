# ДЗ №10: Allure в проекте с Page Object

UI-тест магазина [Sauce Demo](https://www.saucedemo.com/): авторизация,
добавление товаров в корзину, оформление заказа и проверка итоговой суммы.
Каждый шаг и проверка размечены через Allure, отчёт формируется автоматически.

## Структура проекта

- `pages/shop_page.py` — Page Object'ы страниц (авторизация, каталог, корзина);
- `tests/test_shop.py` — тест с фикстурой браузера;
- `requirements.txt` — зависимости.

## Установка

1. Нужен Python 3.10+.
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Установить Allure Commandline (потребуется Java 8+):
   - Windows: `scoop install allure`
   - macOS: `brew install allure`
   - Linux: `sudo apt install allure`
4. Проверить установку: `allure --version`.

## Запуск тестов с формированием отчёта

Из корня проекта:

```bash
pytest tests/test_shop.py --alluredir=allure-results
```

Результаты тестов (в формате JSON) появятся в папке `allure-results`.
В git её пушить не нужно — она есть в `.gitignore`.

## Просмотр отчёта

Вариант 1 — открыть отчёт сразу (не создаёт файлов):

```bash
allure serve allure-results
```

Вариант 2 — сгенерировать отчёт в папку и открыть его:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

В отчёте видно: название и описание теста, severity, шаги с описаниями
(`@allure.step`) и вложенные шаги проверок (`with allure.step`).

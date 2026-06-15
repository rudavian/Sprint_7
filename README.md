# Sprint_7

Автотесты API для учебного сервиса Яндекс Самокат.

## Что проверяется

В проекте реализованы проверки для обязательной части финального проекта 7 спринта:

- создание курьера;
- логин курьера;
- создание заказа с разными вариантами цвета;
- получение списка заказов.

## Структура проекта

```text
Sprint_7/
├── README.md
├── requirements.txt
├── .gitignore
├── conftest.py
├── urls.py
├── data.py
├── helpers.py
├── api_client.py
├── tests/
│   ├── test_create_courier.py
│   ├── test_login_courier.py
│   ├── test_create_order.py
│   └── test_get_orders.py
└── allure_results/
```

## Стек проекта

- Python
- pytest
- requests
- allure-pytest

## Ссылки на сервис

- Сервис: `https://qa-scooter.praktikum-services.ru/`
- Документация API: `https://qa-scooter.praktikum-services.ru/docs/`

## Запуск на Windows

Открой PowerShell в папке проекта:

```powershell
cd D:\Code_Project\Sprint_7
```

Создай виртуальное окружение:

```powershell
py -3 -m venv .venv
```

Активируй виртуальное окружение:

```powershell
.\.venv\Scripts\Activate.ps1
```

Установи зависимости:

```powershell
pip install -r requirements.txt
```

Запусти тесты:

```powershell
pytest -v
```

Запусти тесты с генерацией результатов Allure:

```powershell
pytest -v --alluredir=allure_results --clean-alluredir
```

Открой Allure-отчёт локально, если установлен Allure CLI:

```powershell
allure serve allure_results
```

## Отчёт Allure

Папка `allure_results/` добавлена в репозиторий и содержит результаты последнего успешного запуска тестов.

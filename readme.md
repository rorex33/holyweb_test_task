# HolyWeb Test Task (Django)
Тестовое задание для HolyWeb - система записи к врачу.

## Структура проекта:
holyweb_test_task/
    .venv/ # Виртуальное окружение Python
    .gitignore # Игнорируемые файлы (для git)
    requirements.txt # Зависимости
    app/ - директория основной части проекта
        manage.py # Управляющий скрипт
        db.sqlite3 # База данных (SQLite)
        app/ # Настройки проекта
            settings.py # Конфигурация Django
        api/ # API компоненты
            models.py # Модели данных
            views.py # Логика API
            urls.py # Маршруты API


## 🚀 Быстрый запуск

### 1. Активация окружения:
> `source .venv/bin/activate`  # Linux/MacOS
> `.venv\Scripts\activate`     # Windows

### 2. Установка зависимостей:
> `pip install -r requirements.txt`

### 3. Настройка базы данных (для SQLite):
> `python manage.py migrate`


superuser data:
    Username: admin
    Email address: admin@example.com
    Password: admin

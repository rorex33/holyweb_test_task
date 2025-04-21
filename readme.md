# HolyWeb Test Task (Django)
Тестовое задание для HolyWeb - система записи к врачу.

## Структура проекта:
holyweb_test_task/

├── .venv/ - виртуальное окружение Python
    
├── .gitignore - игнорируемые файлы (для git)
    
├── requirements.txt - Зависимости
    
├── app/ - директория основной части проекта
    
└── manage.py - управляющий скрипт
        
└── db.sqlite3 - база данных (SQLite)
        
└── app/ - настройки проекта
            
└── api/ - API компоненты


## Быстрый запуск

### 1. Активация виртуального окружения Python:
```
source .venv/bin/activate  # Linux/MacOS

.venv\Scripts\activate     # Windows
```

### 2. Установка зависимостей:
`pip install -r requirements.txt`

### 3. Настройка базы данных (для SQLite):
 `python manage.py migrate`


superuser data:
    Username: admin
    Email address: admin@example.com
    Password: admin

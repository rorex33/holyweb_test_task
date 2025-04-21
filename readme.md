# HolyWeb Test Task (Django)
Тестовое задание для HolyWeb - система записи к врачу.

## Структура проекта:
holyweb_test_task/

├── **.gitignore** - игнорируемые файлы (для git)
    
├── **requirements.txt** - список зависимостей
    
├── **app/** - директория основной части проекта
    
└── **manage.py** - управляющий скрипт
        
└── **db.sqlite3** - база данных (SQLite)
        
└── **app/** - настройки проекта
            
└── **api/** - API компоненты


## Быстрый запуск

### 1. Получение проекта с гит-хаба:
Создайте папку в удобнов вам месте, откройте её в консоли. Далее пропишите:

```
git clone https://github.com/rorex33/holyweb_test_task
```

### 2. Создание и активация виртуального окружения Python:
Перейдите в */holyweb_test_task*, затем пропишите:
```
# Linux/MacOS

python3 -m venv .venv       # создаём виртуальное окружение

source .venv/bin/activate   # активируем его
```

```
# Windows

py -m venv .venv

.venv\Scripts\activate
```

### 2. Установка зависимостей:
`pip install -r requirements.txt`

### 3. Настройка базы данных (для SQLite):
`python manage.py migrate`

### 4. Создание администратора:
Администратор по умолчанию:

**Username**: admin

**Email address**: admin@example.com

**Password**: admin

Вы можете создать своего администратора командой:
`python app/manage.py createsuperuser `

### 5. Запуск сервера:
`python app/manage.py runserver `

Готово, теперь вы можете отсылать запросы к серверу.
Сервер будет доступен по: http://127.0.0.1:8000

Управление сервером через админа будет доступна по: http://127.0.0.1:8000/admin

## API Endpoints

### Маршруты:

GET /api/doctors/ - получить список врачей
 
GET /api/appointments/?client_fullname=ФИО - получить список записей к врачам (ФИО через пробелы)

POST /api/appointments/create/?client_fullname=ФИО - создать запись 

**Добавление пользователя в базу данных происходит в момент создания записи к врачу!**

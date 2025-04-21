# HolyWeb Test Task (Django)
Тестовое задание для HolyWeb - система записи к врачу.

## Структура проекта:
holyweb_test_task/

├── **.gitignore** - игнорируемые файлы (для git)

├── **Doctor's appointment API.postman_collection.json** - коллекция запросов к серверу
    
├── **requirements.txt** - список зависимостей
    
├── **app/** - директория основной части проекта
    
└── **manage.py** - управляющий скрипт
        
└── **db.sqlite3** - база данных (SQLite)
        
└── **app/** - настройки проекта
            
└── **api/** - API компоненты


## Быстрый запуск

### 1. Получение проекта с гит-хаба:
Создайте папку в удобном вам месте, откройте её в консоли. Далее пропишите:

```
git clone https://github.com/rorex33/holyweb_test_task
```

### 2. Создание и активация виртуального окружения Python:
Перейдите в */holyweb_test_task*, затем пропишите:
```
# Linux/MacOS

python3.13 -m venv .venv       # создаём виртуальное окружение

source .venv/bin/activate      # активируем виртуальное окружение
```

```
# Windows

py -m venv .venv               # создаём виртуальное окружение

.venv\Scripts\activate         # активируем виртуальное окружение
```

### 2. Установка зависимостей:
`pip install -r requirements.txt`

### 3. Настройка базы данных (для SQLite):
Пропишите команду:
`python app/manage.py migrate`

### 4. Создание администратора:
Администратор по умолчанию:

**name**: admin

**password**: admin

**email**: admin@example.com

Вы можете создать своего администратора командой:
`python app/manage.py createsuperuser `

### 5. Запуск сервера:
`python app/manage.py runserver `

Готово, теперь вы можете отсылать запросы к серверу.
Сервер будет доступен по: http://127.0.0.1:8000

Управление сервером через админа будет доступно по: http://127.0.0.1:8000/admin

## API Endpoints

### Маршруты:

GET /api/doctors/ - получить список врачей
 
GET /api/appointments/?client_fullname=ФИО - получить список записей к врачам (ФИО через пробелы)

POST /api/appointments/create/?client_fullname=ФИО - создать запись 

Протестируем доступ к серверу: `curl http://127.0.0.1:8000/api/doctors/`

**Добавление пользователя в базу данных происходит в момент создания записи к врачу!**

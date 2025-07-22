# HotelSite — Django-приложение для онлайн-бронирования номеров

**HotelSite** — это веб-приложение, разработанное на Django, позволяющее пользователям регистрироваться, бронировать номера в отеле, управлять своими бронированиями и взаимодействовать с административной панелью.

## Функциональность

- Регистрация и авторизация пользователей
- Личный кабинет с просмотром и управлением бронированиями
- Просмотр доступных номеров
- Административная панель (Django Admin) для управления номерами и бронированиями
- Стилизация интерфейса с помощью Bootstrap

## Стек технологий

- **Backend**: Python, Django
- **База данных**: PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap
- **ORM**: Django ORM
- **Аутентификация**: встроенная система Django

## Установка и запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/leshka484/HotelSite.git
   cd HotelSite
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте базу данных для приложения в PostgreSQL

5. Добавьте в корень проекта файл .env с содержимым:
   ```
   POSTGRES_USER = # Имя пользователя PostgreSQL
   POSTGRES_PASSWORD = # Пароль пользователя PostgreSQL
   POSTGRES_HOST = localhost
   POSTGRES_DB = # Название БД
   ```

6. Примените миграции:
   ```bash
   cd hotel_site
   python3 manage.py migrate
   ```

7. (Опционально) Создайте суперпользователя:
   ```bash
   python3 manage.py createsuperuser
   ```

8. Запустите сервер разработки:
   ```bash
   python3 manage.py runserver
   ```

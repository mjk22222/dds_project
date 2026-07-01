# Веб-сервис для управления движением денежных средств (ДДС)

## Описание
Веб-приложение для учета и анализа финансовых операций компании/лица. Реализованы функции CRUD, фильтрация и управление справочниками с логическими зависимостями.

## Технологии
* Python 3.10+
* Django 5.2
* Django REST Framework
* PostgreSQL
* Bootstrap 5

## Инструкция по запуску
1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение:
   `python -m venv venv`
   `source venv/bin/activate` (или `venv\Scripts\activate` на Windows)
3. Установите зависимости:
   `pip install -r requirements.txt`
4. Настройте подключение к PostgreSQL в `config/settings.py`.
5. Примените миграции:
   `python manage.py migrate`
6. Создайте суперпользователя:
   `python manage.py createsuperuser`
7. Запустите сервер:
   `python manage.py runserver`
8. Перейдите по адресу http://127.0.0.1:8000/
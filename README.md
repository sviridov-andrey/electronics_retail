# Тестовое задание для старта трудоустройства

## Для работы с проектом необходимо выполнить следующие действия:
- Клонировать репозиторий.
- Установить и активировать виртуальное окружение 
- Установить зависимости pip install -r requirements.txt
- Создать файл .env, заполнить его данными из файла env.sample
- Создать базу данных в PostreSQL CREATE DATABASE <название базы>;
- Создать python manage.py makemigration и применить миграции python manage.py migrate
- Создать пользователя командой python manage.py csu
- Командой python manage.py runserver запустить локальный сервер
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.

## Поставлена задача:
Создайте веб-приложение с API-интерфейсом и админ-панелью.
Создайте базу данных, используя миграции Django.
Требования к реализации:

Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из трех уровней:

завод;
розничная сеть;
индивидуальный предприниматель.
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т. е. завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, ее уровень — 1.

Каждое звено сети должно обладать следующими элементами:
Название.
Контакты:
email,
страна,
город,
улица,
номер дома.
Продукты:
название,
модель,
дата выхода продукта на рынок.
Поставщик (предыдущий по иерархии объект сети).
Задолженность перед поставщиком в денежном выражении с точностью до копеек.
Время создания (заполняется автоматически при создании).
Сделать вывод в админ-панели созданных объектов.
На странице объекта сети добавить:

ссылку на «Поставщика»;
фильтр по названию города;
admin action, очищающий задолженность перед поставщиком у выбранных объектов.
Используя DRF, создать набор представлений:
CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»).

Добавить возможность фильтрации объектов по определенной стране.

Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.


## Основной стэк
- python==3.11.1
- Django==5.0.3
- djangorestframework==3.14.0
- psycopg2==2.9.9

В описании обнарудены взаимоисключающие условия:
- Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии)
- Поставщик (предыдущий по иерархии объект сети).
Иерархия реализована, как в описании: завод; розничная сеть; индивидуальный предприниматель, через внешние ключи. 
Завод без поставщика, розничная сеть видит только завод, индивидуальный предприниматель видит только розничную сеть.

Все остальные условия были реализованы по заданию.
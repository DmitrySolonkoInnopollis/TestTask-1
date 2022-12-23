# Тестовое задание для Fortech
___
Нужно сделать простой сервис проведения тестирования по каким-либо темам. Т.е. есть тесты с 
вариантами ответов, один или несколько вариантов должны быть правильными. Тесты 
группируются в наборы тестов, которые затем пользователь может проходить и видеть свой 
результат
___

## Запуск проекта
* Клонировать репозиторий: ```https://github.com/OptikRUS/quiz```
* Установить зависимости: ```pip install -r requirements.txt```
* Сделать миграции:
  * ```python manage.py makemigrations```
  * ```python manage.py migrate```
* Создать суперпользователя ```python manage.py createsuperuser```
* Запустить проект ```python manage.py runserver```

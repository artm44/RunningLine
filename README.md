# RunningLine
 
## Описание проекта
RunningLine - это Django приложения для создания бегущей строки.

## Технологический стек
- **Язык программирования:** Python
- **Фреймворк** Django
- **Создание видео:** OpenCV 

## Установка
1. Клонируйте репозиторий: `git clone --branch=django-app https://github.com/artm44/RunningLine.git`
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте виртуальное окружение:
- На Windows: `venv\Scripts\activate`
- На Linux/Mac: `source venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Перейдите в каталог приложения: `cd runningline`
6. Произведите миграцию БД: `python manage.py migrate` 
7. Запустите приложение: `python manage.py runserver`

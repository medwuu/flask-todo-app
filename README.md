# ![Flask-todo-app](/app/static/images/preview.png)

[![Python v3.11+](https://img.shields.io/badge/Python-v3.11+-ffde71)](https://www.python.org/)
[![Flask v3.1.0](https://img.shields.io/badge/Flask-v3.1.0-3eaabf)](https://pypi.org/project/Flask/)
[![SQLAlchemy v.2.0.37](https://img.shields.io/badge/SQLAlchemy-v.2.0.37-d94b4b)](https://pypi.org/project/SQLAlchemy/)
[![Jinja2 v3.1.5](https://img.shields.io/badge/Jinja2-v3.1.5-d94b4b)](https://pypi.org/project/Jinja2/)
[![JQuery v.3.7.1](https://img.shields.io/badge/JQuery-v.3.7.1-0769ad)](https://jquery.com/)
[![Bootstrap v.5.3.3](https://img.shields.io/badge/Bootstrap-v.5.3.3-720ff4)](https://getbootstrap.com/)

## Что это? 🤔
**Flask-todo-app** – небольшое веб-приложение, написанное в процессе изучения Flask.

Оно поможет организовать рабочие и личные задачи в виде удобного списка, а прогресс-бар вверху поможет отслеживать свои успехи 💯

## Преимущества 🤓:
- 🫸🏻 Система пользователей;
- ⚙️ Настройки пользователя (смена пароля, имени и email'а);
- 🌟 Анимации добавления, удаления, изменения задачи;
- 🔝 Сортировка задач по дате добавления;
- 📊 Динамический прогресс-бар. Считает процент выполненных задач;
- 🏛️ Минималистичный дизайн, вдохновлённый [ShaifArfan](https://github.com/ShaifArfan/react-todo-app)

## Системные требования:
- [Python 3](https://www.python.org/downloads/)
- [PIP 3](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/) или другой редактор кода для удобной работы


## Установка:
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/medwuu/flask-todo-app.git
    cd flask-todo-app
    ```

2. Создайте и активируйте вируальное окружение:
* Windows:
    ```bash
    python3 -m venv .venv
    .venv\Scripts\activate
    ```
* Linux:
    ```bash
    : Если модуль venv не установлен
    sudo apt install python3-venv -y

    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Инициализировать и создать базу данных (при использовании SQLite):
    ```bash
    flask db init
    flask db upgrade
    ```

5. Запустить приложение:
    ```bash
    flask run
    ```
    Оно будет доступно по адресу http://127.0.0.1:5000/
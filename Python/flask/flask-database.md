# **Работа с базами данных в Flask**

<br>

Flask не имеет встроенной поддержки баз данных, но предоставляет удобные инструменты для интеграции. Для работы с базами данных часто используется библиотека SQLAlchemy, а для более простой интеграции в Flask — расширение Flask-SQLAlchemy.

---

## **Начало работы**

Для начала было бы неплохо установить библиотеку для работы с Базой данных во Flask. Как уже было сказано ранее, для постоянного хранения файлов рекомендуется использовать SQLAlchemy систему управления базой данных (СУБД).

Для установки SQLAlchemy воспользуемся pip:

```bash
pip install flask flask-sqlalchemy
```

---

<br>

## **Основные понятия SQLAlchemy**

**ORM (Object-Relational Mapping)** — позволяет работать с базами данных через объекты Python.

- Модель — класс Python, который соответствует таблице в базе данных.
- Сессия — интерфейс для выполнения операций с базой данных (CRUD).

---

<br>


## **Подключение базы данных**

Flask-SQLAlchemy поддерживает различные базы данных (SQLite, PostgreSQL, MySQL, и др.). Например, подключение SQLite:

```python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Указываем URI базы данных (SQLite в данном случае)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем предупреждения
db = SQLAlchemy(app)

```

---

<br>

## **Создание модели**

Модель описывает таблицу в базе данных. 

Пример модели:

```python
class User(db.Model):
    __tablename__ = 'users'  # Имя таблицы
    id = db.Column(db.Integer, primary_key=True)  # Колонка ID
    username = db.Column(db.String(80), unique=True, nullable=False)  # Колонка username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Колонка email

    def __repr__(self):
        return f"<User {self.username}>"

```

Каждое свойство модели — это колонка таблицы в базе данных.

---

<br>

## Методы работы с БД

### Создание базы данных

```python
with app.app_context():
    db.create_all()
```

Это создаст файл app.db (в случае SQLite) с таблицей users.

<br>

### Добавление данных

```python
@app.route('/add_user')
def add_user():
    user = User(username='JohnDoe', email='john@example.com')
    db.session.add(user)  # Добавляем объект в сессию
    db.session.commit()   # Сохраняем изменения
    return "User added!"

```

<br>

### Получение данных

Общий пример получения ВСЕХ данных:

```python
@app.route('/users')
def get_users():
    users = User.query.all()  # Получаем всех пользователей
    return {user.id: user.username for user in users}

```

Персонализированные пример получения данных о конкретном пользователе по его ID:

```python
@app.route('/user/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)  # Получаем пользователя или 404
    return {"id": user.id, "username": user.username, "email": user.email}

```

<br>


### Обновление данных

```python
@app.route('/update_user/<int:id>')
def update_user(id):
    user = User.query.get_or_404(id)
    user.username = "UpdatedName"  # Изменяем поле
    db.session.commit()  # Сохраняем изменения
    return f"User {id} updated!"

```

<br>


### Удаление данных

```python
@app.route('/delete_user/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)  # Удаляем объект
    db.session.commit()  # Сохраняем изменения
    return f"User {id} deleted!"

```

---

<br>

## **Пример проекта**

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Модель
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}

# Маршрут для добавления пользователя
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user = User(username=data['username'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# Маршрут для получения всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)

```
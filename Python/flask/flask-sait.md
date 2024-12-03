# Flask сайты


## Работа с маршрутами

Используйте декоратор `@app.route()` для определения маршрута:
```python
@app.route("/hello")
def hello():
    return "This is a new route!"
```

#### Параметры URL

Вы можете передавать параметры через URL:
```python
@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"
```

---

<br>

## Шаблоны и работа с HTML

Flask использует систему шаблонов **Jinja2**, которая поддерживает вставку Python-кода в HTML.

##### Пример HTML-шаблона:

Файл `templates/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

Подробнее про html теги можно узнать [здесь](../../HTML/).

Функция для рендеринга шаблона:

```python
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html", title="My App", name="Flask")
```

---

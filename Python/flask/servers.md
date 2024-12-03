# Flask для серверов

> [!NOTE]
> Flask идеально подходит для создания REST API благодаря своей гибкости и легкости. 
> 
> Он позволяет обрабатывать запросы с различными методами, такими как *GET*, *POST*, *PUT*, *PATCH* и *DELETE*.


## **Сложности, с которыми можно столкнуться**

1. **Аутентификация и авторизация**: Убедитесь, что к API имеют доступ только авторизованные пользователи.
   
2. **Валидация данных**: Неправильный ввод данных может привести к сбоям или ошибкам. Используйте библиотеки, такие как marshmallow или pydantic.

3. **Ошибки и их обработка**: API должен возвращать понятные ошибки (например, 404, 400) с объяснением.

4. **Производительность**: При большом количестве запросов может понадобиться оптимизация кода и базы данных.

5. **Документация**: REST API должен быть хорошо задокументирован. Используйте такие инструменты, как Swagger или Postman.

---

<br>

## **Пример REST API сервера**

### Код сервера

```python
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Простая база данных в виде списка
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Build an API", "done": False},
]

# Утилита для поиска задачи по ID
def find_task(task_id):
    return next((task for task in tasks if task["id"] == task_id), None)

# GET: Получение всех задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# GET: Получение задачи по ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404, description="Task not found")
    return jsonify(task)

# POST: Создание новой задачи
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400, description="Invalid data")
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": request.json["title"],
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# PUT: Обновление задачи полностью
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404, description="Task not found")
    if not request.json or 'title' not in request.json or 'done' not in request.json:
        abort(400, description="Invalid data")
    task['title'] = request.json['title']
    task['done'] = request.json['done']
    return jsonify(task)

# PATCH: Частичное обновление задачи
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def patch_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404, description="Task not found")
    if not request.json:
        abort(400, description="Invalid data")
    if 'title' in request.json:
        task['title'] = request.json['title']
    if 'done' in request.json:
        task['done'] = request.json['done']
    return jsonify(task)

# DELETE: Удаление задачи
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)
    if task is None:
        abort(404, description="Task not found")
    tasks.remove(task)
    return jsonify({"message": "Task deleted"})

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True)

```


### Описание работы

**Функции для каждого метода:**

- `GET /tasks`: Возвращает все задачи.
- `GET /tasks/<id>`: Возвращает задачу с указанным ID.
- `POST /tasks`: Создает новую задачу, принимает JSON.
- `PUT /tasks/<id>`: Полностью обновляет задачу (перезаписывает все поля).
- `PATCH /tasks/<id>`: Обновляет только указанные поля.
- `DELETE /tasks/<id>`: Удаляет задачу с указанным ID.

**Обработка ошибок:**

- `404`: Возвращается, если задача не найдена.
- `400`: Возвращается при некорректных данных.

**Формат данных:**

API использует JSON как формат ввода и вывода.
Данные обрабатываются через request.json.
# **Работа с SQLite базой данных в python**

## Содержание

1. [Введение](./sqlite3.md#введение)
2. [Язык SQL](./sqlite3.md#язык-sql)
3. [Основные методы sqlite3](./sqlite3.md#основные-методы-sqlite3)
4. [Готовые реализации](./sqlite3.md#готовые-реализации)

<br><br>

## Введение

## Язык SQL 

## Основные методы sqlite3

Для начала работы с базой данные необходимо дял начала импортировать библиотеку `sqlite3`.

```python
# импорт бибилиотеки
import sqlite3 as sql
```




## Готовые реализации

В процессе разработки возникают проблемы, после их решения не плохо было бы сохранить какие-то части кода и комментарии для них.

Вот пример нескольких из них:

Функция создания локальной БД и таблицы в ней, если такая отсутствует, в противном случае подключиться к ней:

```python

def create_database(name_db:str) -> None:
    db = sql.connect(name_db)
    # создаем курсор
    cursor = db.cursor()

    # создание таблицы
    cursor.execute("""CREATE TABLE IF NOT EXISTS name_table(
    id INTEGER,
    name TEXT,
    age INTEGER,
    login TEXT,
    password TEXT
    )
    """)

    # сохранить
    db.commit()

```

Функция для изъятия данных из таблицы по какому-то ключу. Вернет кортеж данных. Для выполнения запроса используется все тот же SQL.

```python

# вернет кортеж с данными из базы данных
def get_data_from_database(name_db:str, data) -> tuple:
    
    db = sql.connect(name_db)
    cursor = db.cursor()
    
    cursor.execute(
        f"""SELECT * FROM {name_db} WHERE id={data}"""
    )
    
    # вернуть одно вхождение
    return cursor.fetchone()

```

Функция добавления каких-либо данных в БД:

```python

# Важно помнить о типе данных, которые устанавливали при создании БД
def add_data_in_database(name_db:str, data, add_data) -> None:
    
    db = sql.connect(name_db)
    cursor = db.cursor()
    
    cursor.execute(
        f"""INSERT INTO {name_db} VALUES (id={data}, name='{add_data}')"""
    )
    
    # сохраняем
    db.commit()

```

Функция изменения данных в БД:

```python

def update_data(name_db:str, data, new_data):
    db = sql.connect(name_db)
    cursor = db.cursor()
    
    cursor.execute(
        f"""UPDATE {name_db} SET name='{new_data}' WHERE id={data}"""
    )
    
    # сохранить
    db.commit()

```

Функция удаления каких-либо данных из БД:

```python

# удалить какие-то данных по параметру
def deleteData(login:str) -> None:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
        DELETE FROM users WHERE login='{login}'
    """)
    
    db.commit()
    db.close()

```

Получение определенной строки из таблицы БД:

```python
# получить строку в формате массива по параметру из таблицы БД
def getAllData() -> list:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    data = cursor.execute(f"""
        SELECT login FROM users
    """)

    
    return [i[0] for i in data.fetchall()]

```


<br><br>

<br><br>

###### 17.10.2024

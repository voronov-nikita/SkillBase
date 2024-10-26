# **Работа с SQLite базой данных в python**

## Содержание

1. [Введение](./sqlite3.md#введение)
2. [Язык SQL](./sqlite3.md#язык-sql)
3. [Основные методы sqlite3](./sqlite3.md#основные-методы-sqlite3)
4. [Готовые реализации](./sqlite3.md#готовые-реализации)

<br><br>

## Введение

База данных - это невероятно удобная вещь, когда нужно безопастно хранить данные в долгострочной памяти. Разумеется, что есть вариант с написание кода, который будет парсить данные напрямую из какого-нибудь текстового файлика и иметь возмость зашифровать данные пользователей, но это очень неустойчивая структура, хотя бы потому что остается возможность  потерять данные при ошибке программы. *SQLite* - это одна из самых простых баз данных, которую можно расположить локально у себя на устройтве и не боятся, что ваши данные перехватят или сервер будет взломан.

## Язык SQL 

SQL является довольно понятным языком запросов, т.к все команды исполняются на понятном человеку языком. К примеру:

```sql

SELECT * FROM table WHERE id=0;

```

Буквально можно перевести этот запрос как: 
Выбрать все значения из таблицы table, где id равен 0.

На мой взягляд ничего сложного.

Можно выделить несколько основных команд языка SQL:

| Команда | Действие                                    |
| ------------------ | ------------------------------------------- |
| **CREATE TABLE**        | Создать таблицу |
| **DROP TABLE**        | Удалить таблицу |
| **SELECT**        | Выбрать что-то откуда-то |
| **INSERT**        | Добавить что-то куда-то |
| **UPDATE**        | Обновить что-то где-то |
| **DELET**        | Удалить что-то откуда-то |
| **INSERT**        | Добавить что-то куда-то |
| **WHERE**        | фильтр "ГДЕ". Применяется  к SELECT, UPDATE, DELETE |
| **WHERE**        | фильтр "ГДЕ". Применяется  к SELECT, UPDATE, DELETE |





## Основные методы sqlite3

Для начала работы с базой данных SQLite необходимо дял начала импортировать специальную библиотеку `sqlite3`.

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

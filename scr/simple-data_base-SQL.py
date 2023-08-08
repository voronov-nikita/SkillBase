import sqlite3 as sql

def create_database(name_db:str):
    # подключиться к базы данных
    # если ее нет, то создать новую
    db = sql.connect(name_db)
    # создаем курсор
    cursor = db.cursor()

    # заменить имя {name_table} на что-то другое
    # заменить данные в этой талице
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
    

# получение всех данных из базы данных {name_db}
# для опознания некоторой строки используеться {data}, как признак отличия (id пользователя к примеру)
# вернет кортеж с данными из базы данных
def get_data_from_database(name_db:str, data) -> tuple:
    
    db = sql.connect(name_db)
    cursor = db.cursor()
    
    cursor.execute(
        f"""SELECT * FROM {name_db} WHERE id={data}"""
    )
    
    # вернуть одно вхождение
    return cursor.fetchone()


# добавить данные в базу данных {name_db}
# для опознания некоторой строки используеться {data}, как признак отличия (id пользователя к примеру)
# данные, которые нужно добавить -> {add_data}
# Важно помнить о типе данных, которые устанавливали при создании БД
def add_data_in_database(name_db:str, data, add_data):
    
    db = sql.connect(name_db)
    cursor = db.cursor()
    
    cursor.execute(
        f"""INSERT INTO {name_db} VALUES (id={data}, name='{add_data}')"""
    )
    
    # сохраняем
    db.commit()

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

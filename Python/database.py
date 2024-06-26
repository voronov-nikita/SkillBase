import sqlite3


# Базово создать базу данных с именем {...} и с данными {id}{...}{...}
def createDataBase() -> None:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    # только пример того, как может выглядеть БД
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    
    db.commit()
    db.close()


# добавить какие-то данных в БД по параметру
def addData(login:str, password:str) -> str:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
        INSERT INTO users(login, password) VALUES('{login}', '{password}')
    """)
    
    db.commit()
    db.close()
    
    return "Success"


# получить полную информацию только об одной конкретной строчке  
def getOneData(login:str) -> str:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    data = cursor.execute(f"""
        SELECT password FROM users WHERE login='{login}'
    """)
    
    
    return data.fetchone()[0]


# получения списка какиех-то данных
def getAllData() -> list:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    data = cursor.execute(f"""
        SELECT login FROM users
    """)

    
    return [i[0] for i in data.fetchall()]


# удалить какие-то данных по параметру
def deleteData(login:str) -> None:
    
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
        DELETE FROM users WHERE login='{login}'
    """)
    
    db.commit()
    db.close()
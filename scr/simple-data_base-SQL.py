# добавить данные в базу данных {name_db}
# для опознания некоторой строки используеться {data}, как признак отличия (id пользователя к примеру)
# данные, которые нужно добавить -> {add_data}

    
    
# Обновление данных в БД {name_bd}
# для опознания некоторой строки используеться {data}, как признак отличия (id пользователя к примеру)
# данные, которые нужно добавить -> {new_data}
def update_data(name_db:str, data, new_data):
    db = sql.connect(name_db)
    cursor = db.cursor()
    
    cursor.execute(
        f"""UPDATE {name_db} SET name='{new_data}' WHERE id={data}"""
    )
    
    # сохранить
    db.commit()

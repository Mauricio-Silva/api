import sqlite3, uuid
# cSpell:disable

PATH = "./database.db"

connection = sqlite3.connect(PATH)
database = connection.cursor()
database.execute("DROP TABLE IF EXISTS pessoa")
database.execute("CREATE TABLE pessoa (name TEXT)")
connection.commit()
connection.close()


def insert_name(name: str) -> None:
    connection = sqlite3.connect(PATH)
    database = connection.cursor()
    database.execute(f"INSERT INTO pessoa VALUES ('{name}')")
    connection.commit()
    connection.close()


def get_one_name(name: str) -> str:
    connection = sqlite3.connect(PATH)
    database = connection.cursor()
    query = database.execute(f"SELECT name FROM pessoa WHERE name='{name}'")
    name = query.fetchone()
    connection.close()
    return name


def get_all_names() -> list:
    connection = sqlite3.connect(PATH)
    database = connection.cursor()
    query = database.execute("SELECT * FROM pessoa")
    all_names = query.fetchall()
    all_names = [name[0] for name in all_names]
    connection.close()
    return all_names


def delete_name(name: str) -> None:
    connection = sqlite3.connect(PATH)
    database = connection.cursor()
    database.execute(f"DELETE FROM pessoa WHERE name='{name}'")
    connection.commit()
    connection.close()


def update_name(old_name: str, new_name:str) -> None:
    connection = sqlite3.connect(PATH)
    database = connection.cursor()
    database.execute(f"UPDATE pessoa SET name='{new_name}' WHERE name='{old_name}'")
    connection.commit()
    connection.close()


def get_all_ids() -> list:
    connection = sqlite3.connect(PATH)
    database = connection.cursor()
    query = database.execute("SELECT id FROM pessoa")
    all_ids = query.fetchall()
    all_ids = [objId[0] for objId in all_ids]
    connection.close()
    print(all_ids)
    return all_ids


def generate_id() -> uuid.UUID:
    all_ids = get_all_ids()
    if len(all_ids) == 0:   
        return uuid.uuid4()
    while True:
        objId = uuid.uuid4()
        if objId not in all_ids:
            break
    return objId
        
    

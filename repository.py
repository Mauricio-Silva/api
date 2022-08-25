import sqlite3
# cSpell:disable

PATH = "/home/mauricio/Programing/python/TETI/api/api_database.db"

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


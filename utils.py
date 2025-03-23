import sqlite3
from flask import url_for
from flask import session
from models.users import User

def get_boss_list_names():
    con = sqlite3.connect(f".{url_for('static', filename='data/data.db')}")

    SQL_SELECT = "SELECT name FROM bosses"
    query = con.execute(SQL_SELECT)
    data = query.fetchall()
    data = [
        item[0] for item in data
    ]

    return data


def get_boss_info_by_name(name):
    con = sqlite3.connect(f".{url_for('static', filename='data/data.db')}")

    SQL_SELECT = f"SELECT * FROM bosses WHERE name = '{name}'"
    query = con.execute(SQL_SELECT)
    data = query.fetchone()

    return data

def add_boss(data):
    con = sqlite3.connect(f".{url_for('static', filename='data/data.db')}")

    SQL_INSERT = f'INSERT INTO bosses (name, hp, location, loot, game_description, description, attack) VALUES ("{data[0]}", "{data[1]}", "{data[2]}", "{data[3]}", "{data[4]}", "{data[5]}", "{data[6]}")'
    query = con.execute(SQL_INSERT)
    con.commit()
    con.close()




def get_user_from_session():
    user_data = session.get("user", None)

    if user_data:
        id = user_data.get("id")
        username = user_data.get("username")
        return User(id, username)

    return None
import sqlite3

from flask import url_for


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
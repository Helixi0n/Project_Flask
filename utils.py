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


def add_planet(data):
    con = sqlite3.connect(f".{url_for('static', filename='data/data.db')}")

    SQL_INSERT = f'INSERT INTO planets (name, distance_from_sun, diameter, mass, atmosphere_composition, unique_features, geological_activity, satellites, climate_and_weather) VALUES ("{data[0]}", "{data[1]}", "{data[2]}", "{data[3]}", "{data[4]}", "{data[5]}", "{data[6]}", "{data[7]}", "{data[8]}")'
    query = con.execute(SQL_INSERT)
    con.commit()
    con.close()
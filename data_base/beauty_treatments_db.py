import sqlite3 as sq

from create_bot import bot
# from data_base.sqlite_db import base, cur


# def start_beauty_treatments():
#     global db_beauty_treatments, cur_beauty_treatments
#     # Если БД еще нет, она автоматически создается
#     db_beauty_treatments = sq.connect('database.db')
#     cur_beauty_treatments = db_beauty_treatments.cursor()
#     if db_beauty_treatments:
#         print('База данных db_beauty_treatments подключена')
#     db_beauty_treatments.execute('CREATE TABLE IF NOT EXISTS beauty_treatments(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
#     db_beauty_treatments.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()
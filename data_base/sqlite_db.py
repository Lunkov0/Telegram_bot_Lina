import sqlite3 as sq

from create_bot import bot

def sql_start():
    global base, cur
    # Если БД еще нет, она автоматически создается
    base = sq.connect('data_base.db')
    cur = base.cursor()
    if base:
        print('База данных data_base подключена')
    base.execute('CREATE TABLE IF NOT EXISTS data(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS beauty_treatments(name TEXT PRIMARY KEY, execution_time TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')


















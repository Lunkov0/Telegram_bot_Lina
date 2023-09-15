from aiogram import types, Dispatcher

from data_base.beauty_treatments_db import sql_add_command
from keyboards import admin_settings_kb
from create_bot import bot, dp





# Заносим время выполнения процедуры в бд
# async def time_to_bd(message: types.message):

    # await sql_add_command(message.text, )



def register_handlers_admin_settings(dp: Dispatcher):
    dp.register_message_handler(time_to_bd, commands=['Время_чистки', 'Время_пилинга', 'Время_массажа', 'Время_лазера'])

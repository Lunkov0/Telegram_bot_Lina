from aiogram import types, Dispatcher

from keyboards import admin_settings_kb
from create_bot import bot, dp


# @dp.message_handler(commands=['/Настройки'])
async def handler_admin_settings(message: types.message):
    await bot.send_message(message.from_user.id, 'Здесь настраивается длительность процедур \n'
                                                     'Выбери процедуру:', reply_markup=admin_settings_kb.kb_admin_settings)


def register_handlers_admin_settings(dp: Dispatcher):
    dp.register_message_handler(handler_admin_settings, commands=['Настройки'])

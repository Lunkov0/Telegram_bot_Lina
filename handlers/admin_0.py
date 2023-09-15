from aiogram import Dispatcher, types

from create_bot import bot
from handlers.admin_settings_0 import SetupStates
from keyboards import admin_settings_kb


ID = None


# @dp.message_handler(commands=['/Настройки'])
async def handler_admin_settings(message: types.message):
    global ID
    ID = message.from_user.id

    await bot.send_message(message.from_user.id, 'Здесь настраивается длительность процедур \n'
                                                 'Выбери процедуру:', reply_markup=admin_settings_kb.kb_admin_settings)
    await SetupStates.treatment_name.set()


# Таким образом мы пробрасываем функции в файл bot_telegram
def register_handlers_admin_settings(dp: Dispatcher):
    dp.register_message_handler(handler_admin_settings, commands=['Настройки'])

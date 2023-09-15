from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text, state

from create_bot import dp, bot
from data_base import sqlite_db, beauty_treatments_db
from keyboards import admin_kb

from aiogram.dispatcher.filters.state import State, StatesGroup

class SetupStates(StatesGroup):
    treatment_name = State()
    treatment_time = State()


ID = None


async def treatment_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await message.reply('Теперь введи время необходимое для этой операции')
        await SetupStates.treatment_time.set()


async def treatment_time(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text

        await beauty_treatments_db.sql_add_command(state)
        await message.reply('Информация добавлена в базу данных!')
        await state.finish()

# # Админ группы получает доступ. Получаем id текущего модератора.
# # @dp.message_handler(commands=['модератор'], is_chat_admin=True)
# async def make_changes_command(message: types.Message):
#     global ID
#     ID = message.from_user.id
#     await bot.send_message(message.from_user.id, 'Панель администратора. Здесь можно задать настройки и просмотреть записи', reply_markup=admin_kb.button_case_admin)
#     await message.delete()
#
#
# def register_handlers_admin(dp : Dispatcher):
#     dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
#     dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
#     dp.register_message_handler(make_changes_command, commands=['модератор'], is_chat_admin=True)
#     dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
#     dp.register_message_handler(load_name, state=FSMAdmin.name)
#     dp.register_message_handler(load_description, state=FSMAdmin.description)
#     dp.register_message_handler(load_price, state=FSMAdmin.price)
#     dp.register_message_handler(cancel_handler, state="*", commands='отмена')
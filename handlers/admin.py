from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import dp, bot
from data_base import sqlite_db
from keyboards import admin_kb


ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# Админ группы получает доступ. Получаем id текущего модератора.
# @dp.message_handler(commands=['модератор'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо!?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


# Начало диалога загрузки нового пункта меню
# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')


# Выход из состояний. Для любого машинного состояния
# state="*", вводя команду "отмена", в любом регистре
# @dp.message_handler(state="*", commands='отмена')  # Почему-то именно двойные кавычки
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Загрузка прекращена')


# Ловим первый ответ и пишем в словарь
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Каждой отправленной картинке в телеграмме присваивается id
        data['photo'] = message.photo[0].file_id
    # Переводит состояние бота на второй запрос
    await FSMAdmin.next()
    await message.reply('Теперь введи название')


# Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь введи описание')


# Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь укажи цену')


# Ловим последний ответ
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    await sqlite_db.sql_add_command(state)
    await state.finish()


def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(make_changes_command, commands=['модератор'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')


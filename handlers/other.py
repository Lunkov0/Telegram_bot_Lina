from aiogram import types
from create_bot import dp
from aiogram import Dispatcher


# @dp.message_handler()
# async def echo_send(message: types.Message):
    # await message.answer(message.text)  # Отвечает
    # await message.reply(message.text)  # Отвечает эхом
    # await bot.send_message(message.from_user.id, message.text)

# def register_handlers_other(dp : Dispatcher):
#     dp.register_message_handler(echo_send)

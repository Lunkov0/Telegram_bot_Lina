from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


# Кнопки клавиатуры админа
# button_load = KeyboardButton('/Загрузить')
# button_delete = KeyboardButton('/Удалить')


settings = KeyboardButton('/Настройки')


button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(settings)


# button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load)\
#     .add(button_delete)

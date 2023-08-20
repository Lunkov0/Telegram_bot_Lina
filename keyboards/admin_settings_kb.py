from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

b1 = KeyboardButton('/Время_чистки')
b2 = KeyboardButton('/Время_пилинга')
b3 = KeyboardButton('/Время_массажа')
b4 = KeyboardButton('/Время_лазера')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

# Заменяет клавиатуру на кнопки
kb_admin_settings = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

# add - кнопки во всю строку, insert в свободное место,
# kb_client.add(b1).add(b2).insert(b3)
kb_admin_settings.row(b1, b2, b3, b4)

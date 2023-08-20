from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db, beauty_treatments_db


async def on_startup(_):
    print('Бот вышел в онлайн')
    # Запускаем БД
    sqlite_db.sql_start()


from handlers import client, other, admin, admin_settings

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
admin_settings.register_handlers_admin_settings(dp)
# other.register_handlers_other(dp)  # Пустой хэндлер должен быть в конце

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

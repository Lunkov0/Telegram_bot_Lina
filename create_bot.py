from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Позволяет хранить данные в оперативной памяти. Можно внутри кода приделать любую БД
storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

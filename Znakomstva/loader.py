from aiogram import Bot, Dispatcher, types
from config import config_file
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config_file.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

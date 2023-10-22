from aiogram import Bot, Dispatcher, types
from config import config_file

bot = Bot(token=config_file.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from config import config_file

#
async def user_menu(user_id):
	keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.add('💌 Смотреть анкеты')
	keyboard.add('🖥 Моя анкета')

	if user_id in config_file.global_admins:
		keyboard.add('🔧 Панель 🔧')
	else:
		pass

	return keyboard

#
async def other_profiles():
	keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.row('👎🏻',' 💌','❤️')
	keyboard.add('🖥 Моя анкета')
	return keyboard
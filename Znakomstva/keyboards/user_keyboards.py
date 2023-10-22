from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import config_file


################################START######################################
async def start_button():
	keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	keyboard.add('Регистрация')

	return keyboard

###############################MALE/FEMALE#######################################
async def gender_selection():
	keyboard = InlineKeyboardMarkup(row_width=2)
	keyboard.add(InlineKeyboardButton('Парень', callback_data='male'))
	keyboard.add(InlineKeyboardButton('Девушка', callback_data='female'))

	return keyboard

async def gender_target():
	keyboard = InlineKeyboardMarkup(row_width=3)
	keyboard.add(InlineKeyboardButton('С парнями', callback_data='with_male'))
	keyboard.add(InlineKeyboardButton('С девушками', callback_data='with_female'))
	keyboard.add(InlineKeyboardButton('С обоими', callback_data='with_everyone'))

	return keyboard

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
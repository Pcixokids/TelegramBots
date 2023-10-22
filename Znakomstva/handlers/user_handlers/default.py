from loader import dp, bot
from aiogram import types
from aiogram.types.message import ContentType
from aiogram.dispatcher import FSMContext
@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Это ты девушка Кости?")
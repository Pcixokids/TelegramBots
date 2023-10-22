from loader import dp, bot
from aiogram import types
import aiogram.utils.markdown as md

from aiogram.types.message import ContentType
from aiogram.dispatcher import FSMContext

from keyboards.user_keyboards import *

from states.user_states import registration_state

start_text = """
<b>Приветствую в боте знакомств</b>

<i>Для регистрации нажмите на кнопку</i>
"""

@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, start_text, reply_markup=await start_button())

@dp.message_handler(text='Регистрация', state="*")
async def start_registration(message: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, "Приступим", reply_markup=ReplyKeyboardRemove())
    await registration_state.sex.set()
    await bot.send_message(message.from_user.id, "Укажите ваш пол", reply_markup=await gender_selection())

@dp.callback_query_handler(lambda cb: True, state=registration_state.sex)
async def gender_h(cb: types.CallbackQuery, state: FSMContext):
    if cb.data == 'male':
        await state.update_data(sex='M')
    elif cb.data == 'female':
        await state.update_data(sex='W')

    await registration_state.next()
    await bot.send_message(cb.from_user.id, "С кем хотите знакомится?", reply_markup=await gender_target())

@dp.callback_query_handler(lambda cb: True, state=registration_state.target)
async def target_h(cb: types.CallbackQuery, state: FSMContext):
    if cb.data == 'with_male':
        await state.update_data(target='Male')
    elif cb.data == 'with_female':
        await state.update_data(target='Female')
    elif cb.data == 'with_everyone':
        await state.update_data(target='Everyone')

    await registration_state.next()
    await bot.send_message(cb.from_user.id, "Как вас зовут?")

@dp.message_handler(state=registration_state.name)
async def name_h(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await registration_state.next()
    await bot.send_message(message.from_user.id, "Сколько вам лет?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=registration_state.age)
async def invalid_age_h(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите возраст числом")

@dp.message_handler(lambda message: message.text.isdigit(), state=registration_state.age)
async def age_h(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await registration_state.next()
    await bot.send_message(message.from_user.id, "В каком городе ты живешь?"
                           )
@dp.message_handler(state=registration_state.city)
async def city_h(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await registration_state.next()
    await bot.send_message(message.from_user.id, "Опишите себя")

@dp.message_handler(state=registration_state.description)
async def description_h(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await bot.send_message(message.from_user.id,
                           md.text(
                               md.text('Привет! ', md.bold(data['name'])),
                               md.text('Твой возраст: ', md.code(data['age'])),
                               md.text('Твой город: ', md.italic(data['city'])),
                               md.text('Твой пол: ', md.bold(data['sex'])),
                               md.text('С кем хочешь знакомиться: ', data['target']),
                               md.text('Твое описание: ', data['description']),
                               sep='\n'
                           ))

    await state.finish()
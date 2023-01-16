from django.conf import settings
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

token = '5756764001:AAGeDF53n4ayUazwSbmxSvvS0eGtvhtc79g'
bot = Bot(token)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/pic')
kb.add(b1, b2, b3)

HELP_COMMAND = """
<b>/start</b> - <em>Початок роботи</em> 
<b>/help</b> - <em>Допомога</em> 
<b>/pic</b> - <em>Картинкка</em> 
"""


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Вітаю вас {message.from_user.first_name}",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    # await message.answer(text=message.text)
    # await bot.send_message(chat_id=message.from_user.id, text='Hello!')
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode="HTML",
                           reply_markup=ReplyKeyboardRemove())
    await message.delete()


@dp.message_handler(commands=['pic'])
async def send_pic(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo="https://krasivosti.pro/uploads/posts/2021-03/1616167131_18-p-krasivie-sobachki-sobaka-foto-19.jpg")
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id, )
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
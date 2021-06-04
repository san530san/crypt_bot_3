from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
# хендлер реагирующий на команду /start

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer("Чтобы открыть меню напишите команду /menu .")

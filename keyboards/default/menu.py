from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# создаем клавиатуру
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Шифровать"),
            KeyboardButton(text="Расшифровать")
        ],
        [
            
            KeyboardButton(text="/cancel"),
            KeyboardButton(text="/help")
        ],
    ],
    resize_keyboard=True
)
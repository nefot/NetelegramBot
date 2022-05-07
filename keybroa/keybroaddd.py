from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/лампочка')],
        [KeyboardButton(text='/temp'), KeyboardButton(text='/alert')]
    ],
    resize_keyboard=True
)
admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/temp'), KeyboardButton(text='/alert')]
    ],
    resize_keyboard=True

)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def create_list_authors(arg: list[str]) -> InlineKeyboardMarkup:
    authors_kb = InlineKeyboardBuilder()
    authors_kb.row(
        InlineKeyboardButton(text=arg[0], callback_data='marsian')
    )
    authors_kb.row(
        InlineKeyboardButton(text=arg[1], callback_data='order')
    )
    authors_kb.row(
        InlineKeyboardButton(text=arg[2], callback_data='aliance')
    )
    return authors_kb.as_markup()







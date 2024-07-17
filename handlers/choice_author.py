from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from database.database import users_db
from keyboards.authors import create_list_authors
from services.file_handling import prepare_book, book


from lexicon import LEXICON

router = Router()

books = ['Рэй Бредбери "Марсианские хроники"',
         'Олег Сапфир "Орден Архитекторов" (6 глав)',
         'Михаил Атаманов "Альянс неудачников. Котёнок и его человек"']

callbacks = ['marsian', 'order', 'aliance']

@router.message(Command('authors'))
async def choice_book(message: Message):
    await message.answer(LEXICON[message.text], reply_markup=create_list_authors(arg=books))

@router.callback_query(F.data)
async def get_chosen_book(callback: CallbackQuery):
    await callback.answer(LEXICON['succesfully_choice'])
    path = users_db[callback.from_user.id]['book_path']
    path = path[:path.rfind('/')+1]
    path += str(callback.data)
    users_db[callback.from_user.id]['book_path'] = path
    prepare_book(path)
    await callback.answer()

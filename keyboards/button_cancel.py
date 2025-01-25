from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lepricone.lepricone import LEPRICONE_RU

def button_cancel() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEPRICONE_RU['cancel'],
            callback_data='cancel'
        )
    )
    return kb_builder.as_markup()
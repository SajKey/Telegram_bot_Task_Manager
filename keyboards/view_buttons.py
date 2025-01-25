from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lepricone.lepricone import LEPRICONE_RU

def list_buttons_tasks(names, dates) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for i in range(len(names)):
        kb_builder.row(
            InlineKeyboardButton(
                text = (f'{names[i]} - {dates[i]}'),
                callback_data=str(i)
        ))
    kb_builder.row(
    InlineKeyboardButton(
        text=LEPRICONE_RU['delete'],
        callback_data='delete'
        ),
    InlineKeyboardButton(
        text=LEPRICONE_RU['cancel'],
        callback_data='cancel_view'
        ),
    InlineKeyboardButton(
        text=LEPRICONE_RU['edit'],
        callback_data='edit'
        )
    )
    return kb_builder.as_markup()

def edit_buttons_tasks(names, dates) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for i in range(len(names)):
        kb_builder.row(
            InlineKeyboardButton(
                text = (f'{names[i]} - {dates[i]}'),
                callback_data=str(i)
        ))
    kb_builder.row(
        InlineKeyboardButton(
            text=LEPRICONE_RU['cancel'],
            callback_data='cancel_view'
        )
    )
    return kb_builder.as_markup()

def what_edit_buttons_tasks() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text=LEPRICONE_RU['edit_name'],
            callback_data='edit_name'
        ),
        InlineKeyboardButton(
            text=LEPRICONE_RU['edit_date'],
            callback_data='edit_date'
        ),
        width=2
    )
    kb_builder.row(
        InlineKeyboardButton(
            text=LEPRICONE_RU['cancel'],
            callback_data='cancel_view'
        )
    )
    return kb_builder.as_markup()

def del_buttons_tasks(names, dates) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for i in range(len(names)):
        kb_builder.row(
            InlineKeyboardButton(
                text = (f'{names[i]} - {dates[i]}'),
                callback_data=str(i+1) + ',del'
        ))

    kb_builder.row(
        InlineKeyboardButton(
            text=LEPRICONE_RU['cancel'],
            callback_data='cancel_view'
        )
    )
    return kb_builder.as_markup()
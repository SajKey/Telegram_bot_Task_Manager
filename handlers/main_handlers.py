from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup

from keyboards.button_cancel import button_cancel
from keyboards.view_buttons import (list_buttons_tasks, edit_buttons_tasks,
                                    del_buttons_tasks, what_edit_buttons_tasks)
from filtres.filtres import IsDelTask, DateFilter

from lepricone.lepricone import LEPRICONE_RU
from db.db import (list_users, add_new_user,
                   view_task, add_new_task,
                   del_task, generate_num_task,
                   rename_task, redate_task)

from datetime import datetime

class FMSUserAction(StatesGroup):
    name_task = State()
    date_task = State()
    edit_task = State()
    del_task = State()
    new_name_task = State()
    new_date_task = State()
    new_edit_task = State()

main_router = Router()


## КОМАНДНЫЕ ВЫЗОВЫ
# start
@main_router.message(CommandStart())
async def tap_start(message: Message):
    await message.answer(LEPRICONE_RU[message.text])
    if message.from_user.id not in await list_users():
        await add_new_user(message.from_user.id, message.from_user.username)

# help
@main_router.message(Command(commands='help'))
async def tap_help(message: Message):
    await message.answer(LEPRICONE_RU[message.text])

# new_task
@main_router.message(Command(commands='new_task'), StateFilter(default_state))
async def tap_new_task(message: Message, state: FSMContext):
    await message.answer(
        text = LEPRICONE_RU['create_new_task_name'],
        reply_markup=button_cancel()
        )
    await state.set_state(FMSUserAction.name_task)

# view_task
@main_router.message(Command(commands='view_task'))
async def tap_view_task(message: Message):
    global names_task, dates_task
    names_task, dates_task = await view_task(message.from_user.id)
    if names_task != []:
        await message.answer(
            text = LEPRICONE_RU['view_tasks'],
            reply_markup=list_buttons_tasks(names_task, dates_task)
        )
    else:
        await message.answer(LEPRICONE_RU['no_task'])

## РАБОТА ПО СОЗДАНИЮ НОВОЙ ЗАДАЧИ
# name
@main_router.message(StateFilter(FMSUserAction.name_task), F.text)
async def name_entered(message: Message, state: FSMContext):
    await message.answer(LEPRICONE_RU['greate_task'])
    await state.update_data(task_name=message.text)
    await state.set_state(FMSUserAction.date_task)

#date
@main_router.message(StateFilter(FMSUserAction.date_task), DateFilter())
async def date_entered(message: Message, state: FSMContext):
    name_task = await state.get_data()
    await add_new_task(
        message.from_user.id,
        name_task.get('task_name'),
        datetime.strptime(message.text, "%d.%m.%Y %H:%M"),
        await generate_num_task(message.from_user.id))
    await message.answer(LEPRICONE_RU['new_task_ready'])
    await state.clear()


## РАБОТА ПО РЕДАКТИРОВАНИЯ\УДАЛЕНИЮ ЗАДАЧ
# кнопка редактировать
@main_router.callback_query(F.data == 'edit')
async def cancel_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=LEPRICONE_RU['edit_task_text'],
        reply_markup=edit_buttons_tasks(names_task, dates_task)
        )
    await state.set_state(FMSUserAction.edit_task)

# что редактировать в выбранной задаче
@main_router.callback_query(StateFilter(FMSUserAction.edit_task))
async def cancel_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=LEPRICONE_RU['edit_one_task_text'] ,
        reply_markup=what_edit_buttons_tasks()
        )
    await state.update_data(num_task=int(callback.data)+1)
    await state.set_state(FMSUserAction.new_edit_task)

# ввод нового имени
@main_router.callback_query(StateFilter(FMSUserAction.new_edit_task), F.data == 'edit_name')
async def new_name_confirmation(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(LEPRICONE_RU['edit_name_text'])
    await state.set_state(FMSUserAction.new_name_task)

# сообщение об успешном изменении
@main_router.message(StateFilter(FMSUserAction.new_name_task), F.text)
async def new_name_ok(message: Message, state: FSMContext):
    num_task = await state.get_data()
    await rename_task(message.text, num_task.get('num_task'), message.from_user.id)
    await message.answer(LEPRICONE_RU['greate_edit'])
    await state.clear()

# редактировать дату
@main_router.callback_query(StateFilter(FMSUserAction.new_edit_task), F.data == 'edit_date')
async def cancel_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(LEPRICONE_RU['edit_date_text'])
    await state.set_state(FMSUserAction.new_date_task)

# сообщение об успешном редактировании даты
@main_router.message(StateFilter(FMSUserAction.new_date_task), DateFilter())
async def new_date_ok(message: Message, state: FSMContext):
    num_task = await state.get_data()
    await redate_task(message.text, num_task.get('num_task'), message.from_user.id)
    await message.answer(LEPRICONE_RU['greate_edit'])
    await state.clear()

# кнопка удалить
@main_router.callback_query(F.data == 'delete')
async def cancel_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=LEPRICONE_RU['delete_one_task_text'],
        reply_markup=del_buttons_tasks(names_task, dates_task)
        )
    await state.set_state(FMSUserAction.del_task)

# выбор задачи для удаления
@main_router.callback_query(StateFilter(FMSUserAction.del_task), IsDelTask())
async def task_is_del(callback: CallbackQuery, state: FSMContext):
    await del_task(callback.data.split(',')[0], callback.from_user.id)
    await callback.message.edit_text(LEPRICONE_RU['delete_task'])
    await state.clear()


## ОТМЕНА
@main_router.callback_query(F.data == 'cancel')
async def cancel_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=LEPRICONE_RU['cancel_text'])
    await state.clear()

@main_router.callback_query(F.data == 'cancel_view')
async def cancel_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text=LEPRICONE_RU['cancel_view'])
    await state.clear()

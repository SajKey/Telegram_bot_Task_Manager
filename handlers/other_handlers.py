from aiogram import Router
from aiogram.types import Message

other_router = Router()

@other_router.message()
async def send_nothing(message: Message):
    await message.answer('Чувак, ты думал что-то здесь будет? О, нет...')
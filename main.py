import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config_data.config import Config, load_config
from handlers import other_handlers, main_handlers
from db import db
from keyboards.main_menu import set_main_menu


logger = logging.getLogger(__name__)
storage = MemoryStorage()

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
        style='{'
    )

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)

    await set_main_menu(bot)
    
    dp.include_router(main_handlers.main_router)
    dp.include_router(other_handlers.other_router)
    dp.include_router(db.db_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
asyncio.run(main())
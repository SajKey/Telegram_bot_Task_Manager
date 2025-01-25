from aiogram import Bot
from aiogram.types import BotCommand

from lepricone.lepricone import LEPRICONE_COMMANDS

async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=descriprion
    ) for command,
        descriprion in LEPRICONE_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)
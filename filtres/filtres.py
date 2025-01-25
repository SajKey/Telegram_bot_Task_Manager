import re
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message

class IsDelTask(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.data.endswith(',del')
    
class DateFilter(BaseFilter):
    async def __call__(self, message: Message):
        return re.search('[0-9]{2}.[0-9]{2}.[0-9]{4} [0-9]{2}:[0-9]{2}', message.text)[0] == message.text


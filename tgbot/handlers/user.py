from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters.callback_data import CallbackData

from tgbot.models.gpt_api import GPT

user_router = Router()
gpt = GPT()

@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет!')

@user_router.message()
async def request(message: Message):
    await message.answer('Подождите, идет обработка запроса...')
    try:
        await message.answer(gpt.request(message.text))
    except Exception as e:
        await message.answer(f'Ошибка: {e}')
    
        

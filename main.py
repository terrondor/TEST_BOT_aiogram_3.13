import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv

from handlers.user_group import user_group_router
from handlers.user_private import user_private_router
from common.bot_commands_list import private

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message', 'edited_message']

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)
async def main():
    # Строчка служит для того чтобы бот не отвечал на обновления которы присылались когда бот был офлайн
    # await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=[], scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())

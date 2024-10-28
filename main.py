import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from handlers.greeting import router_greeting
from handlers.history import router_history
from handlers.hotel import router_hotel
from handlers.search import router_search
from handlers.unknown import router_unknown

with open("setting.txt", "r", encoding="utf-8") as file:
    token = file.read()


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота


# @goodmorn_ru_bot
bot = Bot(token=token)


# Диспетчер
dp = Dispatcher()


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_routers(
        router_greeting,
        router_history,
        router_hotel,
        router_search,
        router_unknown)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

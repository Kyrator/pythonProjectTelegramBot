import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

with open("setting.txt", "r", encoding="utf-8") as file:
    token = file.read()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
# @goodmorn_ru_bot
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def command_start_handler(message: types.Message) -> None:
    await message.answer("Привет {name} это лучший сервис по поиску отелей, пользуйся на здоровье мой пирожочек".format(
        name=message.from_user.first_name
    ))

# Хэндлер на команду /help — для получения справки о доступных командах бота;
@dp.message(Command("hello-world"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")


# Хэндлер на команду /help — для получения справки о доступных командах бота;
@dp.message(Command)
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# ● уточнение локации с помощью клавиатур;
# ● получение дат заезда/выезда;
# ● получение диапазона цен.


# Хэндлер на команду /history — для вывода истории запросов пользователей;
@dp.message(Command("/history"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


# В вывод истории запросов должны быть включены:
# ● дата поиска,
# ● ссылка на бронирование,
# ● описание,
# ● цена,
# ● фотографии,
# ● координаты.


# Хэндлер на команду /low — для вывода минимальных показателей с
# соответствующим изображением товара/услуги и так далее;
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


# Хэндлер на команду /high — для вывода максимальных показателей с
# соответствующим изображением товара/услуги и так далее.
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

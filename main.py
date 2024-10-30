import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7985978821:AAFwgKHlUGJQzXtPooEARSoQfa6UZlkmlTA")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")
    await message.answer("Вызов справки /help")
    await message.answer("Здесь можно посмотреть информацию от отелях с сайта Hotels.com")


# Хэндлер на команду /help
@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    list_commands = [
        ('start', "Запустить бота"),
        ('help', "Вывести справку"),
        ('highprice', 'самые дорогие отели в городе'),
        ('lowprice', 'недорогие отели в городе'),
        ('bestdeal', 'отели подходящие по цене и удалению от центра'),
        ('history', 'история поиска'),
        ('city', 'выбрать город/даты')]
    text = [f'/{command} - {desk}' for command, desk in list_commands]
    await message.answer('\n'.join(text))



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
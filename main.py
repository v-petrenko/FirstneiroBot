import json
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Токен бота
with open('config.json') as f:
    config = json.load(f)

API_TOKEN = config['API_TOKEN']

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        name = message.chat.first_name
        await message.answer(f"Привет, {name}! Я бот Вова знаю три слова - /start, /info и /joke")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /start: {e}")

# Обработчик команды /info
@dp.message(F.text == 'Информация')
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    try:
        await message.reply("Я тестовый бот, не обижайте меня, а то Вам прилетит")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /info: {e}")

# Обработчик команды /joke
@dp.message(Command("joke"))
async def cmd_joke(message: types.Message):
    try:
        await message.reply("Купи слона")
        await message.answer("Согласен /yes")
        await message.answer("Не согласен /no")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /joke: {e}")

# Обработчик команды /yes
@dp.message(Command("yes"))
async def cmd_yes(message: types.Message):
    try:
        await message.reply("Блестяще! Я продавец от бога!")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /yes: {e}")

# Обработчик команды /no
@dp.message(Command("no"))
async def cmd_no(message: types.Message):
    try:
        await message.reply("Все говорят нет, а ты купи слона")
        await message.answer("Согласен /yes")
        await message.answer("Не согласен /no")
    except Exception as e:
        logging.error(f"Ошибка при обработке команды /no: {e}")

# Обработчик неизвестных команд
@dp.message()
async def unknown_command(message: types.Message):
    try:
        command_list = "Доступные команды:\n/info\n/joke"
        await message.answer(command_list)
    except Exception as e:
        logging.error(f"Ошибка при обработке неизвестной команды: {e}")

# Основная функция
async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
import json
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from rondom_dog import dog

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Токен бота
with open('config.json') as f:
    config = json.load(f)

API_TOKEN = config['API_TOKEN']

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

button1 = types.KeyboardButton(text='Старт')
button2 = types.KeyboardButton(text='Информация')
button3 = types.KeyboardButton(text='Шутка')
button4 = types.KeyboardButton(text='Покажи собаку')

keyboard1 = [
    [button4,],
    [button3,button2],
    [button1,]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

# Обработчик команды /start
@dp.message(F.text == 'Старт')
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    try:
        name = message.chat.first_name
        await message.answer(f'Привет, {name}! Я бот Вова знаю три слова - /start, /info и /joke',reply_markup=kb1)
    except Exception as e:
        logging.error(f'Ошибка при обработке команды /start: {e}')

# Обработчик команды /info
@dp.message(F.text == 'Информация')
@dp.message(Command('info'))
async def cmd_info(message: types.Message):
    try:
        await message.reply('Я тестовый бот, не обижайте меня, а то Вам прилетит',reply_markup=kb1)
    except Exception as e:
        logging.error(f'Ошибка при обработке команды /info: {e}')

# Обработчик команды /joke
@dp.message(F.text == 'Шутка')
@dp.message(Command('joke'))
async def cmd_joke(message: types.Message):
    try:
        await message.reply('Купи слона',reply_markup=kb1)
        await message.answer('Согласен /yes')
        await message.answer('Не согласен /no')
    except Exception as e:
        logging.error(f'Ошибка при обработке команды /joke: {e}')

# Обработчик команды /yes
@dp.message(Command('yes'))
async def cmd_yes(message: types.Message):
    try:
        await message.reply('Блестяще! Я гениальный продавец!')
    except Exception as e:
        logging.error(f'Ошибка при обработке команды /yes: {e}')

# Обработчик команды /no
@dp.message(Command('no'))
async def cmd_no(message: types.Message):
    try:
        await message.reply('Все говорят нет, а ты купи слона')
        await message.answer('Согласен /yes')
        await message.answer('Не согласен /no')
    except Exception as e:
        logging.error(f'Ошибка при обработке команды /no: {e}')

@dp.message(F.text == 'Покажи собаку')
@dp.message(Command('Dog'))
async def cmd_dog(message: types.Message):
    try:
        name = message.chat.first_name
        image_dog = dog()
        await message.answer_photo(photo=image_dog)
    except Exception as e:
        logging.error(f'Ошибка при обработке команды /info: {e}')

# Отработчик команд реагирующих на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'Привет' in msg_user:
        await message.answer(f'Привет - {name}')
    elif 'Пока' in msg_user:
        await message.answer(f'Пока - {name}')
    elif 'Ты кто' in msg_user:
        await message.answer(f'Я тестовый бот - {name}')
    else:
        await message.answer(f'Я пока не знаю такого слова - {name}')

# Обработчик неизвестных команд
@dp.message()
async def unknown_command(message: types.Message):
    try:
        command_list = 'Доступные команды:\n/info\n/joke'
        await message.answer(command_list)
    except Exception as e:
        logging.error(f'Ошибка при обработке неизвестной команды: {e}')

# Основная функция
async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f'Ошибка при запуске бота: {e}')

# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
# Домашнее задание по теме "Клавиатура кнопок".
# Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.
#
# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.

# Измените massage_handler для функции set_age.
# Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.

# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом:
# 'Рассчитать' и 'Информация'.

# Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.

# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
# При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age с которой начинается
# работа машины состояний для age, growth и weight.

# Примечания:
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!


from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

# =======================================================
api = " "
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
# =======================================================


kb = ReplyKeyboardMarkup(resize_keyboard = True)

buttom1 = KeyboardButton(text= 'Информация')
kb.add(buttom1)
buttom2 = KeyboardButton(text= 'Рассчитать')
kb.add(buttom2)

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Привет!')
    await message.answer('Введите команду  "Старт"  чтобы начать общение !')

@dp.message_handler(text = ["Старт"])
async def start_message(message):
    await message.answer(' Я бот помогающий твоему здоровью. ', reply_markup = kb)

@dp.message_handler(text = 'Информация')
async def inform (message):
    await message.answer('Информация: Этот бот может рассчитать индивидуальное  количество каллорий для Вас')

class UserState(StatesGroup):   # КЛАСС МАШИНА СОСТОЯНИЙ
    age = State()               # возраст
    growth = State()            # рост
    weight = State()            # вес
@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст (лет):')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    print('Количество потребления рекомендуемых каллорий в сутки:')
    print(10 * int(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161)
    calories = (10 * int(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161)
    await message.answer('Ваша норма калорий:')
    await message.answer(calories)
    await state.finish()


# =======================================================
if __name__ == "__main__":
    executor.start_polling(dp,  skip_updates = True)
# =======================================================
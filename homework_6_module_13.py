# Домашнее задание по теме "Инлайн клавиатуры".
# Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.
# Задача "Ещё больше выбора":
# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'


# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'


# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.

# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.

# ===================================================================================================
# По итогу получится следующий алгоритм:
# Вводится команда /start
# На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
# В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
# По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
# По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
#
# Примечания:
# При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!



from aiogram.dispatcher import FSMContext
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# =======================================================
api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
# =======================================================

class UserState(StatesGroup):   # КЛАСС МАШИНА СОСТОЯНИЙ
    age = State()               # возраст
    growth = State()            # рост
    weight = State()            # вес

kb = ReplyKeyboardMarkup(resize_keyboard = True)

buttom1 = KeyboardButton(text= 'Информация')
kb.add(buttom1)
buttom2 = KeyboardButton(text= 'Рассчитать')
kb.add(buttom2)


kb_inline = InlineKeyboardMarkup() #resize_keyboard = True
buttom3 = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data= 'calories')
kb_inline.add(buttom3)
buttom4 = InlineKeyboardButton(text= 'Формула расчёта', callback_data= 'formulas')
kb_inline.add(buttom4)


@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Привет!')
    await message.answer('Введите команду  "Старт"  чтобы начать...')

@dp.message_handler(text = ["Старт"])
async def start_message(message):
    await message.answer(' Я бот помогающий твоему здоровью. ', reply_markup = kb)

@dp.message_handler(text = 'Информация')
async def inform (message):
    await message.answer('Информация: Этот бот может рассчитать индивидуальное  количество каллорий для Вас')


# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup = kb_inline)


# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('Норма каллорий будет расчитана по формуле Миффлина-Сан Жеора (для женщин):')
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()


# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (лет):')
    await UserState.age.set()
    await call.answer()

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
    calories = (10 * int(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161)
    await message.answer('Ваша норма калорий:')
    await message.answer(calories)
    await state.finish()


# =======================================================
if __name__ == "__main__":
    executor.start_polling(dp,  skip_updates = True)
# =======================================================
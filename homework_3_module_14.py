# Домашнее задание по теме "Доработка бота"
# Цель: подготовить Telegram-бота для взаимодействия с базой данных.

# # Задача "Витамины для всех!":
# Подготовка:
# Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним в файл module_14_3.py.

# Дополните ранее написанный код для Telegram-бота:

# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".

# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"

# Создайте хэндлеры и функции к ним:
# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).

# Функция get_buying_list должна выводить надписи 'Название:
# Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
# После каждой надписи выводите картинки к продуктам.
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".

# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"



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

# -------------------------------------------------------------------------------------------

kb = ReplyKeyboardMarkup(resize_keyboard = True)
buttom1 = KeyboardButton(text= 'Информация')
kb.add(buttom1)
buttom2 = KeyboardButton(text= 'Рассчитать')
kb.add(buttom2)
buttom3 = KeyboardButton(text= 'Купить')
kb.add(buttom3)

# -------------------------------------------------------------------------------------------

kb_inline = InlineKeyboardMarkup(resize_keyboard = True) #resize_keyboard = True
buttom3 = InlineKeyboardButton(text= 'Рассчитать норму калорий', callback_data= 'calories')
kb_inline.add(buttom3)
buttom4 = InlineKeyboardButton(text= 'Формула расчёта', callback_data= 'formulas')
kb_inline.add(buttom4)

# -------------------------------------------------------------------------------------------

# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"

kb_Products = InlineKeyboardMarkup(resize_keyboard = True)
buttom5 = InlineKeyboardButton(text= 'Product 1', callback_data="product_buying")
kb_Products.add(buttom5)
buttom6 = InlineKeyboardButton(text= 'Product 2', callback_data="product_buying")
kb_Products.add(buttom6)
buttom7 = InlineKeyboardButton(text= 'Product 3', callback_data="product_buying")
kb_Products.add(buttom7)
buttom8 = InlineKeyboardButton(text= 'Product 4', callback_data="product_buying")
kb_Products.add(buttom8)

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Добро пожаловать!')
    await message.answer('Введите команду  "Старт"  чтобы начать...')

@dp.message_handler(text = ["Старт"])
async def start_message(message):
    await message.answer(' Я бот помогающий твоему здоровью. ', reply_markup = kb)

@dp.message_handler(text = 'Информация')
async def inform (message):
    await message.answer('Информация: Этот бот, может рассчитать индивидуальное  количество каллорий для Вас')

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Название: ', reply_markup = kb_inline)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    number = 1
    while number < 5:
        await message.answer(f"Product  {number} | Описание: {number} | Цена: {number * 100}")
        with open(f'image_for_homework_3/{number}.jpg', "rb") as img:                               # <=== ВСТАВЛЯЕМ
            await message.answer_photo(img,)                                                        # <=== КАРТИНКУ
        number += 1
    await message.answer("Выберите продукт для покупки: ", reply_markup = kb_Products)

@dp.callback_query_handler(text= 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели выбранный Вами продукт!')
    await call.answer()

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('Норма каллорий будет расчитана по формуле Миффлина-Сан Жеора (для женщин):')
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()

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
# Домашнее задание по теме "План написания админ панели"
# Цель: написать простейшие CRUD функции для взаимодействия с базой данных.
#
# Задача "Продуктовая база":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.
#
# Дополните ранее написанный код для Telegram-бота:


# --------------------------------------------------------------------------------------------------------
# Создайте файл crud_functions.py и напишите там следующие функции:

# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:

# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - тест
# price(цена) - целое число (не пустой)

# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#----------------------------------------------------------------------------------------------------------

# Изменения в Telegram-бот:
# В самом начале запускайте ранее написанную функцию get_all_products.

# Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов функцию get_all_products.
# Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

# ----------------------------------------------------------------------------------------------------------------------
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from crud_functions import get_all_products


# ====================================v===================
api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())
# =======================================================


prod = get_all_products()

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

kb_Products = InlineKeyboardMarkup(resize_keyboard = True)
buttom5 = InlineKeyboardButton(text= 'Product 1', callback_data="product_buying")
kb_Products.add(buttom5)
buttom6 = InlineKeyboardButton(text= 'Product 2', callback_data="product_buying")
kb_Products.add(buttom6)
buttom7 = InlineKeyboardButton(text= 'Product 3', callback_data="product_buying")
kb_Products.add(buttom7)
buttom8 = InlineKeyboardButton(text= 'Product 4', callback_data="product_buying")
kb_Products.add(buttom8)

# -------------------------------------------------------------------------------------------

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
    for index, product in enumerate(get_all_products()):        # Функция  enumerate()  позволяет пройтись по итерируемому объекту (например, списку, кортежу, строке)# и на каждой итерации возвращает кортеж, содержащий индекс элемента и сам  лемент.
        await message.answer(f"Название:{product[1]} | Описание:{product[2]} | Цена: {product[3]}")
        with open(f'image_for_homework_3/{index+1}.jpg', "rb") as img:                               # <=== ВСТАВЛЯЕМ
            await message.answer_photo(img,)                                                         # <=== КАРТИНКУ
    await message.answer("Выберите продукт для покупки: ", reply_markup = kb_Products)


    # await message.answer('Выберите продукцию:', reply_markup=inline_products)
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


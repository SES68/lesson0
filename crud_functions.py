# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:

# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - тест
# price(цена) - целое число (не пустой)

# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.

import sqlite3

def initiate_db():                                 # id, title, description, price
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,             
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    # for i in range(4):
    #     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?,?,?,?)",
    #                    (i+1, f"Продукт №{i+1}", f"Описание продукта №{i+1}", (i+1)*1000))
    # connection.commit()
    # connection.close()



def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products
    connection.commit()
    connection.close()

# products = get_all_products()
# print(products[1])




# Выбор элементов и функции в SQL запросах"
# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.

# Для решения необходимо дополнить существующий код:

# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.


import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (f"User{i+1}", f"example{i+1}@gmail.com", (i+1)*10, "1000"))
#
# for i in range(0,10,2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i+1))
#
# for i in range(0, 10, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (i+1,))
#
# cursor.execute("SELECT * FROM Users")
# users = cursor.fetchall()
# for user in users:
#     if user[3] != 60:
#         print('Имя: ' + user[1] + ' | ' + 'Почта: ' + user[2] + ' | ' + ' Возраст: ' + str(user[3]) + ' | ' + 'Баланс: ' + str(user[4]))

# =================================== ПЕРВЫЙ БЛОК ПРОГРАММЫ ЗАКОНЧЕН (задание 1) ===================================




# ===================================      ВТОРОЙ БЛОК ПРОГРАММЫ  (задание 2):   ===================================

#  - удаление id 6
# cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# ----------------------------------------------------------------------------------------------------
# Подсчитать общее количество записей:
cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
print(total1)                                               #  = (5,)
# ------------------------------------------------------------------------------------------------------

# Посчитать сумму всех балансов:
cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(total2)
# --------------------------------------------------------------------------------------------------------

# Вывести в консоль средний баланс всех пользователей:
print("средний баланс всех пользователей равен:  ", total2/total1)


connection.commit()
connection.close()
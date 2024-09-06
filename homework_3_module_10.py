# Модуль 10 дз № 3

import threading
from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    list_of_moves = []
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            x = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():  # условия можно объединить
                self.lock.release()
            self.balance += x
            Bank.list_of_moves.append(f'Пополнение:{x}, Баланс:{self.balance}')
            sleep(0.1)

    def take(self):
        for _ in range(100):
            y = randint(50, 500)
            if self.balance >= y:
                self.balance -= y
                Bank.list_of_moves.append(f'Снятие:{y}, Баланс:{self.balance}')
                sleep(0.1)
            else:
                self.lock.acquire()
                Bank.list_of_moves.append(f'Запрос на {y} отклонён, недостаточно средств. Баланс:{self.balance}')
                sleep(0.1)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
print('Программа запущена!')
print('Работает!')
print('Немного надо подождать.          Формируем красивый вывод на экран...')
print('======================================================================')

th1.start()
sleep(0.1)
th2.start()
th1.join()
th2.join()

print(*Bank.list_of_moves, sep='\n')
print('============================')
print(f'Итоговый баланс: {bk.balance}')
print('============================')
print('ПРОГРАММА ОТРАБОТАЛА УСПЕШНО!')
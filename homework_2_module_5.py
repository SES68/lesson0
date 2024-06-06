# 2024/06/06 |Домашняя работа по уроку "Специальные методы классов"
# Домашнее задание по уроку "Специальные методы классов"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
# Полученный код напишите в ответ к домашему заданию

class House:
    def __init__(self, numberOfloors):
        self.numberOffloors = 0

def setNewNumberOfFloors(floor):
    numberOffloors = floor
    print(f'Вы прибыли на {floor} этаж.')

setNewNumberOfFloors(10)

# РЕЗУЛЬТАТ РАБОТЫ ПРОГРАММЫ:
# Вы прибыли на 10 этаж.

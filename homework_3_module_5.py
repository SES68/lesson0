# 2023/06/06|Домашняя работа по уроку "Перегрузка операторов."
# Домашнее задание по уроку "Перегрузка операторов"
#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self.numberOfFloors
# и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашнему заданию



class Building:

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType   = str(buildingType)

    def __eq__(self, other):
        if (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType):
            return True
        else:
            return False

ww1 = Building(4, 3)
ww2 = Building(4, 3)
print(ww1 == ww2)


# class Building:
#
#     def __init__(self, numberOfFloors, buildingType):
#         self.numberOfFloors = int(numberOfFloors)
#         self.buildingType   = str(buildingType)
#
# def __eq__(self, other):
#              return (self.numberOfFloors == other.numberOfFloors) and (self.buildingType == other.buildingType)
#
#
# ww1 = Building(2,2)
# ww2 = Building(2, 2)
# print(ww1 == ww2)
















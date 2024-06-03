# 2024/06/03 17:00 |Домашняя работа по уроку "Атрибуты и методы объекта."
# Цель: применить на практике знания о классах, объектах и их атрибутах.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


h0 = House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Домик в городе', 8)


def go_to(self, new_floor):
    print(f'Вы находитесь в: {self.name}, поднимаемся на {new_floor} этаж.  Поехали...')
    stage_ = 1
    if (new_floor < 1) or (new_floor > self.number_of_floors):
        print('Упс!  Такого этажа не существует!')
    else:
        while stage_ <= new_floor:
            print(stage_)
            stage_ += 1
        print(f'Вы прибыли на {new_floor} этаж. Двери открываются...')


go_to(h1, 18)


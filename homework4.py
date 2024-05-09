# Домашняя работа по уроку "Цикл for.
# Элементы списка.
# Полезные функции в цикле.



list_ = ['BMW','MB','LADA','KIA','HONDA']
cars_count = 0
for i in range(len(list_)):
    print('Я езжу на автомобиле марки ', list_[i])
    cars_count += 10
    print(cars_count)
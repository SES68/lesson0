"                  ДОПОЛНИТЕЛЬНОЕ ПРАКТИЧЕСКОЕ ЗАДАНИЕ ПО МОДУЛЮ № 2"


"                 ЗАДАНИЕ:   Слишком древний шифр. "

# ------------------------------------------------------------------------------------------------

sp_ = list(range(3,21))         # - АВТОМАТИЧЕСКИ СОЗДАЕМ СПИСОК ОТ 3 ДО 20
import random                   # - Вызываем библиотеку random
kod__ = random.choices(sp_)     # - Генерируем случайное значение (камни левого поля) - КЛЮЧ

new_list = map(str, kod__)      # - Преобразуем КЛЮЧ
string_value = ''.join(new_list)# - из типа 'list' в тип 'int'
kod_ = int(string_value)        # - --------------------------

parol = []                                      # - создаем "рабочий" список
ks = 0                                          # - переменная внешнего цикла
kw = 0                                          # - переменная внутреннего цикла
while ((ks <= kod_) and ((ks + kw) <= kod_)):
    ks += 1
    while ((kw <= kod_) and ((ks + kw) <= kod_)):
        kw += 1
        if ((kod_ / (ks + kw)) == (kod_ // (ks + kw)) and (ks < kw)):
            # УСЛОВИЯ:  (КРАТНОСТЬ) and (исключаем ПОВТОРЕНИЕ комбинаций цифр)
            parol.append(str(ks))               # записываем значение в "рабочий" список
            parol.append(str(kw))               # записываем значение в "рабочий" список

    kw = 0
my_parol ="".join(parol)                        # - "рабочий" список преобразуем в пароль в нужном нам виде.


# ------------------------------------------------------------------------------------------------


print("              ")
print("Привет, горе-путешественник! Как дела? Попался?")
print("А я тебя предупреждал - сначала научись программировать!")
print("Ладно, я  тебя вытащу отсюда! (СВОИХ НЕ БРОСАЕМ)")
print("Но обещай, что по приезду домой освоишь профессию Pithon - разработчика!")
print("Потому, что я не буду постоянно вытаскивать тебя из твоих передряг!")
print("              ")
print("              ")
print("Итак, слева от тебя постоянно меняющиеся камни:")
print("-----------------------------------------------")
print("Это ключ к паролю:   ", kod_)
print("А вот тебе и пароль: ", my_parol)
print("-----------------------------------------------")
print("              ")
print("Воспользуйся им побыстрее, пока камни в левом поле не сменились на другие!")
print("              ")
print("                     НЕ БЛАГОДАРИ...!!!")


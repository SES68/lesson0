# 2023/07/01|Домашнее задание по теме "Оператор "with".
# Создайте новый проект или продолжите работу в текущем проекте
#
# Ваша задача:
# Создайте в директории проекта текстовый файл с расширением txt
# Добавьте в этот файл следующий текст
#  -*- coding: utf-8 -*-
# My soul is dark - Oh! quickly string
# The harp I yet can brook to hear;
# And let thy gentle fingers fling
# Its melting murmurs o'er mine ear.
# If in this heart a hope be dear,
# That sound shall charm it forth again:
# If in these eyes there lurk a tear,
# 'Twill flow, and cease to burn my brain.
#
# But bid the strain be wild and deep,
# Nor let thy notes of joy be first:
# I tell thee, minstrel, I must weep,
# Or else this heavy heart will burst;
# For it hath been by sorrow nursed,
# And ached in sleepless silence, long;
# And now 'tis doomed to know the worst,
# And break at once - or yield to song.
#
# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with
# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# Получившийся код прикрепите к заданию текстом


file_open = open('proba_open.txt', mode = 'w')
file_text = "-*- coding: utf-8 -*- \nMy soul is dark - Oh! quickly string) \nThe harp I yet can brook to hear;\nAnd let thy gentle fingers fling\nIts melting murmurs o'er mine ear.\nIf in this heart a hope be dear,\nThat sound shall charm it forth again:\nIf in these eyes there lurk a tear,\n'Twill flow, and cease to burn my brain.\nBut bid the strain be wild and deep,\nNor let thy notes of joy be first:\nI tell thee, minstrel, I must weep,\nI tell thee, minstrel, I must weep,\nI tell thee, minstrel, I must weep,\nOr else this heavy heart will burst;\nOr else this heavy heart will burst;\nFor it hath been by sorrow nursed,\nAnd ached in sleepless silence, long;\nAnd now 'tis doomed to know the worst,\nAnd break at once - or yield to song."
file_open.write(file_text)
file_open.close()

with open('proba_open.txt', mode = 'r') as f:
    for line in f:
        print (line)

print(f.closed)       # Проверяем закрылся ли автоматически файл.

# Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# Ответ: Удобством автоматического закрытия файла, в случае его незакрытия.







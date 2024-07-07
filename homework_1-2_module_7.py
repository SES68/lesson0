# 2024/07/02
# Домашнее задание по теме "Позиционирование в файле".


from pprint import pprint
file_name = 'xxxxx.txt'
strings = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
file_text = "-*- coding: utf-8 -*- \n"
Number_byte = 0

def custom_write(file_name, strings):
    file_open = open(file_name, mode='r+', encoding = 'utf-8')
    strings_positions = {}
    n = 1
    for f in strings:
        number_byte = file_open.tell()
        file_open.write(f)
        file_open.write('\n')
        strings_positions[(n, number_byte)] = f
        n += 1
    file_open.close()
    return strings_positions


pprint(custom_write(file_name, strings))  # Вызов функции



























# ОБРАЗЕЦ кода:
# file_open = open('proba_open.txt', mode = 'w')
# file_text = "-*- coding: utf-8 -*- \nMy soul is dark - Oh! quickly string) \nThe harp I yet can brook to hear;\nAnd let thy gentle fingers fling\nIts melting murmurs o'er mine ear.\nIf in this heart a hope be dear,\nThat sound shall charm it forth again:\nIf in these eyes there lurk a tear,\n'Twill flow, and cease to burn my brain.\nBut bid the strain be wild and deep,\nNor let thy notes of joy be first:\nI tell thee, minstrel, I must weep,\nI tell thee, minstrel, I must weep,\nI tell thee, minstrel, I must weep,\nOr else this heavy heart will burst;\nOr else this heavy heart will burst;\nFor it hath been by sorrow nursed,\nAnd ached in sleepless silence, long;\nAnd now 'tis doomed to know the worst,\nAnd break at once - or yield to song."
# file_open.write(file_text)
# file_open.close()
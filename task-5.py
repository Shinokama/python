"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


from random import randint
from os import path, remove
from sys import exit
from functools import reduce


filename = "task-5.txt"
is_recreate = True

# Проверяем существование файла, в который собираемся писать
if path.exists(filename):
    ask = input(f"Файл {filename} уже существует, Вы хотите его перезаписать? \nY или y = да, "
                f"\nN или n = посчитать сумму из имеющегося файла, \nдругое = остановить программу."
                f"\nВаш ответ: ")
    if ask.lower() == "y":
        remove(filename)
    elif ask.lower() == "n":
        is_recreate = False
    else:
        print("Выполнение программы остановлено.")
        exit()


# Скрипт создает файл из случайно заданных цифр (1-1000) в случайном количестве (5-100), разделенных пробелом.
# Работает если файл отсутствует либо выбрано согласие на перезапись
if is_recreate:
    limit = randint(5, 100)
    with open(filename, "a", encoding="utf-8") as file_obj:
        while limit > 0:
            limit -= 1
            file_obj.write(str(f"{randint(1, 1000)} "))


# Скрипт считает сумму всех цифр из ранее полученного файла и выводит результат в консоль
with open(filename, "r", encoding="utf-8") as file_obj:
    print(reduce(lambda x, y: int(x) + int(y), [el for el in (file_obj.readline()).split()]))

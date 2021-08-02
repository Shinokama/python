"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

from os import path, remove
from sys import stderr


filename = "task-1.txt"

try:
    if path.exists(filename):
        ask = input("Файл уже существует. Вы хотите удалить его? (Y или y если да, "
                    "N или n если продолжаем писать в него): ")
        if ask.lower() == "y":
            remove(filename)
        elif ask.lower() == "n":
            pass
        else:
            raise Exception()
except Exception:
    stderr.write("Вы ввели что-то другое на предыдущий вопрос (должно было быть Y или N)")
else:
    repeat = True
    while repeat:
        string = input("Введите строку: ")
        if string == "":
            repeat = False
        else:
            with open(filename, "a", encoding="utf-8") as file_1:
                print(string, file=file_1)
    print(f"Запись в файл {filename} завершена.")

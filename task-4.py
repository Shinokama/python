"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

from os import path, remove
from sys import exit

filename = "task-4.txt"
new_filename = "task-4-new.txt"
my_dict = {'One': "Один", 'Two': "Два", 'Three': "Три", 'Four': "Четыре"}

# Проверяем существование файла, в который собираемся писать
if path.exists(new_filename):
    ask = input(f"Файл {new_filename} уже существует, в процессе работы скрипта он будет удален. Вы согласны? "
                f"(Y или y если да): ")
    if ask.lower() == "y":
        remove(new_filename)
        print(f"Файл {new_filename} удален")
    else:
        print("Удаление файла не произведено. Выходим из программы.")
        exit()

# Сам скрипт. Выполняется только в случае отсутствия файла или положительного ответа при проверке.
with open(filename, "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        line = line.replace(line.split()[0], my_dict.get(line.split()[0]))
        with open(new_filename, "a", encoding="utf-8") as new_file_obj:
            new_file_obj.write(line)
print(f"Файл {new_filename} создан")

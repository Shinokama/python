"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


filename = "task-2.txt"

print(f'В файле "{filename}":')
with open(filename, "r", encoding="utf-8") as file_obj:
    lines = 0
    for string in file_obj.readlines():
        lines += 1
        word_count = 0
        for word in string.split():
            word_count += 1
        print(f'Строка {lines} содержит слов: {word_count}')
    print(f'Всего в файле строк: {lines}')

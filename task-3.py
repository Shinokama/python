"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


filename = "task-3.txt"

with open(filename, "r", encoding="utf-8") as file_obj:
    salaries = []
    if_present = False
    empl = []
    try:
        for string in file_obj.readlines():
            salaries.append(float(string.split()[1]))
            if float(string.split()[1]) < 20000:
                empl.append(string.split()[0])
                if_present = True
    except ValueError:
        print("Пожалуйста, указывайте оклад числом")
    except Exception:
        print("Возникла непредвиденная ошибка, проверьте формат файла")
    else:
        if if_present:
            print(f'У следующих сотрудников оклад менее 20 тыс.:')
            for emp in empl:
                print(emp)
        else:
            print("Сотрудников в окладом менее 20 тыс. не указано в файле")
        print(f'Средняя величина дохода сотрудников составляет {(sum(salaries) / len(salaries)):g}')

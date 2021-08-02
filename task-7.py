"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

filename = "task-7.txt"
filename_json = "task-7.json"
my_dict = {}
profits = []

with open(filename, "r", encoding="utf-8") as file_obj:
    for line in file_obj:
        firm = line.split()[0]
        profit = int(line.split()[2]) - int(line.split()[3])
        if profit > 0:
            profits.append(profit)
        my_dict.update({firm: profit, })

my_list = [my_dict, {"average_profit": (sum(profits) // len(profits))}]

with open(filename_json, "w") as write_f:
    json.dump(my_list, write_f)

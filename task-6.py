a = float(input("Введите результат пробежки за первый день (км): "))
b = float(input("Введите ожидаемый результат (не менее n км): "))
result = a
day = 1
while result < b:
    result = result * 1.1
    day += 1
print(f'на {day}-й день спортсмен достиг результата — не менее {int(b)} км.')

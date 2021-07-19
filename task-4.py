a = input("Введите любое целое число: ")
le = len(a)
result = 0
while le > 0:
    le = le - 1
    if int(a[le]) >= result:
        result = int(a[le])
print(f'Самая большая цифра: {result}')

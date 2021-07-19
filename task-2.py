# ask for user input
s = int(input("Введите время в секундах (целое число): "))
m = s // 60
s = s % 60
h = m // 60
m = m % 60
if len(str(s)) == 1:
    s = str(f'0{s}')
if len(str(m)) == 1:
    m = str(f'0{m}')
if len(str(h)) == 1:
    h = str(f'0{h}')
print(f'Спасибо, вот сколько это в часах, минутах и секундах: {h}:{m}:{s}')

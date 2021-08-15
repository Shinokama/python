"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
"""
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""
"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


def validation(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper


class Storage:
    equipment_on_storage = []
    equipment_in_work = []

    @classmethod
    @validation
    def to_storage(cls, eq_dict):
        if type(eq_dict) is not dict:
            raise TypeError("Принимается только словарь. Сформируйте его через классы оборудования.")
        else:
            if cls.equipment_on_storage.count(eq_dict) == 1:
                print("Оборудование уже числится на складе")
            else:
                cls.equipment_on_storage.append(eq_dict)
            if cls.equipment_in_work.count(eq_dict) == 1:
                cls.equipment_in_work.remove(eq_dict)

    @classmethod
    @validation
    def to_work(cls, eq_dict):
        if type(eq_dict) is not dict:
            raise TypeError("Принимается только словарь. Сформируйте его через классы оборудования.")
        else:
            if cls.equipment_in_work.count(eq_dict) == 1:
                print("Оборудование уже передано в работу")
            else:
                cls.equipment_in_work.append(eq_dict)
            if cls.equipment_on_storage.count(eq_dict) == 1:
                cls.equipment_on_storage.remove(eq_dict)


class Equipment:
    @validation
    def __init__(self, i_number, vendor, model, eq_type="unknown"):
        self.eq_dict = {'type': eq_type, 'i_number': i_number, 'vendor': vendor, 'model': model}


class Printer(Equipment):
    eq_type = "Printer"

    @validation
    def __init__(self, i_number, vendor, model, color):
        super().__init__(i_number, vendor, model)
        if type(color) is not bool:
            raise TypeError("Ошибка ввода данных. Убедитесь, что 'color' булерово (True/False)")
        else:
            self.eq_dict.update({'type': self.eq_type, 'color': color})


class Laptop(Equipment):
    eq_type = "Laptop"

    @validation
    def __init__(self, i_number, vendor, model, cpu, memory_gb, disk_gb):
        super().__init__(i_number, vendor, model)
        if type(memory_gb) is not int or type(disk_gb) is not int:
            raise TypeError("Ошибка ввода данных. Убедитесь, что 'memory_gb' и 'disk_gb' указаны числом.")
        else:
            self.eq_dict.update({'type': self.eq_type, 'cpu': cpu, 'memory_gb': memory_gb, 'disk_gb': disk_gb})


printer_1 = Printer("PR0021", "HP", "LaserJet CP1215", True)
printer_2 = Printer("PR0022", "Kyocera", "ECOSYS P2335d", False)
laptop_1 = Laptop("L0041", "HP", "ProBook 430", "Intel Core i7-1165G7", 16, 512)
laptop_2 = Laptop("L0042", "Lenovo", "ThinkPad X1 Carbon G9 T", "Intel Core i5 1135G7", 8, 256)

print("\nОтправляем все оборудование на склад")
Storage.to_storage(printer_1.eq_dict)
Storage.to_storage(printer_2.eq_dict)
Storage.to_storage(laptop_1.eq_dict)
Storage.to_storage(laptop_2.eq_dict)

print(f'Оборудование на складе:\n{Storage.equipment_on_storage}')
print(f'Оборудование в работе:\n{Storage.equipment_in_work}')

print("\nПовторяем процедуру для одного экземпляра оборудования (проверка на дубликаты)")
Storage.to_storage(printer_1.eq_dict)

print("\nЗабираем 2 экземпляра оборудования со склада")
Storage.to_work(printer_2.eq_dict)
Storage.to_work(laptop_1.eq_dict)
print(f'Оборудование на складе:\n{Storage.equipment_on_storage}')
print(f'Оборудование в работе:\n{Storage.equipment_in_work}')


print("\nПробуем еще раз забрать оборудование")
Storage.to_work(printer_2.eq_dict)

print("\nПробуем отправить неверные данные")
Laptop("L0041", "HP", "ProBook 430", "Intel Core i7-1165G7", "16", 512)
Printer("PR0021", "HP", "LaserJet CP1215", "True")
Storage.to_work("Something")
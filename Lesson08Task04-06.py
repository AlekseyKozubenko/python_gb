"""
 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
 А также класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определить параметры, общие для приведенных типов.
 В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
 Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
 передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру, например словарь.
 Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except WarehouseError as e:
            print(e)
        except ValueError:
            print("Введите число для Количества")
    return wrapper


class WarehouseError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    """
    Структура склада:
    ключ: объект
    значение: количество
    """
    stock_units = {}

    list_of_types = set()

    @classmethod
    @validate
    def income(cls, obj, count):
        if type(count) not in [int, float]:
            raise ValueError
        elif obj in cls.stock_units.keys():
            new_count = cls.stock_units.get(obj) + count
            cls.stock_units.update({obj: new_count})
        else:
            cls.stock_units.update({obj: count})
            cls.list_of_types.add(obj.get_type())
        print(f"На склад добавлен: {obj.get_type()} - {obj.get_brand()} - {obj.get_model()} - {count}")

    @classmethod
    @validate
    def outcome(cls, obj, count):
        print(f"Запрос на списание: {obj.get_type()} - {obj.get_brand()} - {obj.get_model()} - {count}")
        if type(count) not in [int, float]:
            raise ValueError
        elif obj in cls.stock_units.keys():
            old_count = cls.stock_units.get(obj)
            if count > old_count:
                raise WarehouseError("Недостаточно товара на складе.")
            else:
                cls.stock_units.update({obj: old_count - count})
                print("Списание прошло удачно.")
        else:
            raise WarehouseError("Товара не существует.")

    @classmethod
    def print_stock(cls):
        print("Текущее состояние склада:")
        result = ""
        types = list(cls.list_of_types)
        types.sort()
        # print(types)
        for element in types:
            # print(f"элемент - {element}")
            result = result + element + ":\n"
            # print(result)
            for obj in cls.stock_units.keys():
                # print(f"тип - {obj.get_type()}")
                if str(obj.get_type()) == str(element):
                    # print(True)
                    result = result + "    " + obj.get_brand() + " - " + obj.get_model() + ": " + \
                             str(cls.stock_units.get(obj)) + "\n"
                else:
                    # print(False)
                    pass
        return result


class Technics:
    def __init__(self, brand, model, type_of):
        self.__type_of = type_of
        self.__brand = brand
        self.__model = model

    def get_type(self):
        return self.__type_of

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model


class Printer(Technics):
    def __init__(self, brand, model, colour):
        super().__init__(brand, model, "Printer")
        self.colour = colour


class Scanner(Technics):
    def __init__(self, brand, model, resolution):
        super().__init__(brand, model, "Scanner")
        self.resolution = resolution


class Copier(Technics):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model, "Copier")
        self.speed = speed


print(Warehouse.print_stock())
printer1 = Printer("HP", "H1001", "RGB")
Warehouse.income(printer1, 25)
Warehouse.income(printer1, 15)
print(Warehouse.print_stock())
# print(Warehouse())

printer2 = Printer("HP", "H2002", "RGB")
Warehouse.income(printer2, 48)
Warehouse.outcome(printer2, 37)
printer3 = Printer("Canon", "CP-9", "BW")
Warehouse.income(printer3, 25)
Warehouse.outcome(printer3, 35)
print(Warehouse.print_stock())

scanner1 = Scanner("LG", "6900S", "800px")
Warehouse.income(scanner1, 15)

copier1 = Copier("XEROX", "CM-500S", 1000)
Warehouse.income(copier1, 5)
copier2 = Copier("XEROX", "CM-501S", 1000)
Warehouse.outcome(copier2, 35)
print(Warehouse.print_stock())

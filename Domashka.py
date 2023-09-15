"""Создать объект коттедж.Основные свойства–количество этажей,площадь,гараж,бассейн.Создать определенный коттедж,
который имеет гараж,но не имеет бассейна.Вывести свойства объекта в консоль
"""


class Builder:

    def build_floor(self):
        pass

    def total_square(self):
        pass

    def build_garage(self):
        pass

    def build_pool(self):
        pass


class Floor:
    def __init__(self, num_of_floors):
        self.__num_of_floors = num_of_floors

    def __str__(self):
        if self.__num_of_floors % 10 == 1:  #выбор окончания
            x = 'этаж'
        elif 2 <= self.__num_of_floors % 10 <= 4:
            x = 'этажа'
        else:
            x = 'этажей'
        return f"Коттедж имеет {self.__num_of_floors} {x}."


class TotalSquare:
    def __init__(self, total_square):
        self.__total_square = total_square

    def __str__(self):
        return f"Площадь  коттеджа - {self.__total_square} м^2."


class Garage:
    def __init__(self):
        self.__has_garage = True

    def __str__(self):
        if self.__has_garage:
            return f"В коттедже есть гараж."
        else:
            return f"Гаража нет."


class Pool:
    def __init__(self):
        self.__has_pool = False

    def __str__(self):
        if self.__has_pool:
            return f"Имеется бассейн."
        else:
            return f"Бассейн отсутствует."


class Mansion:
    def __init__(self, floor, square, garage, pool):
        self.__square = square
        self.__floor = floor
        self.__garage = garage
        self.__pool = pool

    def __str__(self):
        return f"{self.__square} {self.__floor} {self.__garage} {self.__pool}"


class MansionBuilder(Builder):
    def build_floor(self):
        return Floor(2)

    def get_square(self):
        return TotalSquare(300)

    def build_garage(self):
        return Garage()

    def build_pool(self):
        return Pool()

    def build_mansion(self):
        floor = self.build_floor()
        square = self.get_square()
        garage = self.build_garage()
        pool = self.build_pool()
        mansion = Mansion(floor, square, garage, pool)
        return mansion


builder = MansionBuilder()

mansion = builder.build_mansion()

print(mansion)

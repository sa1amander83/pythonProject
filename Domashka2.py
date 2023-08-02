"""(Дополнительное задание*) С помощью паттерна Фабрика реализовать
создание объекта коттедж и многоэтажное здание. Свойства коттеджа и
многоэтажного дома на Ваше усмотрение. Должны сочетаться два
паттерна – фабрика и строитель."""


class House:

    def create_total_price(self):
        print("Считаем смету на строительство здания")

    def build_foundation(self):
        print("строим фундамент")

    def build_walls(self):
        print("Возводим стены")

    def build_roof(self):
        print("Делаем крышу")

    def build_communcations(self):
        print("прокладываем инженерные сети: электрику, сантехнические трубы, отопление")

    def create_inerior(self):
        print("выполнение внутренней отделки")


class Floors:
    def __init__(self, num_of_floors):
        self.__num_of_floors = num_of_floors

    def __str__(self):
        if self.__num_of_floors % 10 == 1:
            x = 'этаж'
        elif 2 <= self.__num_of_floors % 10 <= 4:
            x = 'этажа'
        else:
            x = 'этажей'
        return f"Здание имеет {self.__num_of_floors} {x}."


class TotalSquare:
    def __init__(self, total_square):
        self.__total_square = total_square

    def __str__(self):
        return f"Площадь  здания - {self.__total_square} м^2."


class Garage:
    def __init__(self):
        self.__has_garage = True

    def __str__(self):
        if self.__has_garage == True:
            return f"В коттедже есть гараж."
        else:
            return f"Гаража нет."


class Mansion:
    def __init__(self, garage, square, floors):
        self.__pool = True
        self.__garage = garage
        self.__square = square
        self.__floors = floors
        self.make_lawn()

    def make_lawn(self):
        print("Завозим газон")

    def __str__(self):
        has_pool = "бассейн на 4х5 метров" if self.__pool else " бассейна нет"
        return f"{self.__square} {self.__floors} {self.__garage}, {has_pool}"


class MansionBuilder(House):
    def __init__(self):
        self.create_total_price()
        self.build_foundation()
        self.build_walls()
        self.build_roof()
        self.build_communcations()
        self.create_inerior()

    def build_floor(self):
        return Floors(2)

    def build_foundation(self):
        print("Заливаем ростверковый фундамент...")
        super().build_foundation()

    def get_square(self):
        return TotalSquare(400)  # задаем площадь коттеджа

    def build_garage(self):
        return Garage()

    def build_mansion(self):
        floors = self.build_floor()
        square = self.get_square()
        garage = self.build_garage()

        mansion = Mansion(floors, square, garage)

        return mansion


class SkyScraper:
    def __init__(self, square, floors):
        self.__square = square
        self.__floor = floors
        self.__heliport = False  # вертолетная площадка по умолчанию есть

    def __str__(self):
        heliport = "Есть вертолетная площадка" if self.__heliport else " Вертолетной площадки нет"
        return f"{self.__square} {self.__floor} {heliport}"


class SkyScraperBuilder(House):
    def __init__(self):  # количество этажей в небоскребе

        self.create_total_price()
        self.build_foundation()
        self.build_walls()
        self.build_roof()
        self.build_communcations()
        self.build_lift()
        self.create_inerior()

    def build_lift(self):
        print("Устанавливаем лифты...")

    def build_floors(self):
        return Floors(51)

    def get_square(self):
        return TotalSquare(40000)

    def build_foundation(self):
        print("Роем огромный котлован под фундамент и  подземную парковку")
        super().build_foundation()

    def build_skycraper(self):
        floors = self.build_floors()
        square = self.get_square()

        skyscraper = SkyScraper(floors, square)

        return skyscraper

    def __str__(self):
        return f""


class HouseFactory:
    @staticmethod
    def get_building(building_type):
        if building_type == 'коттедж':
            building = MansionBuilder().build_mansion()

            # building.build_mansion()
        elif building_type == 'небоскреб':
            building = SkyScraperBuilder().build_skycraper()
        return building


class HouseMaker:
    @staticmethod
    def build_house(building_type):
        house = HouseFactory.get_building(building_type)
        if house != None:
            print(f"Здание {building_type} построено!\n{house}")



HouseMaker.build_house('небоскреб')
# HouseMaker.build_house('коттедж')


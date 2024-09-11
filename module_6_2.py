
from colorama import Fore, Style

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color: str, engine_power: int,):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self, __model: str):
        pass

    def get_horsepower(self, __engine_power: int):
        pass

    def get_color(self, __color: str):
        pass

    def print_info(self):
        print('Модель:', self.__model)
        print('Мощность двигателя:', self.__engine_power)
        print('Цвет:', self.__color)
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f"{Fore.BLUE}Нельзя сменить цвет на '{new_color}'{Style.RESET_ALL}"
                  f"{Fore.BLUE}у этой модели{Style.RESET_ALL}.")
        self.__color = new_color

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Анисов Федор', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Прокопенко Василий'

vehicle1.print_info()

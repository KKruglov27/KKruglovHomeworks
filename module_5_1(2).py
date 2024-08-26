
class House:
    """Название дома, номера этажей"""
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        """Переход к этажу, перечисление этажей"""
        if new_floor > self.number_of_floors:
            print('Ошибка метода в объекте', '"' + self.name + '"' ':', 'Такого этажа не существует.')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Детский мир', 4)
h1.go_to(5)
h2.go_to(10)
h3.go_to(4)

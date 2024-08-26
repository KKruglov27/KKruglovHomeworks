class House:
    """Название дома, номера этажей"""
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """Переход к этажу, перечисление этажей"""
        if new_floor > self.number_of_floors:
            print('Ошибка. Объект:', '"' + self.name + '"' ':', '-', 'Такого этажа не существует.')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors == other.number_of_floors
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __add__(self, other):
        if isinstance(other, House):
            return self.number_of_floors + other.number_of_floors
        if isinstance(other, (int, float,)):
            return House(self.name, self.number_of_floors + other)
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __iadd__(self, other):
        if isinstance(other, House):
            return self.number_of_floors + other.number_of_floors
        if isinstance(other, (int, float,)):
            return House(self.name, self.number_of_floors + other)
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __radd__(self, other):
        if isinstance(other, House):
            return self.number_of_floors + other.number_of_floors
        if isinstance(other, (int, float,)):
            return House(self.name, self.number_of_floors + other)
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __gt__(self, other):
        if isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors > other.number_of_floors
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __ge__(self, other):
        if isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors >= other.number_of_floors
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __lt__(self, other):
        if isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors < other.number_of_floors
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __le__(self, other):
        if isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors <= other.number_of_floors
        raise ValueError('Не может быть реализовано с этими типами данных')

    def __ne__(self, other):
        if isinstance(other.number_of_floors, (int, float)):
            return self.number_of_floors != other.number_of_floors
        raise ValueError('Не может быть реализовано с этими типами данных')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

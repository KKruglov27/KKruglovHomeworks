
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} поел {food.name} и наелся.")
        if not food.edible:
            print(f"{self.name} съел {food.name} и погиб.")
            self.alive = False


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} поел {food.name} и наелся.")
            self.fed = True
        if not food.edible:
            print(f"{self.name} поел {food.name} и не наелся.")


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


A1 = Predator('Хитрый волк')
A2 = Mammal('Хатико')
A3 = Predator('Копатыч')
A4 = Mammal('Хэмми')
P1 = Flower('Цветик-семицветик')
P2 = Fruit('Заводной апельсин')
P3 = Fruit('антоновки')
P4 = Flower('тюльпан')

print(A1.name)
print(P1.name)
print(A4.name)
print(P4.name)

print(A1.alive)
print(A2.fed)
print(A3.alive)
print(A4.fed)
A1.eat(P1)
A2.eat(P2)
A3.eat(P3)
A4.eat(P4)
print(A1.alive)
print(A2.fed)
print(A3.alive)
print(A4.fed)

# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True

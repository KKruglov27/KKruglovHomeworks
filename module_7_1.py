from colorama import Fore, Style

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        product_get = open(self.__file_name, 'r')
        self.various_products = []
        for prod in product_get:
            self.various_products.append(prod)
        print(*self.various_products, sep="")

    def add_products(self, *products):
        addFile = open(self.__file_name, 'a+', encoding='utf-8')
        addFile.seek(0)
        lines = addFile.read().splitlines()
        for J in products:
            for I in lines:
                if J.name in I:
                    print(f'Продукт {Fore.LIGHTWHITE_EX}"{J}"{Style.RESET_ALL} уже есть в магазине')
                    break
            else:
                addFile.write(f'{J}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add_products(p1, p2, p3)

print(s1.get_products())

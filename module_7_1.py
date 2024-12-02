from pprint import pprint
import os.path

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {str(self.weight)}, {self.category}\n"


class Shop():

    __file_name = "product.txt"

    def add(self, *products):
        for i in range(len(products)):
            if s1.get_products():
                if products[i].name in s1.get_products():
                    print(f'Продукт {products[i].name} уже есть в магазине' )
                else:
                    file = open(self.__file_name, "a")
                    file.write(str(products[i]))
                    file.close()



    def get_products(self):
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name, "r")
            f_r = file.read()
            file.close()

            return f_r
        else:
            return None



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Carrot', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())



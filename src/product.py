from src.base_class import BaseProduct
from src.mixin_print import MixinPrint


class Product(MixinPrint, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """Метод реализует строковое отображение"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает результат сложения сумм всех товаров двух категорий"""
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError(f"Other не является объектом класса {self.__class__}")

    @classmethod
    def new_product(cls, product):
        """
        Метод принимает на вход параметры товара в словаре и возвращать созданный объект класса Product
        """
        return cls(name=product["name"],
                   description=product["description"],
                   price=product["price"],
                   quantity=product["quantity"])

    @property
    def price(self):
        """Геттер для атрибута __price"""
        return self.__price

    @price.setter
    def price(self, price):
        """Сеттер для атрибута __price"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        if self.__price > price:
            print(f"Цена товара понизилась. Было: {self.__price}, Стало: {price}")
            user_message = input("Введите y: подтвердить новую цену или n: оставить цену:")
            if user_message in "y":
                self.__price = price

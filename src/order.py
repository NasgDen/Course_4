from src.abstract import AbstractClass
from src.exception import ExceptionZeroQuantity


class Order(AbstractClass):
    """ Класс для создания заказа"""

    def __init__(self, product, quantity):
        """ Конструктор для класса Order """
        self.product = product
        if quantity == 0:
            raise ExceptionZeroQuantity
        self.quantity = quantity
        self.get_price()

    def __str__(self):
        """Метод реализует строковое отображение"""
        return f"{self.product.name} Количество: {self.quantity}шт. Общая стоимость: {self.price} руб."

    def get_price(self):
        """ Метод рассчитывает полную стоимость заказа"""
        self.price = self.product.price * self.quantity
        return self

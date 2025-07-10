from abc import ABC, abstractmethod


class BaseClass(ABC):
    """ Абстрактный класс для класса Product """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product):
        pass

    @abstractmethod
    def price(self):
        pass

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс, определяющий интерфейс для классов продуктов."""

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

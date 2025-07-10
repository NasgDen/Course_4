class MixinPrint:
    """ Класс Mixin для вывода информации о созданном продукте"""

    def __init__(self):
        """ Конструктор для вывода информации о созданном продукте"""
        print(repr(self))

    def __repr__(self):
        """ Функция формирует строку для вывода информации о созданном продукте"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
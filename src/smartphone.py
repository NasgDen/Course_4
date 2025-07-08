from src.product import Product


class Smartphone(Product):
    """ Класс для хранения Смартфонов - дочерний от Product """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """ Конструктор для Смартфонов """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
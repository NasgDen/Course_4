from src.product import Product


class LawnGrass(Product):
    """ Класс для хранения товара - «Трава газонная» """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """ Конструктор для товара - «Трава газонная» """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

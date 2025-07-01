class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    # Метод принимает на вход параметры товара в словаре и возвращать созданный объект класса Product
    @classmethod
    def new_product(cls, product):
        return cls(name=product["name"],
                   description=product["description"],
                   price=product["price"],
                   quantity=product["quantity"])

    # Геттер для атрибута __price
    @property
    def price(self):
        return self.__price

    # Сеттер для атрибута __price
    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        self.__price = price

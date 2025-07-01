class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # Метод принимает на вход параметры товара в словаре и возвращать созданный объект класса Product
    @classmethod
    def new_product(cls, product):
        return cls(name=product["name"],
                   description=product["description"],
                   price=product["price"],
                   quantity=product["quantity"])

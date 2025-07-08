from src.product import Product


class Category:
    name: str
    description: str
    __products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Метод реализует строковое отображение"""
        quantity_products = 0
        for prod in self.__products:
            quantity_products += prod.quantity
        return f"{self.name}, количество продуктов: {quantity_products} шт."

    def add_product(self, product):
        """Метод для добавления товара"""
        if isinstance(product, Product):
            for prod in self.__products:
                if prod.name == product.name:
                    if prod.price >= product.price:
                        product.price = prod.price
                    elif prod.price < product.price:
                        prod.price = product.price
                    prod.quantity += product.quantity
                    self.__products.append(product)
                    Category.product_count += 1
                    return
            self.__products.append(product)
            Category.product_count += product.quantity
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер - выводить список товаров в виде строк"""
        products = ""
        for prod in self.__products:
            products += (f"{str(prod)}\n")
        return products

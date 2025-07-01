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

    # Метод для добавления товара
    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    # Геттер - выводить список товаров в виде строк
    @property
    def products(self):
        products = ""
        for prod in self.__products:
            products += (f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n")
        return products

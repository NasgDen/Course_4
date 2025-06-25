import json
import os

from src.category import Category
from src.product import Product


def read_json_file(path_file: str) -> dict:
    """
    Функуия чтение json файла
    """
    path = os.path.abspath(path_file)
    with open(path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_product_category(path_file: str):
    """
    Функция создания объектов из класса Product и Category
    """
    data = read_json_file(path_file)
    categories = []
    products = []
    for cat in data:
        product_for_cat = []
        for prod in cat["products"]:
            product = Product(prod["name"], prod["description"], prod["price"], prod["quantity"])
            products.append(product)
            product_for_cat.append(prod["name"])
        category_temp = Category(cat["name"], cat["description"], product_for_cat)
        categories.append(category_temp)
    return products, categories


if __name__ == "__main__":
    products, categories = get_product_category("../data/products.json")

    print("** Данные выгруженные из json файла **")
    for index in range(len(products)):
        print("*" * 30)
        print(f"Наименование: {products[index].name}")
        print(f"Описание: {products[index].description}")
        print(f"Цена: {products[index].price}")
        print(f"Количество: {products[index].quantity}")
    for index in range(len(categories)):
        print("*" * 30)
        print(f"Наименование категории: {categories[index].name}")
        print(f"Описание: {categories[index].description}")
        print(f"Товары: {categories[index].products}")
        print(f"Количество категорий: {categories[index].category_count}")
        print(f"Количество товара: {categories[index].product_count}")

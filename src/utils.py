import json
import os
from src.product import Product
from src.category import Category

def read_json_file(path_file):
    """
    Функуия чтение json файла
    """
    path = os.path.abspath(path_file)
    with open(path_file, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data
from src.product import Product
from unittest.mock import patch


def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 170000.0,
         "quantity": 10})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 170000.0
    assert new_product.quantity == 10
    new_product.price = 180000.0
    assert new_product.price == 170000.0
    # new_product.price = 90000.0
    # mock_input.return_value = "y"
    # assert new_product.price == 90000.0
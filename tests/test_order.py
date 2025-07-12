import pytest

from src.exception import ExceptionZeroQuantity
from src.order import Order
from src.product import Product


def test_order(capsys):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    purchase = Order(product1, 2)
    assert purchase.product.name == "Samsung Galaxy S23 Ultra"
    assert purchase.quantity == 2
    assert purchase.price == 360000
    assert str(purchase) == "Samsung Galaxy S23 Ultra Количество: 2шт. Общая стоимость: 360000.0 руб."


def test_order_zero_quantity():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    with pytest.raises(ExceptionZeroQuantity):
        Order(product1, 0)

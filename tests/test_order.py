from src.product import Product
from src.order import Order


def test_order(capsys):
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    purchase = Order(product1, 2)
    assert purchase.product.name == "Samsung Galaxy S23 Ultra"
    assert purchase.quantity == 2
    assert purchase.price == 360000
    assert str(purchase) == "Samsung Galaxy S23 Ultra Количество: 2шт. Общая стоимость: 360000.0 руб."
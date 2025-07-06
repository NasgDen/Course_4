from src.product import Product


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

    assert str(product_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."

    assert product_1 + new_product == 2600000.0

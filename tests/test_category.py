from src.category import Category
from src.product import Product


def test_category_init(category_1):
    product5 = Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=170000.0, quantity=5
    )
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации"

    assert category_1.products == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert category_1.category_count == 1
    assert category_1.product_count == 1

    category_1.add_product(product5)

    assert str(category_1) == "Смартфоны, количество продуктов: 15 шт."

    category_1 = Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=['55" QLED 4K'],
    )
    assert category_1.product_count == 3
    assert category_1.category_count == 2


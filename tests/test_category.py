from src.category import Category


def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description == "Смартфоны, как средство не только коммуникации"
    )
    assert category_1.products == ["Samsung Galaxy C23 Ultra"]
    assert category_1.category_count == 1
    assert category_1.product_count == 1
    category_1 = Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=['55" QLED 4K'],
    )
    assert category_1.product_count == 2
    assert category_1.category_count == 2

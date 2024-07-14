from multiplos_valores import calculate_total
import pytest

@pytest.mark.parametrize('price', [10.00, 50.00, 100.00])
@pytest.mark.parametrize('discount_rate', [0.2, 0.15, 0.34])
@pytest.mark.parametrize('tax_rate', [0.12, 0.15, 0.2])
def test_calculate_total(price, discount_rate, tax_rate):
    discount_price = price * (1 - discount_rate)
    price_tax = discount_price * (1 + tax_rate)
    assert calculate_total(price, discount_rate, tax_rate) == round(price_tax, 2)
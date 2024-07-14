def calculate_total(price, discount_rate, tax_rate):
    discount_price = price * (1 - discount_rate)
    price_tax = discount_price * (1 + tax_rate)
    return round(price_tax, 2)
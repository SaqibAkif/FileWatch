def apply_discount(price):
    return price - 50
def apply_tax(price):
    return price + 20
def generate_Bill(masala_price,func):
    return func(masala_price)

print(generate_Bill(250,apply_discount))
print(generate_Bill(250,apply_tax))
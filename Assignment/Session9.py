def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate)
    return final_price

# Test
result = calculate_final_price(1200, 0.15)
print("Final Price:", result)


def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 30
    else:
        return 50

# Without city argument
print("Delivery Charge:", get_delivery_charge(500))

# With city argument
print("Delivery Charge:", get_delivery_charge(500, "Surat"))


def format_coupon_message(username, discount=10):
    return f"Hi {username}, you get {discount}% off!"

# Custom discount
print(format_coupon_message("Rahul", 20))

# Default discount
print(format_coupon_message("Priya"))



def apply_discount(price, rate=0.10):
    discounted_price = price - (price * rate)
    return discounted_price

# Calling with only price
print("Discounted Price:", apply_discount(1000))


def calculate_cashback(amount, cashback_rate=0.05):
    cashback = amount * cashback_rate
    return cashback

# Zomato order
zomato_cashback = calculate_cashback(500)

# Flipkart order
flipkart_cashback = calculate_cashback(2000, 0.07)

print("Zomato Cashback: Rs.", zomato_cashback)
print("Flipkart Cashback: Rs.", flipkart_cashback)
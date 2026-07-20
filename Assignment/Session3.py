# Task 1

followers = 2500              # Integer
average_rating = 4.7          # Float
favorite_app = "Instagram"    # String
is_premium_user = True        # Boolean

print("Followers:", followers)
print("Type:", type(followers))

print("Average Rating:", average_rating)
print("Type:", type(average_rating))

print("Favorite App:", favorite_app)
print("Type:", type(favorite_app))

print("Premium User:", is_premium_user)
print("Type:", type(is_premium_user))



# Task 2

price = input("Enter Zomato order price: ")

price = float(price)

gst = price * 0.18

final_bill = price + gst

print("Original Price:", price)
print("GST (18%):", gst)
print("Final Bill Amount:", final_bill)


# Task 3

prices = ['199.99', '299.50', '150']

float_prices = [float(price) for price in prices]

total = sum(float_prices)

print("Prices after conversion:", float_prices)
print("Total Cart Value:", total)



# Task 4

def is_discount_applicable(order_amount):
    return order_amount > 500

print("Order Amount: 450")
print("Discount Applicable:", is_discount_applicable(450))

print()

print("Order Amount: 750")
print("Discount Applicable:", is_discount_applicable(750))



# Task 5

ratings = [4.5, 3.0, 5, 4.2]

float_ratings = [float(rating) for rating in ratings]

highest_rating = max(float_ratings)

print("Ratings after conversion:", float_ratings)
print("Highest Rating:", highest_rating)
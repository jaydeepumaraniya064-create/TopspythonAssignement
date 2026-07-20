# Check IPL ticket booking eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for IPL ticket booking")
else:
    print("Not eligible")

    # Categorize user based on followers

followers = int(input("Enter number of followers: "))

if followers < 10000:
    print("Micro Influencer")
elif followers <= 100000:
    print("Rising Star")
else:
    print("Celebrity")



    # Check Zomato free delivery eligibility

total = float(input("Enter your Zomato order total: ₹"))

if total > 299:
    print("Apply Free Delivery")
elif 200 <= total <= 299:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")


    # Flipkart cashback eligibility using nested if

# cart_value = float(input("Enter cart value: ₹"))
# payment_method = input("Enter payment method (UPI/Card/Cash): ")

# if cart_value > 1000:
#     if payment_method.lower() == "upi":
#         print("Eligible for 10% cashback")
#     else:
#         print("Eligible for 5% cashback")
# else:
#     print("No cashback")
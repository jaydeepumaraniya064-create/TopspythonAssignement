def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Example
print(safe_divide(20, 4))
print(safe_divide(20, 0))





try:
    reviews = int(input("Enter number of reviews: "))
    stars = float(input("Enter total stars: "))

    average = stars / reviews
    print("Average Rating =", round(average, 2))

except ValueError:
    print("Error: Please enter only numeric values.")

except ZeroDivisionError:
    print("Error: Number of reviews cannot be zero.")



# Custom Exception
class InvalidDurationError(Exception):
    pass

def get_playlist_duration(songs):
    total_seconds = 0

    for duration in songs:
        if duration < 0:
            raise InvalidDurationError("Song duration cannot be negative.")
        total_seconds += duration

    return total_seconds / 60

# Example
try:
    playlist = [180, 240, 300, 150]
    print("Total Duration:", get_playlist_duration(playlist), "minutes")

    playlist2 = [180, -200, 250]
    print(get_playlist_duration(playlist2))

except InvalidDurationError as e:
    print("Error:", e)






try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

except ValueError:
    print("Invalid input! Please enter correct numbers.")

else:
    print("Total Price = ₹", total)

finally:
    print("Thank you for shopping!")






try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Result =", result)

finally:
    print("Program completed.")


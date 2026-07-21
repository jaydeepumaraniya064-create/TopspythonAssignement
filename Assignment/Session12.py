# Lambda function to add 18% GST
gst = lambda price: price + (price * 18 / 100)

prices = [100, 250, 500]

print("Prices after adding 18% GST:")
for p in prices:
    print(f"Original Price: ₹{p} --> GST Price: ₹{gst(p):.2f}")




    songs = [
    "  shape OF you ",
    " blinding LIGHTS",
    "   beLiever",
    "peRfect  ",
    "  senorita "
]

# Clean song titles
clean_songs = list(map(lambda song: song.strip().title(), songs))

print("Original Songs:")
print(songs)

print("\nCleaned Songs:")
print(clean_songs)


products = [
    "Smartphone",
    "Laptop",
    "Shoes",
    "speaker",
    "Watch",
    "Shirt",
    "Tablet",
    "Sandals"
]

# Filter products starting with 'S'
filtered_products = list(filter(lambda p: p.lower().startswith('s'), products))

print("Products starting with 'S':")
print(filtered_products)



from functools import reduce

orders = [120, 340, 560, 80]

total_bill = reduce(lambda x, y: x + y, orders)

print("Order Amounts:", orders)
print("Total Bill Amount =", total_bill)



[40, 60, 80, 120]

from functools import reduce

numbers = [40, 60, 80, 120]

# Step 1: Double each number
doubled = list(map(lambda x: x * 2, numbers))

# Step 2: Keep only numbers greater than 100
filtered = list(filter(lambda x: x > 100, doubled))

# Step 3: Find the sum using reduce()
total = reduce(lambda x, y: x + y, filtered)

print("Original Numbers :", numbers)
print("Doubled Numbers  :", doubled)
print("Filtered Numbers :", filtered)
print("Final Sum        :", total)
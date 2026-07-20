# Task 1

product_name = input("Enter product name: ")

print("Original Product Name :", product_name)
print("Uppercase :", product_name.upper())
print("Lowercase :", product_name.lower())


# Task 2

def clean_brand_name(name):
    cleaned = name.strip().replace("-", " ")
    return cleaned

# Test
brand = " oneplus-Nord "
print("Original :", brand)
print("Cleaned :", clean_brand_name(brand))



# Task 3

product = "Apple iPhone 14 Pro Max"

parts = product.split()

brand = parts[0]
model = " ".join(parts[1:])

print("Brand :", brand)
print("Model :", model)


# Task 4

def format_product_display(name, price):
    return f"{name} - ₹{price}"

# Test
product = "Boat Earbuds"
price = 1299

result = format_product_display(product, price)
print(result)



# Task 5

messy_products = [
    " mi-Band 5 ",
    " SAMSUNG-Galaxy ",
    " realme-Book "
]

cleaned_products = []

for product in messy_products:
    clean_name = product.strip()          # Remove extra spaces
    clean_name = clean_name.replace("-", " ")   # Replace hyphen
    clean_name = clean_name.title()       # Convert to Title Case
    cleaned_products.append(clean_name)

print("Original List:")
print(messy_products)

print("\nCleaned List:")
print(cleaned_products)
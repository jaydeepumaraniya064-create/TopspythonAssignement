# Task 1

playlist_ids = [101, 102, 103, 104, 105]

print("Original Playlist IDs:", playlist_ids)

# Add a new playlist ID
playlist_ids.append(106)

print("Updated Playlist IDs:", playlist_ids)



# Task 2

cart_items = ['t-shirt', 'shoes']

print("Original Cart:", cart_items)

# Add multiple items
cart_items.extend(['jeans', 'cap'])

print("Final Cart:", cart_items)



# Task 3

def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item

# Sample order list
order_list = ['Pizza', 'Burger', 'Cold Drink', 'Ice Cream']

print("Original Order:", order_list)

removed = remove_last_item(order_list)

print("Removed Item:", removed)
print("Updated Order:", order_list)



# Task 4

insta_filters = ("Clarendon", "Juno", "Lark", "Valencia")

print("Original Tuple:", insta_filters)

# Try to update the second filter
# insta_filters[1] = "Gingham"

# This line will produce:
# TypeError: 'tuple' object does not support item assignment

print("Tuple remains unchanged:", insta_filters)

# Explanation:
# Tuples are immutable, meaning their values cannot be changed
# after the tuple has been created.



# Task 5

# Favorite genres may change, so use a list.
favorite_genres = ["Pop", "Rock", "Hip-Hop"]

# Train classes are fixed, so use a tuple.
train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")

print("Favorite Genres:", favorite_genres)
print("Train Classes:", train_classes)
# Task 1

playlist_prices = {
    "Top Hits India": 199,
    "Workout Mix": 149,
    "Chill Vibes": 99,
    "Party Songs": 249,
    "Romantic Hits": 179
}

print("Playlist Prices:")
print(playlist_prices)


# Task 2

playlist_prices = {
    "Top Hits India": 199,
    "Workout Mix": 149,
    "Chill Vibes": 99,
    "Party Songs": 249,
    "Romantic Hits": 179
}

def update_playlist_price(playlist, new_price):
    if playlist in playlist_prices:
        playlist_prices[playlist] = new_price
        print(f"{playlist} price updated successfully.")
    else:
        print("Playlist not found.")

# Update one playlist
update_playlist_price("Workout Mix", 199)

print("\nUpdated Playlist Prices:")
print(playlist_prices)



# Task 3

playlist_prices = {
    "Top Hits India": 199,
    "Workout Mix": 149,
    "Chill Vibes": 99,
    "Party Songs": 249,
    "Romantic Hits": 179
}

# Delete a playlist
del playlist_prices["Chill Vibes"]

print("Dictionary after deleting 'Chill Vibes':")
print(playlist_prices)


# Task 4

# Restaurants ordered from Zomato
set1 = {
    "McDonald's",
    "Domino's",
    "KFC",
    "Pizza Hut",
    "Subway"
}

# Restaurants ordered from Swiggy
set2 = {
    "Domino's",
    "Burger King",
    "KFC",
    "Biryani By Kilo",
    "Subway"
}

# Union
union_result = set1.union(set2)

# Intersection
intersection_result = set1.intersection(set2)

print("Restaurants Ordered from Zomato:")
print(set1)

print("\nRestaurants Ordered from Swiggy:")
print(set2)

print("\nUnion of Sets:")
print(union_result)

print("\nIntersection of Sets:")
print(intersection_result)

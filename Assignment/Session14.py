# Task 1

songs = [
    "Shape of You",
    "Perfect",
    "Believer",
    "Kesariya",
    "Blinding Lights"
]

with open("my_playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")

print("my_playlist.txt created successfully.")




# Task 2

with open("my_playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())


import csv

matches = [
    ["Match", "Team1", "Team2", "Winner"],
    ["Match 1", "CSK", "MI", "CSK"],
    ["Match 2", "RCB", "GT", "GT"],
    ["Match 3", "KKR", "SRH", "KKR"],
    ["Match 4", "RR", "PBKS", "RR"],
    ["Match 5", "DC", "LSG", "LSG"]
]

with open("ipl_matches.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(matches)

print("CSV file created successfully.")

import csv

with open("ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Winning Teams:\n")

    for row in reader:
        print(f"{row['Match']} Winner: {row['Winner']}")


    import json

user = {
    "username": "jaydeep123",
    "followers": 2500,
    "bio": "Python Developer"
}

with open("user_profile.json", "w") as file:
    json.dump(user, file, indent=4)

print("JSON file created successfully.")


import json

with open("user_profile.json", "r") as file:
    profile = json.load(file)

print("Username :", profile["username"])
print("Followers:", profile["followers"])


from pathlib import Path

file_path = Path("zomato_orders.json")

if file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")

    
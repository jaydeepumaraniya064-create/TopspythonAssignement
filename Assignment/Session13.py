def reverse_string(s):
    # Base case
    if len(s) == 0:
        return ""

    # Recursive case
    return s[-1] + reverse_string(s[:-1])


# Example
text = input("Enter a string: ")
print("Reversed String:", reverse_string(text))




def sum_playlist_durations(durations):
    # Base case
    if len(durations) == 0:
        return 0

    # Recursive case
    return durations[0] + sum_playlist_durations(durations[1:])


# Example
playlist = [180, 240, 200, 150]

print("Playlist Durations:", playlist)
print("Total Duration:", sum_playlist_durations(playlist), "seconds")



count = 10

def update_count():
    count = 5
    print("Inside:", count)

update_count()

print("Outside:", count)




def count_likes(posts):
    total = posts["likes"]

    for reply in posts.get("replies", []):
        total += count_likes(reply)

    return total


# Example nested dictionary
instagram_post = {
    "likes": 120,
    "replies": [
        {
            "likes": 30,
            "replies": [
                {
                    "likes": 15,
                    "replies": []
                },
                {
                    "likes": 10,
                    "replies": []
                }
            ]
        },
        {
            "likes": 25,
            "replies": [
                {
                    "likes": 20,
                    "replies": []
                }
            ]
        }
    ]
}

print("Total Likes:", count_likes(instagram_post))




# Global variable
app_status = "Online"

print("Before Function Call")
print("Global app_status:", app_status)


def show_status():
    # Local variable
    user_status = "Typing..."

    print("\nInside Function")
    print("Local user_status:", user_status)
    print("Global app_status:", app_status)


show_status()

print("\nAfter Function Call")
print("Global app_status:", app_status)

# Uncommenting the next line will produce an error
# print(user_status)

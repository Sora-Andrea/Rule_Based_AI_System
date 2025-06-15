# User Input
genre = input("Genre (action/comedy/drama/sci-fi)? ").lower()
time_available = int(input("Time (minutes)? "))

# Rules and dataset
if genre == "action" and time_available >= 120:
    movie = "Ballerina"
elif genre == "action":
    movie = "Kung Fury"
elif genre == "comedy" and time_available >= 120:
    movie = "Deadpool & Wolverine"
elif genre == "comedy":
    movie = "Scary Movie"
elif genre == "drama":
    movie = "The Shawshank Redemption" if time_available >= 120 else "The Town"
elif genre == "sci-fi":
    movie = "Avatar" if time_available >= 120 else "Valerian and the City of a Thousand Planets"
else:
    movie = "Whiplash"

# Output
print(f"Based on your choices, I recommend: {movie}")

import random

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

msg = "Welcome to the Movie Night Recommender!\n\
Available genres: Action, Comedy, Drama, Sci-Fi, Horror\n\
Enter a genre: "
genres = ["action", "comedy", "drama", "sci-fi", "horror"]
mov_rec = "You should watch: "
genre_err = "Sorry, that genre is not available. Try again!\n"
choice = ""

try:
    while True:
        choice = input(msg)

        if choice.lower() not in genres:
            print(genre_err)
        else:
            # print(movies[choice.capitalize()])
            print(f'\n{mov_rec} {random.choice(movies[choice.title()])}\n')
except KeyboardInterrupt:
    print('\nctrl+c detected, exiting...')

print('\nGoodbye!')

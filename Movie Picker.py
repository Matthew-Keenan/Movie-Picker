# Every movie is constructed by new_movie function
# Takes input of name, length, and genre to filter into a new list 
# Random number generator picks a random number within the total number of movies in the new list
# Movie title is displayed, removed from unwatched and added to watched 
# Functionality to add new movies to either list
# Starts by asking if you want to add or pick a movie or show a movie
import random


# Ask user for input on if they are adding a new movie, picking an existing movie, or displaying
# all unwatched movies. Action variable is assigned to the users input after it has been made
# lowercase. Calls which_action function to process what the user typed.
def action_pick():
    action_input = input("Do you want to add a movie, pick a movie, or show all movies? ")
    print()
    action = action_input.lower()
    which_action(action)


# Takes the users input from action_pick and processes it. If it is "add", "pick", or "show", the
# corresponding function is called. If the input is something else, a warning is shown and the
# function action_pick is called
def which_action(some_action):
    if some_action == "add" or some_action == "pick" or some_action == "show":
        if some_action == "add":
            add_movie()
        elif some_action == "pick":
            pick_movie()
        else:
            show_movies()
    else:
        print("Please type 'add', 'pick', or 'show'.")
        action_pick()


# pick_movie asks for more user input, this time asking if the user wants any movie from
# Unwatched.txt to be chosen, or if there is a time constraint that needs to be considered.
# Pick variable is assigned to user input and made lowercase. Calls which_pick to process the user input.
def pick_movie():
    how_to_pick = input(
        "Would you like a movie chosen by length, by genre, or fully random? (Type 'length', 'genre', or 'random') ")
    print()
    pick = how_to_pick.lower()
    which_pick(pick)


# Takes user input sent by pick_movie and processes it. If it is "genre", the program asks for a
# genre from the user and calls the corresponding function. If it is "random", the corresponding
# function is called. If it is "length", more user input is asked for. Variable maxLength takes
# the (minute) number input from the user, then the function picked_by_length is called.
# If the input is something else, a warning is shown and function pick_movie is called again.
def which_pick(some_pick):
    if some_pick == 'length' or some_pick == 'random' or 'genre':
        if some_pick == 'length':
            max_length = int(input("Type the maximum length the movie can be (in minutes). "))
            picked_by_length(max_length)
        elif some_pick == 'genre':
            what_genre = input("Type the genre you want the movie to be. ")
            genre = what_genre.lower()
            picked_by_genre(genre)
        else:
            picked_at_random()
    else:
        print("Please type 'length' or 'random'")
        pick_movie()


# Asks user for input on if the movie being added has been watched or unwatched. Takes the input and
# assigns it to variable answer, and is made lowercase. Function which_answer is called to process
# the input.
def add_movie():
    new_or_old = input("Has this movie been watched yet? (Type Watched or Unwatched). ")
    print()
    answer = new_or_old.lower()
    which_answer(answer)


# Takes the user input variable answer and processes it. If answer is "watched", the user inputs
# the movie title, length, and genre and new_movie function is called with the information. If answer
# is "unwatched", the user inputs the movie title, length, and genre and old_movie is called with the
# information. If answer is neither, a warning is displayed and function add_movie is called again.
def which_answer(answer):
    if answer == "watched" or answer == "unwatched":
        if answer == "unwatched":
            movie = input("Type the movie name, length (in minutes), and genre, all separated by commas. ")
            inputs = movie.split(",")
            new_movie(inputs[0], inputs[1], inputs[2])
        else:
            movie = input("Type the movie name, length (in minutes), and genre, all separated by commas. ")
            inputs = movie.split(",")
            old_movie(inputs[0], inputs[1], inputs[2])
    else:
        print("Type 'watched' or 'unwatched'")
        add_movie()


# Opens unwatched movie text file, reads all of the lines, and prints out every movie, line by line,
# with the title, length, and genre.
def show_movies():
    watched_file = open("Unwatched.txt", "r")
    lines = watched_file.readlines()
    for line in lines:
        print(line)


# Takes in the title, length, and genre values, opens the unwatched movie text file, and prints
# the new movie and its info on a new line.
def new_movie(title, length, genre):
    unwatched_file = open("Unwatched.txt", "a")
    unwatched_file.write(f"Movie: {title}, Length: {length} minutes, Genre: {genre}\n")
    unwatched_file.close()


# Takes in the title, length, and genre values, opens the watched movie text file, and prints
# the old movie and its info on a new line.
def old_movie(title, length, genre):
    watched_file = open("Watched.txt", "a")
    watched_file.write(f"Movie: {title}, Length: {length} minutes, Genre: {genre}\n")
    watched_file.close()


# Takes in the max length the user wants the movie to be, opens the unwatched movie text file,
# processes each movie line, and adds each movie that fits the time length to a new list. A movie
# from the new list is picked at random and displayed.  
def picked_by_length(max_length):
    movie_list = []
    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()

    for line in lines:
        movie_data = line.split(",")
        split_data = movie_data[1]
        get_length = split_data.split()
        length = int(get_length[1])
        if length <= max_length:
            movie_list.append(line)

    rand_num = random.randint(0, (len(movie_list) - 1))
    rand_movie = movie_list[rand_num]
    print(rand_movie)


# Takes in what the user wants the genre to be, opens the unwatched movie text file, processes each
# movie line, and add each movie that matches in genre to a new list. A movie from the new list is 
# picked at random and displayed
def picked_by_genre(genre):
    movie_list = []
    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()

    for line in lines:
        movie_data = line.split(",")
        get_genre_part = movie_data[2]
        split_genre_part = get_genre_part.split()
        movie_genre = split_genre_part[1]
        if movie_genre.lower() == genre:
            movie_list.append(line)

    if len(movie_list) == 0:
        print("There are no movies with that genre. Please start again. ")
        print()
        action_pick()
    else:
        rand_num = random.randint(0, (len(movie_list) - 1))
        rand_movie = movie_list[rand_num]
        print(rand_movie)


# Opens the unwatched movie text file, processes each movie line, and picks one at random and displays it.
def picked_at_random():
    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()
    rand_num = random.randint(0, (len(lines) - 1))

    print(lines[rand_num])


# Calls function action_pick
def main():
    action_pick()


main()

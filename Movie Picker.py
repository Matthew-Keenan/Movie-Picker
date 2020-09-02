# Movie program has two text files of movies - unwatched and watched
# Every movie is constructed by newMovie function
# Takes input of name, length, and genre to filter into a new list 
# Random number generator picks a random number within the total number of movies in the new list
# Movie title is displayed, removed from unwatched and added to watched 
# Functionality to add new movies to either list
# Starts by asking if you want to add or pick a movie or show a movie
import random

def actionPick():
    actionInput = input("Do you want to add a movie, pick a movie, or show all movies? ")
    print()
    action = actionInput.lower()

    if action == "add" or action == "pick" or action == "show":
        if action == "add":
            addMovie()
        elif action == "pick":
            pickMovie()
        else:
            showMovies()
    else:
        print("Please type 'add', 'pick', or 'show'.")  
        actionPick()

def pickMovie():
    howToPick = input("Would you like a movie chosen by length or fully random? (Type 'length' or 'random') ")
    print()
    pick = howToPick.lower()

    if pick == 'length' or pick == 'random':
        if pick == 'length':
            maxLength = int(input("Type the maximum length the movie can be (in minutes). "))
            pickedByLength(maxLength)
        else:
            pickedAtRandom()
    else:
        print("Please type 'length' or 'random'") 
        pickMovie()

def addMovie():
    newOrOld = input("Has this movie been watched yet? (Type Watched or Unwatched). ")
    print()
    answer = newOrOld.lower()

    if answer == "watched" or answer == "unwatched":
        if answer == "unwatched":
            movie = input("Type the movie name, length (in minutes), and genre, all separated by commas. ")
            inputs = movie.split(",")
            newMovie(inputs[0], inputs[1], inputs[2])
        else:
            movie = input("Type the movie name, length (in minutes), and genre, all separated by commas. ")
            inputs = movie.split(",")
            oldMovie(inputs[0], inputs[1], inputs[2])
    else:
        print("Type 'watched' or 'unwatched'") 
        addMovie()

def showMovies():
    watched_file = open("Unwatched.txt", "r")
    lines = watched_file.readlines()
    for line in lines:
        print(line)

def newMovie(title, length, genre):
    unwatched_file = open("Unwatched.txt", "a")
    unwatched_file.write(f"Movie: {title}, Length: {length} minutes, Genre: {genre}\n")
    unwatched_file.close()

def oldMovie(title, length, genre):
    watched_file = open("Watched.txt", "a")
    watched_file.write(f"Movie: {title}, Length: {length} minutes, Genre: {genre}\n")
    watched_file.close()

def pickedByLength(maxLength):
    movieList = []

    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()

    for line in lines:
        movieData = line.split(",")
        splitData = movieData[1]
        getLength = splitData.split()
        length = int(getLength[1])
        if length <= maxLength:
            movieList.append(line)
    
    randNum = random.randint(0, (len(movieList)- 1))

    randMovie = movieList[randNum]

    print(randMovie)

def pickedAtRandom():
    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()
    randNum = random.randint(0, (len(lines)- 1))

    print(lines[randNum])

def main():
    actionPick()

main()
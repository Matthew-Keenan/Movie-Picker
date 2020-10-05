# Every movie is constructed by newMovie function
# Takes input of name, length, and genre to filter into a new list 
# Random number generator picks a random number within the total number of movies in the new list
# Movie title is displayed, removed from unwatched and added to watched 
# Functionality to add new movies to either list
# Starts by asking if you want to add or pick a movie or show a movie
import random

# Ask user for input on if they are adding a new movie, picking an existing movie, or displaying
# all unwatched movies. Action variable is assigned to the users input after it has been made
# lowercase. Calls whichAction function to process what the user typed.
def actionPick():
    actionInput = input("Do you want to add a movie, pick a movie, or show all movies? ")
    print()
    action = actionInput.lower()
    whichAction(action)

# Takes the users input from actionPick and processes it. If it is "add", "pick", or "show", the 
# corresponding function is called. If the input is something else, a warning is shown and the
# function actionPick is called
def whichAction(someAction):
    if someAction == "add" or someAction == "pick" or someAction == "show":
        if someAction == "add":
            addMovie()
        elif someAction == "pick":
            pickMovie()
        else:
            showMovies()
    else:
        print("Please type 'add', 'pick', or 'show'.")  
        actionPick()

# pickMovie asks for more user input, this time asking if the user wants any movie from 
# Unwatched.txt to be chosen, or if there is a time constraint that needs to be considered.
# Pick variable is assigned to user input and made lowercase. Calls whichPick to process the user input. 
def pickMovie():
    howToPick = input("Would you like a movie chosen by length, by genre, or fully random? (Type 'length', 'genre', or 'random') ")
    print()
    pick = howToPick.lower()
    whichPick(pick)

# Takes user input sent by pickMovie and processes it. If it is "genre", the program asks for a 
# genre from the user and calls the corresponding function. If it is "random", the corresponding
# function is called. If it is "length", more user input is asked for. Variable maxLength takes
# the (minute) number input from the user, then the function pickedByLength is called.
# If the input is something else, a warning is shown and function pickMovie is called again.
def whichPick(somePick):
    if somePick == 'length' or somePick == 'random' or 'genre':
        if somePick == 'length':
            maxLength = int(input("Type the maximum length the movie can be (in minutes). "))
            pickedByLength(maxLength)
        elif somePick == 'genre':
            whatGenre = input("Type the genre you want the movie to be. ")
            genre = whatGenre.lower()
            pickedByGenre(genre)
        else:
            pickedAtRandom()
    else:
        print("Please type 'length' or 'random'") 
        pickMovie()

# Asks user for input on if the movie being added has been watched or unwatched. Takes the input and 
# assigns it to variable answer, and is made lowercase. Function whichAnswer is called to process
# the input.
def addMovie():
    newOrOld = input("Has this movie been watched yet? (Type Watched or Unwatched). ")
    print()
    answer = newOrOld.lower()
    whichAnswer(answer)

# Takes the user input variable answer and processes it. If answer is "watched", the user inputs
# the movie title, length, and genre and newMovie function is called with the information. If answer
# is "unwatched", the user inputs the movie title, length, and genre and oldMovie is called with the
# information. If answer is neither, a warning is displayed and function addMovie is called again.
def whichAnswer(answer):
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

# Opens unwatched movie text file, reads all of the lines, and prints out every movie, line by line,
# with the title, length, and genre.
def showMovies():
    watched_file = open("Unwatched.txt", "r")
    lines = watched_file.readlines()
    for line in lines:
        print(line)

# Takes in the title, length, and genre values, opens the unwatched movie text file, and prints
# the new movie and its info on a new line.
def newMovie(title, length, genre):
    unwatched_file = open("Unwatched.txt", "a")
    unwatched_file.write(f"Movie: {title}, Length: {length} minutes, Genre: {genre}\n")
    unwatched_file.close()

# Takes in the title, length, and genre values, opens the watched movie text file, and prints
# the old movie and its info on a new line.
def oldMovie(title, length, genre):
    watched_file = open("Watched.txt", "a")
    watched_file.write(f"Movie: {title}, Length: {length} minutes, Genre: {genre}\n")
    watched_file.close()

# Takes in the max length the user wants the movie to be, opens the unwatched movie text file, 
# processes each movie line, and adds each movie that fits the time length to a new list. A movie
# from the new list is picked at random and displayed.  
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

# Takes in what the user wants the genre to be, opens the unwatched movie text file, processes each
# movie line, and add each movie that matches in genre to a new list. A movie from the new list is 
# picked at random and displayed
def pickedByGenre(genre):
    movieList = []
    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()

    for line in lines:
        movieData = line.split(",")
        getGenrePart = movieData[2]
        splitGenrePart = getGenrePart.split()
        movieGenre = splitGenrePart[1]
        if movieGenre.lower() == genre:
            movieList.append(line)
    
    if len(movieList) == 0:
        print("There are no movies with that genre. Please start again. ")
        print()
        actionPick()
    else:
        randNum = random.randint(0, (len(movieList)- 1))
        randMovie = movieList[randNum]
        print(randMovie)

# Opens the unwatched movie text file, processes each movie line, and picks one at random and displays it.
def pickedAtRandom():
    movies = open("Unwatched.txt", "r")
    lines = movies.readlines()
    randNum = random.randint(0, (len(lines)- 1))

    print(lines[randNum])

# Calls funtion actionPick 
def main():
    actionPick()

main()
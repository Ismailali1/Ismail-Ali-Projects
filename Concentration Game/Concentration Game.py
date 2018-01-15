import random

 #Memorization game
# Ismail Ali
# 300008883
def hist(deck):
    #list of string ---- list of string, shows distribution of a string in a list
    answer = {}
    special = set(deck)
    for i in special:
        answer[i] = deck.count(i)
    return answer


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE

    random.shuffle(deck)


def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None] * size

    letter = 'A'
    for i in range(len(board) // 2):
        board[i] = letter
        board[i + len(board) // 2] = board[i]
        letter = chr(ord(letter) + 1)
    return board


def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i + 1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()


def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    discovered[p2] = original_board[p2]
    discovered[p1] = original_board[p1]
    print_board(discovered)
    wait_for_player()
    if discovered[p1] != board[p2]:
        discovered[p1] = "*"
        discovered[p2] = "*"


#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    try:
        raw_board = open(file).read().splitlines()
        for i in range(len(raw_board)):
            raw_board[i] = raw_board[i].strip()
        return raw_board
    except FileNotFoundError:
        noFile = []
        return noFile


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board= []
    for i in l:
        if i != "*":
            playable_board.append(i)

    numbercount = hist(playable_board)
    removed_strings = []
    for i,j in numbercount.items():
        if j % 2 == 1:
            removed_strings.append(i)
    for i in removed_strings:
        playable_board.remove(i)

    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    if len(l) == 0:
        return True
    elif len(l) == 1:
        return False
    flag = True
    for i in l:
        if l.count(i) != 2:
            flag = False
    return flag

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    print("ready to play...\n")
    gameloop = True
    guess = 0
    discovered = []
    for i in range(0,len(board)):
        discovered.append("*")





    while gameloop:
        print("\n"*8)
        print_board(discovered)
        print()
        print("Enter two distinct positions on the board that you want revealed.\ni.e two integers in the range  [1," + str(
            len(board)) + "]")
        p1 = int(input("Enter position 1: "))
        p2 = int(input("Enter position 2: "))
        if p1 == p2:
            print("you chose the same positions.\n Please try again, this guess didn't count.")
            print("your current number of guesses is " + str(guess))
            continue
        if (p2 > len(board)) or (p2 < 1) or (p1 > len(board)) or (p1 < 1):
            print("your value is out of range. Please try again, number of attempts remain unaffected.")
            continue

        p1 = p1 - 1
        p2 = p2 - 1

        if discovered[p1] != "*" or discovered[p2] != "*":
            print(
                "One or both of your chosen positions has already been paired, number of attempts remain the same. Please try again.")
            continue
        print_revealed(discovered, p1, p2, board)


        if discovered.count("*") ==0:
            gameloop = False



        guess = guess + 1

    print("Congrats! It took you", guess, " guesses.\nYou took", guess - (len(board) // 2), " more guesses than thebest possible")
##########################################################################################

#
name = " __" + "welcome to my Concentration Game" + "__"

print(len(name) * "*" + "**")
print("  " + len(name) * "  ")
print("*" + len(name) * " " + "*")
print(" " + len(name) * " " + " ")
print("*" + name + "*")
print(" " + len(name) * " " + " ")
print("*" + len(name) * " " + "*")
print(len(name) * "*" + "**")

print("would you like (enter 1 or 2 to indicate choices):")
choice = input(
    " Enter \n (1) me to create a rigorous deck of cards for you \n (2) or, would you like to read a deck form a file?")
while choice != "1" and choice != "2":
    print(str(choice) + " " + "is not an existing option, please choose 1 or 2")
    choice = input(
        " Enter \n1 for me to create a rigorous deck of cards for you \n2 or, would you like to read a deck form a file?")
if choice == "1":
    print("You have chosen a rigorous deck generated for you")
    print("                                                 ")
    print("How many cards do you want to play with")
    cardnumber = int(input("enter a even number between 0 and 52:"))
    while cardnumber % 2 != 0 or cardnumber > 52 or cardnumber < 0:
        print("How many cards do you want to play with")
        cardnumber = int(input("enter a even number between 0 and 52:"))
    if cardnumber % 2 == 0:
        board = create_board(cardnumber)
        shuffle_deck(board)
        wait_for_player()
        play_game(board)

if choice == "2":
    print("You chose to load a deck of cards from a file")
    file = input("Enter the name of the file: ")
    file = file.strip()
    board = read_raw_board(file)
    board1 = clean_up_board(board)




    if is_rigorous(board1) == False:
        if len(board1) == 0:
            print("The resulting board does not have any cards and playing concentration game without cards is immpossible,\nGoodbye!!")
            exit()
        message = 'The deck is now playable. it is not rigorous and has ' + str(len(board1)) + "  cards."
        print(len(message) * "*" + "**")
        print("  " + len(message) * "  ")
        print("*" + len(message) * " " + "*")
        print(" " + len(message) * " " + " ")
        print("*" + message + "*")
        print(" " + len(message) * " " + " ")
        print("*" + len(message) * " " + "*")
        print(len(message) * "*" + "**")
        shuffle_deck(board1)
        wait_for_player()
        play_game(board1)
    if is_rigorous(board1) == True:
        if len(board1) == 0:
            print("The resulting board does not have any cards and playing concentration game without cards is immpossible,\nGoodbye!!")
            exit()
        message = 'The deck is now playable. it is  rigorous and has ' + str(len(board1)) + " cards."
        print(len(message) * "*" + "**")
        print("  " + len(message) * "  ")
        print("*" + len(message) * " " + "*")
        print(" " + len(message) * " " + " ")
        print("*" + message + "*")
        print(" " + len(message) * " " + " ")
        print("*" + len(message) * " " + "*")
        print(len(message) * "*" + "**")
        shuffle_deck(board1)
        wait_for_player()
        play_game(board1)




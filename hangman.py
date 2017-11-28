#Hangman
#Dashiona T.

def header():
    print(" .----------------. .----------------. .-----------------..----------------. .----------------. .----------------. .-----------------..----------------. ")
    print("| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |")
    print("| |  ____  ____  | | |      __      | | | ____  _____  | | |    ______    | | | ____    ____ | | |      __      | | | ____  _____  | | |              | |")
    print("| | |_   ||   _| | | |     /  \     | | ||_   \|_   _| | | |  .' ___  |   | | ||_   \  /   _|| | |     /  \     | | ||_   \|_   _| | | |      _       | |")
    print("| |   | |__| |   | | |    / /\ \    | | |  |   \ | |   | | | / .'   \_|   | | |  |   \/   |  | | |    / /\ \    | | |  |   \ | |   | | |     | |      | |")
    print("| |   |  __  |   | | |   / ____ \   | | |  | |\ \| |   | | | | |    ____  | | |  | |\  /| |  | | |   / ____ \   | | |  | |\ \| |   | | |     | |      | |")
    print("| |  _| |  | |_  | | | _/ /    \ \_ | | | _| |_\   |_  | | | \ `.___]  _| | | | _| |_\/_| |_ | | | _/ /    \ \_ | | | _| |_\   |_  | | |     | |      | |")
    print("| | |____||____| | | ||____|  |____|| | ||_____|\____| | | |  `._____.'   | | ||_____||_____|| | ||____|  |____|| | ||_____|\____| | | |     |_|      | |")
    print("| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |     (_)      | |")
    print("| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |")
    print(" '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' ")

    
def show_credits():
    print("  _______ _     _        _____                       __          __        ")
    print(" |__   __| |   (_)      / ____|                      \ \        / /        ")
    print("    | |  | |__  _ ___  | |  __  __ _ _ __ ___   ___   \ \  /\  / /_ _ ___  ")
    print("    | |  | '_ \| / __| | | |_ |/ _` | '_ ` _ \ / _ \   \ \/  \/ / _` / __| ")
    print("    | |  | | | | \__ \ | |__| | (_| | | | | | |  __/    \  /\  / (_| \__ \ ")
    print("    |_|  |_| |_|_|___/  \_____|\__,_|_| |_| |_|\___|     \/  \/ \__,_|___/ ")
    print("   _____                _           _   ____          _____        _       ")
    print("  / ____|              | |         | | |  _ \        |  __ \      (_)      ")
    print(" | |     _ __ ___  __ _| |_ ___  __| | | |_) |_   _  | |  | | __ _ _       ")
    print(" | |    | '__/ _ \/ _` | __/ _ \/ _` | |  _ <| | | | | |  | |/ _` | |      ")
    print(" | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| | | |__| | (_| | |      ")
    print("  \_____|_|  \___|\__,_|\__\___|\__,_| |____/ \__, | |_____/ \__,_|_|      ")
    print("                                               __/ |                       ")
    print("                                              |___/                        ")

def get_name():
    print("What is your name?")
    name = input()
    print("It is nice to meet you, " + name + ".")
    return name
     
def get_puzzle():
    return "puppies"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(name):
    letter = input("Guess a letter " + name + ": ")
    return letter

def display_board(solved):
    print(solved)

def show_result(strikes, limit):

    if strikes == limit:
        print ("You lose " + name + "!")
        result = 1
        gameover = 1

    else:
        print("You Win " + name + "!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision= decision.lower()
        
        print("")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    puzzle = get_puzzle()

    guesses = ""
    solved = "-" * len(puzzle)

    strikes = 0
    limit = 6
    result = 0
    gameover = 0
    
    display_board(solved)
    
    while solved != puzzle:
        letter = get_guess(name)

        if letter not in puzzle:
            strikes += 1
            if strikes == limit:
                return print ("You ran out of tries... You lose " + name + "!")

            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(0,6)

header()
    
name = get_name()
playing = True

while playing:
    play(name)
    playing = play_again()

show_credits()

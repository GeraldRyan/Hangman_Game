#!/usr/bin/python3

# AUTHORS: Michał Kobiec & Tomasz M. Krystyan

import random
import time

capitals = ["Tirana","Andorra","Yerevan","Vienna","Minsk","Brussels","Sarajevo","Sofia","Zagreb","Nicosia","Prague",
"Copenhagen","Tallinn","Helsinki","Paris","Tbilisi","Berlin","Athens","Budapest","Reykjavik","Dublin","Riga","Vaduz",
"Vilnius","Luxembourg","Skopje","Valletta","Chisinau","Monaco","Podgorica","Amsterdam","Oslo","Warsaw","Lisbon",
"Bucharest","Moscow","San Marino","Belgrade","Bratislava","Ljubljana","Madrid","Stockholm","Bern","Ankara"]

# Pick (randomly) one city from the list of contained in script European capitals.
chosen_capital = random.choice(capitals)

# List of letters contained in current randomly picked word (European capital).
letters = []

# Replacing randomly picked capital by dashes, which quantity is according to the lenght of city name.
for x in range(len(chosen_capital)):    # Variable "x" is used, only in this loop, to symbolise letters in city name. 
    if chosen_capital[x] != " ":
        letters.append("_")
    else:
        letters.append(" ")             # When city name is two word (e.g. "San Marino") ==> replace the whitespace to blank, instead of dash. 

# Simple registry, that count and print out user's failed attempts.
failed_attempts = []

# Number of total attempts, before the game is over.
life = 5

# Number of player successfull attempts (default set = 0).
guess_count = 0

def intro():
    print(" _                                             ")
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/                       ")

def hangman(life):
    """Prints different hangman pictures based on the current "life" status."""

    if life == 5:
        print(" _________ ")
        print(" |/        ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|___      ")

    elif life == 4:
        print(" _________ ")
        print(" |/      | ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|___      ")

    elif life == 3:
        print(" _________ ")
        print(" |/      | ")
        print(" |      (_)")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|___      ")

    elif life == 2:
        print(" _________ ")
        print(" |/      | ")
        print(" |      (_)")
        print(" |      \|/")
        print(" |         ")
        print(" |         ")
        print(" |         ")
        print("_|___      ")

    elif life == 1:
        print(" _________ ")
        print(" |/      | ")
        print(" |      (_)")
        print(" |      \|/")
        print(" |       | ")
        print(" |         ")
        print(" |         ")
        print("_|___      ")

    elif life <= 0:
        print(" _________ ")
        print(" |/      | ")
        print(" |      (_)")
        print(" |      \|/")
        print(" |       | ")
        print(" |      / \\")
        print(" |         ")
        print("_|___      ")

        print("The secret capital was {}, fool!".format(chosen_capital))

        time.sleep(2.5)

        print("\n\033[91m┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀┼┼")
        print("┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼┼┼")
        print("┼┼██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀┼┼")
        print("┼┼██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼┼┼")
        print("┼┼███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼┼┼")
        print("┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼┼┼")
        print("┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼┼┼")
        print("┼┼██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼┼┼")
        print("┼┼███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼┼┼")
        print("┼┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼┼┼\x1b[0m")


        start_again('')

def start_again(enter):
    """Resetting the global values."""
    global life
    global chosen_capital
    global letters

    once_again = input("{}Would you like to start again? (""\"""Yes""\""" to continue): ".format(enter))
            
    if once_again.lower() == "yes":     # Be insensitive to the lower- or uppercase of letters.
        life = 5
        chosen_capital = random.choice(capitals)
        letters = []
        for x in range(len(chosen_capital)):
            if chosen_capital[x] != " ":
                letters.append("_")
            else:
                letters.append(" ")
    else:
        exit()

def win():
    elapsed_time = time.time() - start_time
    
    print("\nThe European capital is (in English):"," ".join(letters))

    print("\nYou guessed after: {} tries. It took you {} seconds. {}".format(guess_count,round(elapsed_time,2)))
        
    time.sleep(4)

    print("\n             *     ,MMM8&&&.            *      ")
    print("                  MMMM88&&&&&    .             ")
    print("                 MMMM88&&&&&&&                 ")
    print("     *           MMM88&&&&&&&&                 ")
    print("                 MMM88&&&&&&&&                 ")
    print("                 'MMM88&&&&&&'                 ")
    print("                   'MMM8&&&'      *      _     ")
    print("          |\___/|                      \\\\    ")
    print("         =) ^Y^ (=   |\_/|             ||  '   ")
    print("          \  ^  /    )a a '._.------.  //      ")
    print("           )===(    =\T_= /    ~  ~  \//       ")
    print("          /     \     ` `\   ~   / ~  /        ")
    print("          |     |         |~   \ |  ~/         ")
    print("         /| | | |\         \  ~/- \ ~\         ")
    print("         \| | |_|/|        || |  // /`         ")
    print("  _/\_/\_/'_/\ \_/'\_/'\_/((_/'((/'\\/'\_/\_/\_")
    print("  |  |  |   | \_)   |   |   |   |   |   |  |  |")    # Below there is text "Congrats..." typed as colour (red), so there's no need to be worry about.
    print("  |  |  | \033[91mC\x1b[0m | \033[91mO\x1b[0m | \033[91mN\x1b[0m | \033[91mG\x1b[0m | \033[91mR\x1b[0m | \033[91mA\x1b[0m | \033[91mT\x1b[0m | \033[91mS\x1b[0m |  |  |")
    print("  |  |  |   |   |   |   |   |   |   |   |  |  |")
    print("  |  |  | \033[91mY\x1b[0m | \033[91mO\x1b[0m | \033[91mU\x1b[0m |   | \033[91mW\x1b[0m | \033[91mO\x1b[0m | \033[91mN\x1b[0m | \033[91m!\x1b[0m |  |  |")
    print("  |  |  |   |   |   |   |   |   |   |   |  |  |")
 
    start_again('\n')

intro()                     # Displays game welcome logo at the beginning.

start_time = time.time()    # Remember the actual time (hour and minutes) to estimate (later) the start time.

# The body of the script.
while True:
    ### DEBUG MODE ### print(chosen_capital)
    print("\nLifes left:", life)
    if "_" not in letters:  # The game was over when there are no "_" sign left.
        win()

    if failed_attempts:
        print("\nYou already tried:",", ".join(failed_attempts))  # Print remembered incorrect user attempts (despite of picked quessing method).

    print("\nThe European capital is (in English):", " ".join(letters))
    hangman(life)
    
    # Two methods of quessing a hidden city name: by word or by a letter.
    pick_method = input("\nWould you like to guess whole WORD or by a LETTER? (Type ""\"""W""\""" or ""\"""L""\"""): ")
    guess_count += 1
        
    if pick_method.lower() == "w":
        word_choice = input("\nGuess by a word: ")
        
        # Conditions of "word method".
        if word_choice.lower() == chosen_capital.lower():   # Be insensitive to the size of (user) input and (encoded in the script) output letters.
            for x in range(len(chosen_capital)):            # Variable "x" is used, only in this loop, to symbolise letters in the city name.
                letters[x] = chosen_capital[x].upper()              # Quantity of "letters" are exactly the same, as in the current randomly picked city name.
        else:
            failed_attempts.append(word_choice)             
            life -= 2                                       # Punish the player by taking him/her 1 point of life...
            hangman(life)                                   # ... and display the current "hangman" graphic status.
    
    # Conditions of "letter method".
    elif pick_method.lower() == "l":

        letter_choice = input("\nGuess by a letter: ")
        while len(letter_choice) != 1:                      # Allow user to input only one letter in this method. 
            print("\nPlease type one letter only!")
            letter_choice = input("\nGuess a letter: ")

        if letter_choice.lower() in chosen_capital.lower():
            for x in range(len(chosen_capital)):
                if chosen_capital[x].lower() == letter_choice.lower():  # Independently of letters size, match the user input letter (if it is contained in) to the hidden city name.
                    letters[x] = chosen_capital[x].upper()              # Change the output to uppercase letters.
        else:
            failed_attempts.append(letter_choice)
            life -= 1
            hangman(life)

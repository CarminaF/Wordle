import random
from colors import colors # colors.py imports colored module
from word_bank import word_bank
from scoreboard import init_scoreboard
from input import get_valid_input
from keyboard import color_in_keyboard, display_keyboard, reset_keyboard
from print import print_title, print_you_won, print_you_lose, print_word_to_guess

####### PRINT_MARGIN FUNCTION #########
# - Prints spaces to center grid
def print_margin():
    print("               ", end="")

####### FORMAT_STRING FUNCTION #########
# - gets passed a color list from "check_guess" function
# - checks the same index of color list and string
#       - if it is 'G' then turn background to green
#       - if 'Y' then turn background to yellow
# - also adds pipe "|" and spaces between letters
def format_string(string, color):
    colored_string = "|"
    for i in range(len(string)):
        if color[i] == 'G':
            colored_string += f" {colors['green_bg']}{string[i].upper()}{colors['reset']} |"
        elif color[i] == 'Y':
            colored_string += f" {colors['yellow_bg']}{string[i].upper()}{colors['reset']} |"
        else:
            colored_string += f" {colors['grey_bg']}{string[i].upper()}{colors['reset']} |"
    return colored_string

####### CHECK_GUESS FUNCTION #########
# - first checks if each letter is in the correct position
# - then checks if correct letter in the wrong position 
# - "found_flag" and breaking out of j loop ensures there is only one letter in the user's string
#    highlighted per occurrence in the word_to_guess even if there are more occurrences in the user's guess
def check_guess(string, word_to_guess):
    color = ['-'] * 5
    found_flag = [False] * 5
    for i in range(len(string)):
        if string[i] == word_to_guess[i]:
            color[i] = 'G'
            color_in_keyboard(string[i].upper(), 'G')
            found_flag[i] = True
    
    for i in range(len(string)):
        if color[i] == '-':
            for j in range(len(string)):
                if string[i] == word_to_guess[j] and not found_flag[j]:
                    color[i] = 'Y'
                    color_in_keyboard(string[i].upper(), 'Y')
                    found_flag[j] = True
                    break
            if color[i] == '-':
                color_in_keyboard(string[i].upper(), 'B')
    
    # for i in range(len(string)):
    #     if color[i] == '-' and not found_flag[j]:
    #         color_in_keyboard(string[i].upper(), 'B')
                    
    return format_string(string, color)

####### PRINT_LINE FUNCTION #########
# - Prints horizontal lines of the grid
def print_line():
    print_margin()
    print("+---+---+---+---+---+")



####### PRINT_GUESS FUNCTION #########
# - Prints with user's guesses
# - Then prints blank squares for remaining guesses
def print_grid(guesses, word_to_guess):
    grid = []
    for guess in guesses:
        grid.append(guess)
    for guess in guesses:
        print_line()
        print_margin()
        print(check_guess(guess, word_to_guess)) 
    for i in range(6 - len(guesses)):
        print_line()
        print("               |   |   |   |   |   |")
    print_line()


def main():
    init_scoreboard()

    guess_remaining = 6
    guess_count = 0
    guesses = []
    word_to_guess = random.choice(word_bank).upper()

    continue_game = True
    while continue_game:
        if guess_remaining == 6:
            print_title()
        
        print_grid(guesses, word_to_guess)
        display_keyboard()
        user_input = get_valid_input()
        
        guesses.append(user_input)
        guess_count += 1
        guess_remaining -= 1
        
        if user_input == "QUIT":
            continue_game = False
            break
        elif user_input == word_to_guess or guess_remaining == 0:
            print_grid(guesses, word_to_guess)
            display_keyboard()
            print_word_to_guess(word_to_guess)
            if user_input == word_to_guess:
                print_you_won()    
            elif guess_remaining == 0:
                print_you_lose()
            continue_game = get_valid_input("ask_to_play_again")
            if continue_game:
                guess_remaining = 6
                guess_count = 0
                guesses = []
                word_to_guess = random.choice(word_bank).upper()
                reset_keyboard()
            else:
                break
    print("Thank you for playing, see you soon!")

if __name__ == "__main__":
    main()
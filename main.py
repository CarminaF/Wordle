import random
from colors import COLORS # colors.py imports colored module
from word_bank import WORD_BANK
from scoreboard import init_scoreboard, update_score
from input import get_valid_input
from timekeeper import get_start_time, get_game_duration
from keyboard import color_in_keyboard, display_keyboard, reset_keyboard
from print import print_title, print_you_won, print_you_lose 
from print import print_word_to_guess, print_thank_you

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
def format_guess(guess, color):
    colored_guess = "|"
    for i in range(len(guess)):
        tile_color = " "
        reset = f"{COLORS['reset']} |"
        if color[i] == 'G':
            tile_color = f" {COLORS['green_bg']}{COLORS['white_font']}"
        elif color[i] == 'Y':
            tile_color = f" {COLORS['yellow_bg']}{COLORS['white_font']}"
        colored_guess += tile_color + f"{guess[i].upper()}" + reset
    return colored_guess

####### CHECK_GUESS FUNCTION #########
# - first checks if each letter is in the correct position
# - then checks if correct letter in the wrong position 
# - "found" and breaking out of j loop ensures there is only 
#    one letter in the user's string highlighted per 
#   occurrence in the word_to_guess even if there are 
#   more occurrences in the user's guess
def check_guess(user_guess, word_to_guess):
    color = ['-'] * 5
    found = [False] * 5
    for i in range(len(user_guess)):
        if user_guess[i] == word_to_guess[i]:
            color[i] = 'G'
            color_in_keyboard(user_guess[i].upper(), 'G')
            found[i] = True
            
    for i in range(len(user_guess)):
        if color[i] == '-':
            for j in range(len(word_to_guess)):
                if (user_guess[i] == word_to_guess[j] and
                    not found[j]):
                    color[i] = 'Y'
                    color_in_keyboard(user_guess[i].upper(), 'Y')
                    found[j] = True
                    break
            if color[i] == '-':
                # H for hidden
                color_in_keyboard(user_guess[i].upper(), 'H')              
    return color

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
        color = check_guess(guess, word_to_guess)
        formatted_guess = format_guess(guess, color)
        print(formatted_guess) 
    for i in range(6 - len(guesses)):
        print_line()
        print_margin()
        print("|   |   |   |   |   |")
    print_line()

def main():
    init_scoreboard()

    guess_remaining = 6
    guess_count = 0
    guesses = []
    word_to_guess = random.choice(WORD_BANK).upper()

    continue_game = True
    start_time = get_start_time()
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
        elif (user_input == word_to_guess or guess_remaining == 0):
            game_duration = get_game_duration(start_time)
            print_grid(guesses, word_to_guess)
            display_keyboard()
            print_word_to_guess(word_to_guess)
            if user_input == word_to_guess:
                print_you_won()
                update_score(game_duration, 
                            guess_count, 
                            word_to_guess)
            elif guess_remaining == 0:
                print_you_lose()
            continue_game = get_valid_input("ask_to_play_again")
            if continue_game:
                start_time = get_start_time()
                guess_remaining = 6
                guess_count = 0
                guesses = []
                word_to_guess = random.choice(WORD_BANK).upper()
                reset_keyboard()
            else:
                break
    print_thank_you()


if __name__ == "__main__":
    main()
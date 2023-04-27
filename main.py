from colors import COLORS
from input import get_valid_input
from print import print_title, print_you_won, print_you_lose, print_word_to_guess

####### FORMAT_STRING FUNCTION #########
# - gets passed a color list from "check_guess" function
# - checks the same index of color list and string
#   - if it is 'G' then turn background to green
#   - if 'Y' then turn background to yellow
# - also adds pipe "|" and spaces between letters
def format_string(string, color):
    colored_string = ''
    for i in range(len(string)):
        if color[i] == 'G':
            colored_string += f"| {COLORS['green_bg']}{string[i].upper()}{COLORS['reset']} "
        elif color[i] == 'Y':
            colored_string += f"| {COLORS['yellow_bg']}{string[i].upper()}{COLORS['reset']} "
        else:
            colored_string += f"| {COLORS['grey_bg']}{string[i].upper()}{COLORS['reset']} "
    return colored_string + "|"

####### CHECK_GUESS FUNCTION #########
# - first checks if each letter is in the correct position
# - then checks if correct letter in the wrong position 
# - "found_flag" and breaking out of j loop ensures there is only one letter in the user's string
#    highlighted per occurence in the word_to_guess even if there are more occurences in the user's guess
def check_guess(string, word_to_guess):
    color = ['-'] * 5
    found_flag = [False] * 5
    for i in range(len(string)):
        if string[i] == word_to_guess[i]:
            color[i] = 'G'
            found_flag[i] = True
    
    for i in range(len(string)):
        if color[i] == '-':
            for j in range(len(string)):
                if string[i] == word_to_guess[j] and not found_flag[j]:
                    color[i] = 'Y'
                    found_flag[j] = True
                    break
    return format_string(string, color)

####### PRINT_LINE FUNCTION #########
# - Prints horizontal lines of the grid
def print_line():
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
        print(check_guess(guess, word_to_guess)) 
    for i in range(6 - len(guesses)):
        print_line()
        print("|   |   |   |   |   |")
    print_line()

'''
def print_alphabet(guesses, word_to_guess):
'''
guess_remaining = 6
guess_count = 0
guesses = []
word_to_guess = "ABOVE"
print_title()
print_grid(guesses, word_to_guess)
while guess_remaining != 0:
    user_input = get_valid_input()
    if user_input == "QUIT":
        print("Thank you for playing, see you soon!")
        break
    guesses.append(user_input)
    print_grid(guesses, word_to_guess)
    guess_count += 1
    guess_remaining -= 1
    if user_input == word_to_guess:
        print_you_won()
        break
if guess_remaining == 0:
    print_word_to_guess(word_to_guess)
    print_you_lose()
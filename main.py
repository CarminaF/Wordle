from colored import fg, bg, attr

# Initializing global colors dictionary for better readability
COLORS = {
    "green_bg" : bg(28),
    "yellow_bg" : bg(94),
    "grey_bg" : bg(234),
    "white_font" : fg(15),
    "reset" : attr('reset')
}

# Gets the color formatting of the string depending on:
# - If correct letter is in the correct position, add green background
# - If correct letter is in the wrong position, add yellow background
# - If wrong letter, add grey background
# - Also adds pipe "|" and spaces between letters
# - Also typecasts character to a string then transforms it to uppercase
# - Return value is a concatenation of the formatted letters in the string
# Maybe need to refactor by splitting logic and formatting
def get_colored_string(string, word_to_guess):
    colored_string = ''
    for i in range(len(string)):
        if string[i] == word_to_guess[i]:
            colored_string += f"| {COLORS['green_bg']}{str(string[i]).upper()}{COLORS['reset']} "
        elif string[i] in word_to_guess:
            colored_string += f"| {COLORS['yellow_bg']}{str(string[i]).upper()}{COLORS['reset']} "
        elif string[i] not in word_to_guess:
            colored_string += f"| {COLORS['grey_bg']}{str(string[i]).upper()}{COLORS['reset']} "
    return colored_string + "|"

def print_grid(guesses):
    grid = []
    for guess in guesses:
        grid.append(guess)
    for guess in guesses:
        print("+---+---+---+---+---+")
        print(get_colored_string(guess, word_to_guess)) 
    for i in range(6 - len(guesses)):
        print("+---+---+---+---+---+")
        print("|   |   |   |   |   |")
    print("+---+---+---+---+---+")
'''
def print_alphabet(guesses, word_to_guess):
'''
guesses = ["hello", "there", "maybe"]
word_to_guess = "above"
print_grid(guesses)
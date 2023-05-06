from colors import COLORS
KEYBOARD = (('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'), 
            ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ' '),
            (' ','Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', ' '))

# need to hard code this instead of using 
# keyboard_color = [['-'] * 10] * 3 
# as it results in duplication of colors in 
# the rows/first dimension of the array 
KEYBOARD_COLOR = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]


def get_keyboard_index(letter):
    index = ()
    for row in range(len(KEYBOARD)):
        try:
            index = (row, KEYBOARD[row].index(letter))
        except ValueError:
            continue
    return index

def print_keyboard_margin():
    print("     ", end="")
    
def display_keyboard():
    print_keyboard_margin()
    reset = f"{COLORS['reset']} "
    for row in range(len(KEYBOARD)):
        for letter in KEYBOARD[row]:
            print("+---", end="") 
        print("+")
        print_keyboard_margin()
        for letter in range(len(KEYBOARD[row])):
            color = "| "
            if KEYBOARD_COLOR[row][letter] == 'G':
                color = f"| {COLORS['green_bg']}{COLORS['white_font']}"
            elif KEYBOARD_COLOR[row][letter] == 'Y':
                color = f"| {COLORS['yellow_bg']}{COLORS['white_font']}"
            elif KEYBOARD_COLOR[row][letter] == 'H':
                color = f"| {COLORS['hidden']}"
            print(color + f"{KEYBOARD[row][letter]}" + reset, end="")
        print("|")
        print_keyboard_margin()
    # print last line of keyboard
    for letter in KEYBOARD[0]:
        print("+---", end="") 
    print("+")

####### COLOR_IN_KEYBOARD FUNCTION #########
# - populates keyboard 2D list above
# - if keyboard colour is already green, it will stay green in 
#   consequent guesses
# - if keyboard is already populated as yellow, it can only be 
#   overwritten by green colors
def color_in_keyboard(letter, color):
    index = get_keyboard_index(letter)
    if KEYBOARD_COLOR[index[0]][index[1]] != 'G':
        if ((KEYBOARD_COLOR[index[0]][index[1]] == 'Y' 
             and color == 'G') or 
             (KEYBOARD_COLOR[index[0]][index[1]] == '-')):
            KEYBOARD_COLOR[index[0]][index[1]] = color

def reset_keyboard():
    for row in range(len(KEYBOARD_COLOR)):
        for letter in range(len(KEYBOARD_COLOR[row])):
            KEYBOARD_COLOR[row][letter] = '-'


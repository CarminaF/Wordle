from pprint import pprint
from colors import colors
keyboard = (('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'), 
            ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ' '),
            (' ','Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', ' '))

# need to hard code this instead of using keyboard_color = [['-'] * 10] * 3 
# as it results in duplication of colors in the rows/first dimension of the array 
keyboard_color = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]


def get_keyboard_index(letter):
    index = ()
    for row in range(len(keyboard)):
        try:
            index = (row, keyboard[row].index(letter))
        except ValueError:
            continue
    return index

def print_keyboard_margin():
    print("     ", end="")
    
def display_keyboard():
    print_keyboard_margin()
    for row in range(len(keyboard)):
        for letter in keyboard[row]:
            print("+---", end="") 
        print("+")
        print_keyboard_margin()
        for letter in range(len(keyboard[row])):
            if keyboard_color[row][letter] == 'G':
                print(f"| {colors['green_bg']}{keyboard[row][letter]}{colors['reset']} ", end="")
            elif keyboard_color[row][letter] == 'Y':
                print(f"| {colors['yellow_bg']}{keyboard[row][letter]}{colors['reset']} ", end="")
            else:
                print(f"| {colors['grey_bg']}{keyboard[row][letter]}{colors['reset']} ", end="")
        print("|")
        print_keyboard_margin()
    # print last line of keyboard
    for letter in keyboard[0]:
        print("+---", end="") 
    print("+")

def color_in_keyboard(letter, color):
    index = get_keyboard_index(letter)
    if keyboard_color[index[0]][index[1]] != 'G':
        if keyboard_color[index[0]][index[1]] == '-' or keyboard_color[index[0]][index[1]] == 'Y':
            keyboard_color[index[0]][index[1]] = color


from colors import COLORS
def print_instructions():
	print(f'''
{COLORS['blue_font']}
******************************************************************************************

INSTRUCTIONS:
1.	You have six tries to guess the five-letter Wordle of the day.

2.	Type in your guess and submit your word by hitting the “enter” key.

3.	The color of the tiles will change after you submit your word. A yellow tile indicates 
	that you picked the right letter but it’s in the wrong spot. The green tile indicates 
	that you picked the right letter in the correct spot. The gray tile indicates that 
	the letter you picked is not included in the word at all.

4.	Continue until you solve the Wordle or run out of guesses. Good luck!

5. Type "quit" and press "enter" on your keyboard to exit the game

******************************************************************************************
{COLORS['reset']}
''')

def print_title():
	print(f'''{COLORS['green_font']}
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
{COLORS['reset']}
{COLORS['yellow_font']}
**********    Guess the 5-letter word!   ********** 
	
	- "INSTRUCTIONS" for how to play
	- "QUIT" to exit 
{COLORS['reset']}                    
''')

def print_you_lose():
	print(f'''{COLORS['red_font']}
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████  ▐██▌ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀  ▐██▌ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███    ▐██▌ 
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄  ▓██▒ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒ ▒▄▄  
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░       ░ 
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░ ░    
 ░ ░
 {COLORS['reset']}                                                                
''')

def print_you_won():
	print(f'''{COLORS['green_font']}
/$$     /$$/$$$$$$  /$$   /$$       /$$      /$$  /$$$$$$  /$$   /$$ /$$
|  $$   /$$/$$__  $$| $$  | $$      | $$  /$ | $$ /$$__  $$| $$$ | $$| $$
 \  $$ /$$/ $$  \ $$| $$  | $$      | $$ /$$$| $$| $$  \ $$| $$$$| $$| $$
  \  $$$$/| $$  | $$| $$  | $$      | $$/$$ $$ $$| $$  | $$| $$ $$ $$| $$
   \  $$/ | $$  | $$| $$  | $$      | $$$$_  $$$$| $$  | $$| $$  $$$$|__/
    | $$  | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$\  $$$    
    | $$  |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$ \  $$ /$$
    |__/   \______/  \______/       |__/     \__/ \______/ |__/  \__/|__/
{COLORS['reset']}                                                   
''')

def print_word_to_guess(word_to_guess):
	print(f'''{COLORS['yellow_font']}
**********************************************************
		The word was : {word_to_guess}
**********************************************************
	''')
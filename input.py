from colors import COLORS
from word_bank import WORD_BANK
from valid_words import VALID_WORDS
from print import print_instructions
from scoreboard import print_scoreboard

MARGIN = '           '

####### GET_VALID_INPUT FUNCTION #########
# - Keeps asking user for input if
#		- The input is not "instruction" or "quit" or
#		- word does not contain only alphabets
#		- word is not 5 letters
# - returns
def get_valid_input(purpose=""):
	while True:
		color = f"{MARGIN}{COLORS['red_font']}"
		reset = f"{COLORS['reset']}"

		if purpose == "ask_to_play_again":
			question = f"{MARGIN}Would you like to play again? (Y/N): "
			user_input = input(question)
		else:
			question = f"{MARGIN}Enter a 5-letter word: "
			user_input = input(question)
		print("\n")
		user_input = user_input.strip().upper()
		if not user_input.isalpha():
			message = "ERROR: Please enter alphabets only"
			print(color + message + reset)
		elif user_input == 'INSTRUCTIONS':
			print_instructions()
		elif user_input == 'SCOREBOARD':
			print_scoreboard()
		elif user_input.upper() == "QUIT":
			return user_input
		elif purpose == "ask_to_play_again":
			if user_input == "Y" or user_input == "YES":
				return True
			elif user_input == "N" or user_input == "NO":
				return False
			else:
				message = "ERROR: You must enter Y or N"
				print(color + message + reset)
		elif len(user_input) != 5:
			message = "ERROR: You must enter 5 letters"
			print(color + message + reset)
		elif (user_input.lower() not in VALID_WORDS and 
			user_input.lower() not in WORD_BANK):
			message = "ERROR: Not a valid word in the word bank"
			print(color + message + reset)
		else:
			return user_input


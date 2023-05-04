from colors import colors
from word_bank import word_bank
from valid_words import valid_words
from print import print_instructions

margin = '           '
####### GET_VALID_INPUT FUNCTION #########
# - Keeps asking user for input if
#		- The input is not "instruction" or "quit" or
#		- word does not contain only alphabets
#		- word is not 5 letters
# - returns
def get_valid_input(purpose=""):
	while(True):
		if purpose == "ask_to_play_again":
			user_input = input(f"{margin}Would you like to play again? (Y/N): ")
		else:
			user_input = input(f"{margin}Enter a 5-letter word: ")
		print("\n")
		user_input = user_input.strip().upper()
		if not user_input.isalpha():
			print(f"{margin}{colors['red_font']}ERROR: Please enter alphabets only{colors['reset']}")
		elif user_input == 'INSTRUCTIONS':
			print_instructions()
		elif user_input.upper() == "QUIT":
			return user_input
		elif purpose == "ask_to_play_again":
			if user_input == "Y":
				return True
			elif user_input == "N":
				return False
			else:
				print(f"{margin}{colors['red_font']}ERROR: You must enter Y or N{colors['reset']}")
		elif len(user_input) != 5:
			print(f"{margin}{colors['red_font']}ERROR: You must enter 5 letters{colors['reset']}")
		elif user_input.lower() not in valid_words and user_input.lower() not in word_bank:
			print(f"{margin}{colors['red_font']}ERROR: Not a valid word in the word bank{colors['reset']}")
		else:
			return user_input


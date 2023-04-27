from colors import COLORS
from print import print_instructions

####### GET_VALID_INPUT FUNCTION #########
# - Keeps asking user for input if
#		- The input is not "instruction" or "quit" or
#		- word does not contain only alphabets
#		- word is not 5 letters
# - retyrns
def get_valid_input():
	while(True):
		user_input = input("Enter a 5-letter word: ")
		user_input = user_input.strip().upper()
		if not user_input.isalpha():
			print(f"{COLORS['red_font']}ERROR: Please enter alphabets only{COLORS['reset']}")
		elif user_input == 'INSTRUCTIONS':
			print_instructions()
		elif user_input.upper() == "QUIT":
			return user_input
		elif len(user_input) != 5:
			print(f"{COLORS['red_font']}ERROR: You must enter 5 letters{COLORS['reset']}")
		else:
			return user_input
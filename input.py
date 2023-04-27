from colors import COLORS
from print import print_instructions

def get_valid_input():
	while(True):
		user_input = input("Enter a 5-letter word: ")
		if not user_input.strip().isalpha():
			print(f"{COLORS['red_font']}ERROR: Please enter alphabets only{COLORS['reset']}")
		elif user_input.strip().upper() == 'INSTRUCTIONS':
			print_instructions()
		elif user_input.strip().upper() == "QUIT":
			return user_input.strip().upper()
		elif len(user_input.strip()) != 5:
			print(f"{COLORS['red_font']}ERROR: You must enter 5 letters{COLORS['reset']}")
		else:
			return user_input.strip().upper()
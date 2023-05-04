import csv
from colors import colors

file_name = "scoreboard.csv"

def init_scoreboard():
	try:
		scoreboard_file = open(file_name, "r", newline='') #In Windows, new lines are created automatically. 
		scoreboard_file.close()
	except FileNotFoundError:
		scoreboard_file = open(file_name, "w")
		scoreboard_file.write("Position,Name,Guesses,Time\n")
		scoreboard_file.close()

def update_scoreboard(duration, guess_count):
	name = input("Enter your name for the scoreboard: ")
	print(f"Name: {name}, Guesses: {guess_count}, Time: {duration}")

def print_scoreboard():
	print("Scoreboard")
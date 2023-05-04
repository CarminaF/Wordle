import csv

file_name = "scoreboard.csv"

def init_scoreboard():
	try:
		highscore_file = open(file_name, "r", newline='') #In Windows, new lines are created automatically. 
		highscore_file.close()
	except FileNotFoundError:
		highscore_file = open(file_name, "w")
		highscore_file.write("Position,Name,Guesses,Time\n")
		highscore_file.close()


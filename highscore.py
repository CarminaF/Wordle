import csv

file_name = "highscore.csv"

try:
	highscore_file = open(file_name, "r")
	highscore_file.close()
except FileNotFoundError:
	highscore_file = open(file_name, "w")
	highscore_file.write("Name,Guesses,Time\n")
	highscore_file.close()

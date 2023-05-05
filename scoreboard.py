import csv
import datetime
from colors import COLORS

SCORE_FILE_PATH = "scoreboard.csv"
COLUMN_NAMES = ["Position", "Name", "Attempts", "Duration", "Word"]

def init_scoreboard():
    try:
        scoreboard_file = open(SCORE_FILE_PATH, "r", newline="")
        scoreboard_file.close()
    except FileNotFoundError:
        with open(SCORE_FILE_PATH, "w", newline="") as file:
            writer = csv.DictWriter(file, COLUMN_NAMES)
            writer.writeheader()

def write_to_score_file(scoreboard):
    with open(SCORE_FILE_PATH, "w", newline="") as file:
        writer = csv.DictWriter(file, COLUMN_NAMES)
        writer.writeheader()
        for row in scoreboard:
            writer.writerow(row)


def get_keys(row):
    import datetime

def get_keys(row):
    attempts = int(row["Attempts"])
    duration = datetime.datetime.strptime(row["Duration"], "%H:%M:%S.%f")
    duration_td = datetime.timedelta(hours=duration.hour,
                                    minutes=duration.minute, 
                                    seconds=duration.second,
                                    microseconds=duration.microsecond)
    return attempts, duration_td


def sort_scoreboard(scoreboard):
    sorted_scoreboard = sorted(scoreboard, key=get_keys)
    for i, row in enumerate(sorted_scoreboard):
        row["Position"] = i + 1
    return sorted_scoreboard
    

def add_to_scoreboard(name, guess_count, duration, word):
    scoreboard = []
    with open(SCORE_FILE_PATH, "r+", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            scoreboard.append(row)
        new_row = {"Name": name, "Attempts": guess_count,
            "Duration": duration, "Word": word}
        scoreboard.append(new_row)
    return scoreboard

def adjust_spaces(string, field):
    match field:
        case "position":
            max_len = 10
        case "name":
            max_len = 16
            # Truncate name len to max_len so field not too wide
            string = string[:max_len]
        case "attempts":
            max_len = 10
        case "duration":
            max_len = 16
        case "word":
            max_len = 8
    string_len = len(string)
    number_of_spaces = int((max_len - string_len) / 2)
    margin = " " * number_of_spaces
    formatted_string = margin + string + margin
    if string_len % 2 == 1:
        formatted_string += " "
    return formatted_string

def print_scoreboard():
    with open(SCORE_FILE_PATH, "r") as file:
        reader = csv.DictReader(file, COLUMN_NAMES)
        display = f'''{COLORS["blue_font"]}
        ╔═╗╔═╗╔═╗╦═╗╔═╗╔╗ ╔═╗╔═╗╦═╗╔╦╗
        ╚═╗║  ║ ║╠╦╝║╣ ╠╩╗║ ║╠═╣╠╦╝ ║║
        ╚═╝╚═╝╚═╝╩╚═╚═╝╚═╝╚═╝╩ ╩╩╚══╩╝
'''
        for row in reader:
            display += f"|{adjust_spaces(row['Position'], 'position')}"
            display += f"|{adjust_spaces(row['Name'], 'name')}"
            display += f"|{adjust_spaces(row['Attempts'], 'attempts')}"
            display += f"|{adjust_spaces(row['Duration'], 'duration')}"
            display += f"|{adjust_spaces(row['Word'], 'word')}|\n"
        display += f"{COLORS['reset']}\n"
    print(display)

def update_score(duration, guess_count, word):
    name = input("		Enter your name for the scoreboard: ")
    updated_scoreboard = add_to_scoreboard(name.strip(), guess_count,
                         str(duration), word)
    sorted_scoreboard = sort_scoreboard(updated_scoreboard)
    write_to_score_file(sorted_scoreboard)
    print_scoreboard()


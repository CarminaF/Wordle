import datetime


# returns datetime object
def get_start_time():
    start_time = datetime.datetime.now()
    return start_time

def get_game_duration(start_time):
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    return duration


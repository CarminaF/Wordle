from main import check_guess, print_grid
from colors import COLORS


# def test_check_guess():
#     answer = f"| T "
#     answer += f"| {COLORS['yellow_bg']}H{COLORS['reset']} "
#     answer += f"| {COLORS['yellow_bg']}E{COLORS['reset']} "
#     answer += f"| R "
#     answer += f"| E |"
#     assert check_guess(user_guess="THERE", word_to_guess="HELLO") == answer
#     answer = f"| {COLORS['blue_font']}T{COLORS['reset']} "
#     answer += f"| {COLORS['yellow_bg']}R{COLORS['reset']} "
#     answer += f"| {COLORS['yellow_bg']}E{COLORS['reset']} "
#     answer += f"| {COLORS['green_bg']}E{COLORS['reset']} "
#     answer += f"| S |"
#     assert check_guess(user_guess="TREES", word_to_guess="HELLO") == answer
#     answer = f"| {COLORS['green_bg']}H{COLORS['reset']} "
#     answer += f"| {COLORS['green_bg']}E{COLORS['reset']} "
#     answer += f"| {COLORS['green_bg']}L{COLORS['reset']} "
#     answer += f"| {COLORS['green_bg']}L{COLORS['reset']} "
#     answer += f"| {COLORS['green_bg']}O{COLORS['reset']} |"
#     assert check_guess(user_guess="HELLO", word_to_guess="HELLO") == answer



def test_check_guess():
    test1 = ["-", "Y", "Y", "-", "-"]
    assert check_guess(user_guess="THERE", word_to_guess="HELLO") == test1
    test2 = ["G", "Y", "Y", "G", "-"]
    assert check_guess(user_guess="TREES", word_to_guess="THREE") == test2
    test3 = ["G", "G", "G", "G", "G"]
    assert check_guess(user_guess="HELLO", word_to_guess="HELLO") == test3
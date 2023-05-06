from main import check_guess
from colors import COLORS

def test_check_guess():
    test1 = ["-", "Y", "Y", "-", "-"]
    assert check_guess(user_guess="THERE", word_to_guess="HELLO") == test1
    test2 = ["G", "Y", "Y", "G", "-"]
    assert check_guess(user_guess="TREES", word_to_guess="THREE") == test2
    test3 = ["G", "G", "G", "G", "G"]
    assert check_guess(user_guess="HELLO", word_to_guess="HELLO") == test3
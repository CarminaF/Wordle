from keyboard import KEYBOARD, KEYBOARD_COLOR
from keyboard import get_keyboard_index

def test_get_keyboard_index():
    assert get_keyboard_index("Q") == (0, 0)
    assert get_keyboard_index("G") == (1, 4)
    assert get_keyboard_index("M") == (2, 7)

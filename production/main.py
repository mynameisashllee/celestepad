import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [
    board.D1,  # SW1 - up
    board.D2,  # SW2 - down
    board.D3,  # SW3 - left
    board.D4,  # SW4 - right
    board.D6,  # SW5 - z (climb)
    board.D7,  # SW6 - x (dash)
    board.D0,  # SW7 - c (jump)
]


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


keyboard.keymap = [
    [
        KC.UP,      # SW1
        KC.DOWN,    # SW2
        KC.LEFT,    # SW3
        KC.RIGHT,   # SW4
        KC.Z,       # SW5
        KC.X,       # SW6
        KC.C,       # SW7
    ]
]

if __name__ == '__main__':
    keyboard.go()

# My goal is to make the game tic-tac-toe scalable - without using hard code - so that you can change the parameters
# by changing the playing field.
#
# At the same time, I have immutable rules that the user cannot change, such as the name "X" and "O", and also that
# the number of cells is equal in width and height.
#
# It is also ideal to write the code typed so that it is easy to read and understand.
import os

demo_board = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
board_width = 3


def display_board(board, line_width):
    os.system('cls')

    current_line = "|"
    for index, item in enumerate(board):
        current_line += item + '|'
        current_item_number = index + 1

        if current_item_number % line_width == 0:
            print(current_line)
            current_line = "|"


display_board(demo_board, board_width)

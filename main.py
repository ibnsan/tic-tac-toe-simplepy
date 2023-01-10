# My goal is to make the game tic-tac-toe scalable - without using hard code - so that you can change the parameters
# by changing the playing field.
#
# At the same time, I have immutable rules that the user cannot change, such as the name "X" and "O", and also that
# the number of cells is equal in width and height.
#
# It is also ideal to write the code typed so that it is easy to read and understand.
import os

demo_board = ['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']


def get_board_width():
    """
    Asks the user for the width of the board in numbers and returns that width
    :return: Playing board width in numbers above 2
    """
    width = 0
    while not (isinstance(int(width), int) and int(width) > 2 and int(width) < 24):
        width = input(
            "Specify the length of the playing board (the length must be in numbers and greater than 2): ")

    return int(width)


board_width = get_board_width()


def create_board(board_width):
    """
    :param board_width: Playing board width in numbers
    :return: Playboard array where each cell corresponds to an index
    """
    board_size = board_width * board_width
    board = []
    for cell_number in range(board_size):
        board.append(str(cell_number))
    return board


def select_symbol():
    """
    :return: Selected user characters (x or y)
    """
    marker = ''
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1 - please choose you marker 'x or o': ").upper()

    if marker == "X":
        return ("x", "o")
    else:
        return ("o", "x")


player1_marker, player2_marker = select_symbol()

game_board = create_board(board_width)


def display_board(board, line_width):
    """
    :param board: An array of element values - the number of which is a multiple of line_width
    :param line_width: Board length horizontally and vertically
    :return: Board with separator | with the number of characters in width and height equal to line_width
    """
    os.system('cls')

    current_line = "|"
    final_board = ""
    for index, item in enumerate(board):
        current_line += item + '|'
        current_item_number = index + 1

        if current_item_number % line_width == 0:
            final_board += current_line + "\n"
            current_line = "|"

    return final_board


board = display_board(game_board, board_width)
print(board)

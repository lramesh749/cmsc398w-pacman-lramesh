from game_board import GameBoard

def test_board_dimensions():
    board = GameBoard(["###", "#.#", "###"])
    assert board.width == 3
    assert board.height == 3

from tic_tac_toe_classes import Board, Player, Ajudicator
from mock import patch
import pytest


@pytest.mark.parametrize('row_length, expected_board_positions', [
    (3, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]),
    (0, [])
])
def test_get_correct_board_positions_on_board(row_length, expected_board_positions):
    # when
    b = Board(row_length)

    # then
    assert b.board_positions == expected_board_positions



@pytest.mark.parametrize('row_length, player_symbol, board_positions, expected_board_positions', [
    (3, "X", [1, "X", 3, 4, 5, 6, 7, 8, "X"], [1, 8]),
    (2, "O", [1, 2, "O", 4], [2]),
    (0, "X", [], []),
    (4, "O", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [])
])
def test_get_player_positions_for_player(row_length, player_symbol, board_positions, expected_board_positions):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player = Player(player_symbol, board)

    # when
    result = sample_player.get_player_positions()

    # then
    assert result == expected_board_positions



@patch('tic_tac_toe_classes.Player.get_player_move')
@pytest.mark.parametrize('row_length, player_symbol, board_positions, expected_board_positions', [
    (3, "X", [1, "X", 3, 4, 5, 6, 7, 8, "X"], [" X ", "X", 3, 4, 5, 6, 7, 8, "X"]),
    (2, "O", [1, 2, "O", 4], [" X ", 2, "O", 4])
])
def test_player_move_when_have_player_move(get_player_move, row_length, player_symbol, board_positions, expected_board_positions):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player = Player(player_symbol, board)
    get_player_move.return_value = 1

    # when
    sample_player.player_move()

    # then
    assert board.board_positions == expected_board_positions



@patch('tic_tac_toe_classes.Player.get_player_move')
def test_player_move_when_have_player_move(get_player_move):
    # given
    board = Board(3)
    board.board_positions = [1, "X", 3, 4, 5, 6, 7, 8, "X"]
    expected_board_positions = [" X ", "X", 3, 4, 5, 6, 7, 8, "X"]
    sample_player = Player("X", board)
    get_player_move.return_value = 1

    # when
    sample_player.player_move()

    # then
    assert board.board_positions == expected_board_positions




@pytest.mark.parametrize('row_length, board_positions', [
    (3, ["X", "X", "O", "O", "X", "O", "O", "X", "X"]),
    (2, ["X", "O", "X", "O"]),
    (0, [])
])
def test_no_moves_remain_when_no_moves_remain(row_length, board_positions):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player1 = Player("X", board)
    sample_player2 = Player("O", board)
    ajud = Ajudicator(board, sample_player1, sample_player2)

    # when
    result = ajud.no_moves_remain()

    # then
    assert result



@pytest.mark.parametrize('row_length, board_positions', [
    (3, [1, "X", "O", "O", "X", "O", "O", "X", "X"]),
    (2, [1, 2, 3, 4]),
])
def test_no_moves_remain_when_moves_do_remain(row_length, board_positions):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player1 = Player("X", board)
    sample_player2 = Player("O", board)
    ajud = Ajudicator(board, sample_player1, sample_player2)

    # when
    result = ajud.no_moves_remain()

    # then
    assert not result



@pytest.mark.parametrize('row_length, board_positions', [
    (3, ["X", "X", "X", 4, 5, 6, 7, 8, 9]),
    (4, ["O", "X", "X", 4, 5, "O", "X", 8, 9, 10, "O", 12, "X", 14, 15, "O"]),
    (2, [1, "X", "X", "O"]),
])
def test_some_player_has_won_when_someone_has_won(row_length, board_positions):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player1 = Player("X", board)
    sample_player2 = Player("O", board)
    ajud = Ajudicator(board, sample_player1, sample_player2)

    # when
    result = ajud.some_player_has_won()

    # then
    assert result



@pytest.mark.parametrize('row_length, board_positions', [
    (3, ["X", 2, 3, 4, 5, 6, 7, 8, 9]),
    (4, ["O", "X", "X", 4, 5, "O", "X", 8, 9, 10, "O", 12, "X", 14, 15, 16]),
    (2, [1, "X", 3, "O"]),
])
def test_some_player_has_won_when_no_winner(row_length, board_positions):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player1 = Player("X", board)
    sample_player2 = Player("O", board)
    ajud = Ajudicator(board, sample_player1, sample_player2)

    # when
    result = ajud.some_player_has_won()

    # then
    assert not result



@pytest.mark.parametrize('row_length, player_positions', [
    (3, [0, 1, 2]),
    (4, [0, 5, 10, 15]),
    (2, [0, 2]),
])
def test_contains_winning_combination_when_contains_combination(row_length, player_positions):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.contains_winning_combination(player_positions)

    # then
    assert result



@pytest.mark.parametrize('row_length, player_positions', [
    (3, [1, 2]),
    (4, [0, 5, 10, 14]),
    (2, [2]),
])
def test_contains_winning_combination_when_contains_combination(row_length, player_positions):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.contains_winning_combination(player_positions)

    # then
    assert not result



@pytest.mark.parametrize('row_length, player_positions', [
    (3, [0, 1, 2]),
    (4, [4, 5, 6, 7]),
    (2, [2, 3]),
])
def test_contains_row_when_contains_row(row_length, player_positions):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.contains_row(player_positions)

    # then
    assert result



@pytest.mark.parametrize('row_length, player_positions', [
    (3, [0, 1]),
    (4, [0, 1, 4, 5, 8, 9, 12, 14]),
    (2, [0, 3]),
])
def test_contains_row_when_does_not_contain_row(row_length, player_positions):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.contains_row(player_positions)

    # then
    assert not result



@pytest.mark.parametrize('row_length, original_list, expected_sublists', [
    (3, [0, 1, 2, 3, 4, 5, 6, 7, 8], [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]),
    (2, [0, 1, 2, 3], [[0, 1], [1, 2], [2, 3]]),
])
def test_gets_all_sublists(row_length, original_list, expected_sublists):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    sublists = ajud.get_all_sublists(original_list, row_length)

    # then
    assert sublists == expected_sublists



@pytest.mark.parametrize('row_length, nums', [
    (3, [0, 1, 2]),
    (3, [3, 4, 5]),
    (2, [2, 3]),
    (4, [12, 13, 14, 15])
])
def test_is_a_row_when_is_row(row_length, nums):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.is_a_row(nums)

    # then
    assert result



@pytest.mark.parametrize('row_length, nums', [
    (3, [0, 1]),
    (3, [3, 4, 5, 6]),
    (2, [0, 3]),
    (4, [11, 12, 13, 14, 15])
])
def test_is_a_row_when_not_a_row(row_length, nums):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.is_a_row(nums)

    # then
    assert not result



@pytest.mark.parametrize('row_length, position', [
    (3, 3),
    (3, 0),
    (2, 2),
    (4, 12)
])
def test_is_start_of_row_when_start(row_length, position):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.is_start_of_row(position)

    # then
    assert result


@pytest.mark.parametrize('row_length, position', [
    (3, 1),
    (3, 2),
    (2, 1),
    (4, 11)
])
def test_is_start_of_row_when_not_start(row_length, position):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.is_start_of_row(position)

    # then
    assert not result



@pytest.mark.parametrize('row_length, player_positions', [
    (3, [1, 4, 7]),
    (3, [0, 3, 6]),
    (2, [0, 2]),
    (4, [3, 7, 11, 15])
])
def test_contains_column_when_contains_column(row_length, player_positions):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.contains_column(player_positions)

    # then
    assert result



@pytest.mark.parametrize('row_length, player_positions', [
    (3, [0, 4, 7]),
    (3, [0, 3]),
    (2, [0, 1]),
    (4, [3, 7, 11, 14]),
    (0, [])
])
def test_contains_column_when_no_column(row_length, player_positions):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    result = ajud.contains_column(player_positions)

    # then
    assert not result



@pytest.mark.parametrize('player_positions, values', [
    ([0, 1, 2, 3], [0, 1, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4]),
    ([1, 2, 6, 7, 8], [6, 7]),
])
def test_has_all_values_when_has_all(player_positions, values):
    # given
    ajud = Ajudicator(None)

    # when
    result = ajud.has_all_values(player_positions, values)

    # then
    assert result



@pytest.mark.parametrize('player_positions, values', [
    ([0, 1, 2], [0, 1, 2, 3]),
    ([2, 3, 4, 5], [1, 2, 3, 4]),
    ([1, 2, 7, 8], [6, 7, 8, 9]),
])
def test_has_all_values_when_has_does_not_have_all(player_positions, values):
    # given
    ajud = Ajudicator(None)

    # when
    result = ajud.has_all_values(player_positions, values)

    # then
    assert not result



@pytest.mark.parametrize("row_length, expected_sublists",[
    (3, [[0, 3, 6], [1, 4, 7], [2, 5, 8]]),
    (2, [[0, 2], [1, 3]]),
    (0, [])
])
def test_get_all_columns(row_length, expected_sublists):
    # given
    board = Board(row_length)
    ajud = Ajudicator(board)

    # when
    column_sublists = ajud.get_all_columns()

    # then
    assert column_sublists == expected_sublists



@pytest.mark.parametrize("row_length, board_positions, expected_winner", [
    (3, ["O", "X", 3, 4, "X", 6, 7, "X", "O"], "X"),
    (2, [1, "O", "O", "X"], "O"),
    (2, [1, "O", 3, "X"], False)
])
def test_find_which_player_has_won(row_length, board_positions, expected_winner):
    # given
    board = Board(row_length)
    board.board_positions = board_positions
    sample_player1 = Player("X", board)
    sample_player2 = Player("O", board)
    ajud = Ajudicator(board, sample_player1, sample_player2)

    # when
    winning_player = ajud.find_which_player_has_won()

    # then
    assert winning_player == expected_winner

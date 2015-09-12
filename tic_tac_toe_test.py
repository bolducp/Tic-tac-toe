from any_board_size_tic_tac_toe import get_board, player_move, player_has_won, contains_winning_combination, contains_row, get_all_sublists, is_a_row, is_start_of_row, contains_column, has_all_values, get_all_columns, is_start_of_column, contains_diagonal, get_left_corner_diagonal, get_right_corner_diagonal, no_moves_remain
from mock import patch

import pytest


@pytest.mark.parametrize('row_length, expected_board', [
    (2, [1, 2, 3, 4]),
    (4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]),
    (0, [])
])
def test_get_board(row_length, expected_board):
    # when
    board = get_board(row_length)

    # then
    assert board == expected_board


@patch('any_board_size_tic_tac_toe.get_player_move')
@pytest.mark.parametrize('board, user_symbol, expected_board', [
    ([1, 2, 3, 4], "X", [" X ", 2, 3, 4]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], "O", [" O ", 2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_player_move(get_player_move, board, user_symbol, expected_board):
    # given
    get_player_move.return_value = 1

    # when
    player_move(board, user_symbol)

    # then
    assert board == expected_board


def test_player_has_won_when_player_has_won():
    # given
    board = ["X", 2, 3, "X", 5, 6, "X", 8, 9]
    player_symbol = "X"
    row_length = 3

    # when
    result = player_has_won(board, player_symbol, row_length)

    # then
    assert result



def test_player_has_won_when_no_player_has_won():
    # given
    board = ["X", 2, 3, "O", "O", 6, "X", 8, 9]
    player_symbol = "X"
    row_length = 3

    # when
    result = player_has_won(board, player_symbol, row_length)

    # then
    assert not result



def test_contains_winning_combination_when_contains_winning_combination():
    # given
    player_positions = [0, 1, 2, 5, 9]
    row_length = 3

    # when
    result = contains_winning_combination(player_positions, row_length)

    # then
    assert result


def test_contains_winning_combination_when_no_combination_present():
    # given
    player_positions = [3, 4, 8]
    row_length = 3

    # when
    result = contains_winning_combination(player_positions, row_length)

    # then
    assert not result


def test_contains_row_when_player_positions_contains_row():
    # given
    player_positions = [6, 7, 8]
    row_length = 3

    # when
    result = contains_row(player_positions, row_length)

    # then
    assert result


def test_contains_row_when_player_positions_does_not_contain_row():
    # given
    player_positions = [0, 1, 9]
    row_length = 3

    # when
    result = contains_row(player_positions, row_length)

    # then
    assert not result


@pytest.mark.parametrize('original_list, len_sublist, expected_sublists', [
    ([0, 1, 2, 3, 4, 5, 6, 7, 8], 3, [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]),
    ([1, 2, 3, 4], 2, [[1, 2], [2, 3], [3, 4]]),
    ([0, 1, 2], 2, [[0, 1], [1, 2]])
])
def test_get_all_sublists(original_list, len_sublist, expected_sublists):
    # when
    sublists = get_all_sublists(original_list, len_sublist)

    # then
    assert sublists == expected_sublists


def test_is_a_row_when_is_a_row():
    # given
    nums = [3, 4, 5]
    row_length = 3

    # when
    result = is_a_row(nums, row_length)

    # then
    assert result

def test_is_a_row_when_is_not_a_row():
    # given
    nums = [0, 2, 3, 4]
    row_length = 3

    # when
    result = is_a_row(nums, row_length)

    # then
    assert not result



def test_is_start_of_row_when_start_of_row():
    # given
    position = 0
    row_length = 3

    # when
    result = is_start_of_row(position, row_length)

    # then
    assert result

def test_is_start_of_row_when_not_start_of_row():
    # given
    position = 1
    row_length = 3

    # when
    result = is_start_of_row(position, row_length)

    # then
    assert not result


def test_contains_column_when_contains_column():
    # given
    player_positions = [2, 5, 8]
    row_length = 3
    # when
    result = contains_column(player_positions, row_length)

    # then
    assert result

def test_contains_column_when_does_not_contains_column():
    # given
    player_positions = [0, 5, 8]
    row_length = 3
    # when
    result = contains_column(player_positions, row_length)

    # then
    assert not result

def test_has_all_values_when_has_all_values():
    # given
    player_positions = [0, 1, 2, 3, 4, 5]
    values = [0, 1, 2]

    # when
    result = has_all_values(player_positions, values)

    # then
    assert result

def test_has_all_values_when_does_not_have_all_values():
    # given
    player_positions = [0, 2, 3]
    column = [0, 1, 2]

    # when
    result = has_all_values(player_positions, column)

    # then
    assert not result



@pytest.mark.parametrize('row_length, expected_columns', [
    (0, []),
    (2, [[0, 2],[1, 3]]),
    (3, [[0, 3, 6], [1, 4, 7], [2, 5, 8]])
])
def test_get_all_columns(row_length, expected_columns):
    # when
    column_sublists = get_all_columns(row_length)

    # then
    assert column_sublists == expected_columns


def test_is_start_of_column_when_is_start():
    # given
    position = 2
    row_length = 3

    # when
    result = is_start_of_column(position, row_length)

    # then
    assert result

def test_is_start_of_column_when_is_not_start():
    # given
    position = 04
    row_length = 3

    # when
    result = is_start_of_column(position, row_length)

    # then
    assert not result


def test_contains_diagonal_when_contains_diagonal():
    # given
    player_positions = [3, 6, 9, 12, 14]
    row_length = 4

    # when
    result = contains_diagonal(player_positions, row_length)

    # then
    assert result

def test_contains_diagonal_when_does_not_contain_diagonal():
    # given
    player_positions = [3, 6, 9, 14]
    row_length = 4

    # when
    result = contains_diagonal(player_positions, row_length)

    # then
    assert not result


@pytest.mark.parametrize('row_length, expected_diagonal', [
    (1, [0]),
    (2, [0, 3]),
    (3, [0, 4, 8]),
    (4, [0, 5, 10, 15])
])
def test_get_left_corner_diagonal(row_length, expected_diagonal):
    # when
    diagonal_values = get_left_corner_diagonal(row_length)

    # then
    assert diagonal_values == expected_diagonal


@pytest.mark.parametrize('row_length, expected_diagonal', [
    (1, [0]),
    (2, [1, 2]),
    (3, [2, 4, 6]),
    (4, [3, 6, 9, 12])
])
def test_get_right_corner_diagonal(row_length, expected_diagonal):
    # when
    diagonal_values = get_right_corner_diagonal(row_length)

    # then
    assert diagonal_values == expected_diagonal


def test_no_moves_remain_when_no_moves_remain():
    # given
    board = ["X", "O", "O", "X"]

    # when
    result = no_moves_remain(board)

    # then
    assert result


def test_no_moves_remain_when_moves_still_remain():
    # given
    board = ["X", "O", 3, "X"]

    # when
    result = no_moves_remain(board)

    # then
    assert not result

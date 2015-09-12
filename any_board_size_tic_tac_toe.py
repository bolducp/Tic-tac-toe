
def get_row_length():
    try:
        row_length = int(raw_input("Enter desired length of rows."))
        return row_length
    except ValueError:
        print "Please enter a valid number greater than 0"
        return get_row_length()


def get_board(row_length):
    return [(num + 1) for num in xrange(row_length**2)]


def print_board(positions, row_length):
    for index in range(len(positions)):
        if index < 9 and type(positions[index]) == int:
            print " 0" + str(positions[index]) + " |",
        else:
            print " " + str(positions[index]) + " |",
        if (index + 1) % row_length == 0:
            print "\n", "------" * row_length


def player_move(board, user_symbol):
    move = get_player_move(board, user_symbol)
    board[move - 1] = " " + user_symbol + " "
    return board


def get_player_move(board, user_symbol):
    try:
        move = int(raw_input("Player " + user_symbol + ": Choose a position \n"))
        if move in range(1, len(board) + 1) and type(board[move - 1]) == int:
            return move
        else:
            print "Please enter a valid position"
            return get_player_move(board, user_symbol)
    except ValueError:
        print "Please enter a valid numeric position"
        return get_player_move(board, user_symbol)


def player_has_won(board, player_symbol, row_length):
    player_positions = [index for index in xrange(row_length**2) if player_symbol in str(board[index])]
    return contains_winning_combination(player_positions, row_length)


def contains_winning_combination(player_positions, row_length):
    return contains_row(player_positions, row_length) or contains_column(player_positions, row_length) or \
           contains_diagonal(player_positions, row_length)

def contains_row(player_positions, row_length):
    player_positions = sorted(player_positions)
    for possible_row in get_all_sublists(player_positions, row_length):
        if is_a_row(possible_row, row_length):
            return True
    return False

def get_all_sublists(original_list, len_sublist):
    sublists = []
    last_possible_starting_sublist_index = len(original_list) - len_sublist
    for start_of_sublist in xrange(last_possible_starting_sublist_index + 1):
        end_of_sublist = start_of_sublist + len_sublist
        sublist = original_list[start_of_sublist:end_of_sublist]
        sublists.append(sublist)
    return sublists

def is_a_row(nums, row_length):
    return is_start_of_row(nums[0], row_length) and nums[-1] - nums[0] == row_length - 1

def is_start_of_row(position, row_length):
    return position in (row_length * row_number for row_number in xrange(row_length))



def contains_column(player_positions, row_length):
    for column_values in get_all_columns(row_length):
        if has_all_values(player_positions, column_values):
            return True
    return False

def has_all_values(player_positions, values):
    for position in values:
        if position not in player_positions:
            return False
    return True

def get_all_columns(row_length):
    num_rows = row_length
    positions = [num for num in xrange(row_length**2)]
    sublists = []

    for num in positions:
        if is_start_of_column(num, row_length):
            sublist = []
            for i in xrange(num_rows):
                sublist.append(num + (row_length * i))
            sublists.append(sublist)
    return sublists

def is_start_of_column(position, row_length):
    return position in xrange(row_length)



def contains_diagonal(player_positions, row_length):
    return has_all_values(player_positions, get_left_corner_diagonal(row_length)) \
           or has_all_values(player_positions, get_right_corner_diagonal(row_length))


def get_left_corner_diagonal(row_length):
    positions = [num for num in xrange(row_length**2)]
    num_rows = row_length
    diagonal = []
    start_diagonal = positions[0]

    for index in xrange(num_rows):
        diagonal.append(start_diagonal + ((row_length + 1) * index))
    return diagonal

def get_right_corner_diagonal(row_length):
    positions = [num for num in xrange(row_length**2)]
    num_rows = row_length
    diagonal = []
    start_diagonal = positions[row_length -1]

    for index in xrange(num_rows):
        diagonal.append(start_diagonal + ((row_length - 1) * index))
    return diagonal


def no_moves_remain(board):
    for position in board:
        if type(position) == int:
            return False
    return True

def print_outcome(board, row_length):
    if player_has_won(board, 'X', row_length):
        print "Player1 wins!"
    elif player_has_won(board, "O", row_length):
        print "Player2 wins!"
    elif no_moves_remain(board):
        print "No moves remain. It's a tie."
    else:
        print "Something went wrong."



def main():
    row_length = get_row_length()
    board = get_board(row_length)
    print_board(board, row_length)

    while True:
        if player_has_won(board, "O", row_length) or no_moves_remain(board):
            print_outcome(board, row_length)
            break
        player_move(board, "X")
        print_board(board, row_length)

        if player_has_won(board, "X", row_length) or no_moves_remain(board):
            print_outcome(board, row_length)
            break
        else:
            player_move(board, "O")
            print_board(board, row_length)


if __name__ == "__main__":
    main()
positions = ["_1_|", "_2_", "|_3_", "_4_|", "_5_", "|_6_", " 7 |", " 8 ", "| 9 "]


def print_board():
    for index in range(9):
        print positions[index],
        if (index + 1) % 3 == 0:
            print


def make_user_move(player_symbol):
    try:
        move = int(raw_input("\nPlayer %s: Choose a position:  \n" % player_symbol))
        if move in range(1, 10) and "X" not in positions[move - 1] and "O" not in positions[move - 1]:
            positions[move - 1] = " %s " % player_symbol
        else:
            print "Please enter a valid position"
            return make_user_move(player_symbol)
    except ValueError:
        print "Please enter a valid numeric position"
        return make_user_move(player_symbol)


def game_has_been_won(player_symbols):
    for player_symbol in player_symbols:
        if player_has_won(player_symbol):
            return True
    return False


def player_has_won(player_symbol):
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        if player_has_combo(player_symbol, combo):
            return True
    return False


def player_has_combo(player_symbol, combo):
    for index in combo:
        if player_symbol not in positions[index]:
            return False
    return True


def no_moves_remain():
    for position in positions:
        if "X" not in position and "O" not in position:
            return False
    return True


def print_outcome():
    if player_has_won("X"):
        print "Player X wins!"
    elif player_has_won("O"):
        print "Player O wins!"
    elif no_moves_remain():
        print "No moves remain. It's a tie."
    else:
        print "Something went wrong."


def main():
    print_board()
    player_symbols = ["X", "O"]

    while True:
        for player_symbol in player_symbols:
            if game_has_been_won(player_symbols) or no_moves_remain():
                print_outcome()
                return

            make_user_move(player_symbol)
            print_board()


if __name__ == "__main__":
    main()

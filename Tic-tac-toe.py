

positions = ["_1_|", "_2_", "|_3_", "_4_|", "_5_", "|_6_", " 7 |", " 8 ", "| 9 "]

def print_board():
    for i in xrange(9):
        print positions[i],
        if (i + 1) % 3 == 0:
            print


def get_user1_move():
    move = int(raw_input("Player 1: Choose a position \n"))
    if move in range(1, 10) and positions[move - 1] != " X " and positions[move - 1] != " O ":
        positions[move - 1] = " X "
    else:
        print "Please enter a valid position"
        return get_user1_move()


def get_user2_move():
    move = int(raw_input("Player 2: Choose a position \n"))
    if move in range(1, 10) and positions[move - 1] != " X " and positions[move - 1] != " O ":
        positions[move - 1] = " O "
    else:
        print "Please enter a valid position"
        return get_user2_move()


def player_has_won(player_symbol):
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        player_symbol_count = 0
        for index in combo:
            if player_symbol in positions[index]:
                player_symbol_count += 1
        if player_symbol_count == 3:
            return True
    return False


def no_moves_remain():
    for position in positions:
        if position != " X " and position != " O ":
            return False
    return True


def print_outcome():
    if no_moves_remain():
        print "No moves remain. It's a tie."
    elif player_has_won("X"):
        print "Player 1 wins!"
    elif player_has_won("O"):
        print "Player 2 wins!"
    else:
        print "Something went wrong."


def main():
    print_board()

    while True:
        if player_has_won("x") or player_has_won("O") or no_moves_remain():
            print_outcome()
            break
        get_user1_move()
        print_board()

        if player_has_won("x") or player_has_won("O") or no_moves_remain():
            print_outcome()
            break
        else:
            get_user2_move()
            print_board()


if __name__ == "__main__":
    main()

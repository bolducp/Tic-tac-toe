
def get_row_length():
    try:
        row_length = int(raw_input("Enter desired length of rows."))
        return row_length
    except ValueError:
        print "Please enter a valid number greater than 0"
        return get_row_length()


class Board(object):
    def __init__(self, row_length):
        self.row_length = row_length
        self.board_positions = [(num + 1) for num in xrange(self.row_length**2)]

    def print_board(self):
        for index in range(len(self.board_positions)):
            if index < 9 and type(self.board_positions[index]) == int:
                print " 0" + str(self.board_positions[index]) + " |",
            else:
                print " " + str(self.board_positions[index]) + " |",
            if (index + 1) % self.row_length == 0:
                print "\n", "------" * self.row_length


class Player(object):
    def __init__(self, player_symbol, board):
        self.player_symbol = player_symbol
        self.board = board

    def get_player_positions(self):
        return [index for index in xrange(self.board.row_length**2) if self.player_symbol in str(self.board.board_positions[index])]

    def player_move(self):
        move = self.get_player_move()
        self.board.board_positions[move - 1] = " " + self.player_symbol + " "

    def get_player_move(self):
        try:
            move = int(raw_input("Player " + self.player_symbol + ": Choose a position \n"))
            if move in range(1, len(self.board.board_positions) + 1) and type(self.board.board_positions[move - 1]) == int:
                return move
            else:
                print "Please enter a valid position"
                return self.get_player_move()
        except ValueError:
            print "Please enter a valid numeric position"
            return self.get_player_move()



class Ajudicator(object):
    def __init__(self, board, *players):
        self.board = board
        self.players = players

    def no_moves_remain(self):
        for position in self.board.board_positions:
            if type(position) == int:
                return False
        return True

    def some_player_has_won(self):
        for player in self.players:
            player_positions = player.get_player_positions()
            if self.contains_winning_combination(player_positions):
                return True
        return False

    def contains_winning_combination(self, player_positions):
        return self.contains_row(player_positions) or self.contains_column(player_positions) or \
               self.contains_diagonal(player_positions)

    def contains_row(self, player_positions):
            player_positions = sorted(player_positions)
            for possible_row in self.get_all_sublists(player_positions, self.board.row_length):
                if self.is_a_row(possible_row):
                    return True
            return False

    def get_all_sublists(self, original_list, len_sublist):
        sublists = []
        last_possible_starting_sublist_index = len(original_list) - len_sublist
        for start_of_sublist in xrange(last_possible_starting_sublist_index + 1):
            end_of_sublist = start_of_sublist + len_sublist
            sublist = original_list[start_of_sublist:end_of_sublist]
            sublists.append(sublist)
        return sublists

    def is_a_row(self, nums):
        return self.is_start_of_row(nums[0]) and (nums[-1] - nums[0] == self.board.row_length - 1)

    def is_start_of_row(self, position):
        return position in (self.board.row_length * row_number for row_number in xrange(self.board.row_length))

    def contains_column(self, player_positions):
        for column_values in self.get_all_columns():
            if self.has_all_values(player_positions, column_values):
                return True
        return False

    def has_all_values(self, player_positions, values):
        for position in values:
            if position not in player_positions:
                return False
        return True

    def get_all_columns(self):
        num_rows = self.board.row_length
        positions = [num for num in xrange(self.board.row_length**2)]
        sublists = []

        for num in positions:
            if self.is_start_of_column(num):
                sublist = []
                for i in xrange(num_rows):
                    sublist.append(num + (self.board.row_length * i))
                sublists.append(sublist)
        return sublists

    def is_start_of_column(self, position):
        return position in xrange(self.board.row_length)


    def contains_diagonal(self, player_positions):
        return self.has_all_values(player_positions, self.get_left_corner_diagonal()) \
               or self.has_all_values(player_positions, self.get_right_corner_diagonal())

    def get_left_corner_diagonal(self):
        positions = [num for num in xrange(self.board.row_length**2)]
        num_rows = self.board.row_length
        diagonal = []
        start_diagonal = positions[0]

        for index in xrange(num_rows):
            diagonal.append(start_diagonal + ((self.board.row_length + 1) * index))
        return diagonal

    def get_right_corner_diagonal(self):
        positions = [num for num in xrange(self.board.row_length**2)]
        num_rows = self.board.row_length
        diagonal = []
        start_diagonal = positions[self.board.row_length -1]

        for index in xrange(num_rows):
            diagonal.append(start_diagonal + ((self.board.row_length - 1) * index))
        return diagonal


    def find_which_player_has_won(self):
            for player in self.players:
                player_positions = player.get_player_positions()
                if self.contains_winning_combination(player_positions):
                    return player.player_symbol
            return False

    def print_outcome(self):
        if self.some_player_has_won():
            winner = self.find_which_player_has_won()
            print "Player %s wins!" % winner
        elif self.no_moves_remain():
            print "No moves remain. It's a tie."
        else:
            print "Something went wrong."



def main():
    row_length = get_row_length()
    board = Board(row_length)
    board.print_board()

    player_x = Player("X", board)
    player_o = Player("O", board)

    ajudicator = Ajudicator(board, player_x, player_o)

    while True:
        if ajudicator.some_player_has_won() or ajudicator.no_moves_remain():
            ajudicator.print_outcome()
            break
        player_x.player_move()
        board.print_board()

        if ajudicator.some_player_has_won() or ajudicator.no_moves_remain():
            ajudicator.print_outcome()
            break
        player_o.player_move()
        board.print_board()


if __name__ == "__main__":
    main()

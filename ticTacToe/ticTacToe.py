
class Board:

    def __init__(self):
        self.symbols = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.game_board = f"\n\t\t {self.symbols[0]} | {self.symbols[1]}\n" \
                          f"\t\t-----------\t\t\t\t-----------\n" \
                          f"\t\t {self.symbols[3]} | {self.symbols[4]}\n" \
                          f"\t\t-----------\t\t\t\t-----------\n" \
                          f"\t\t {self.symbols[6]} | {self.symbols[7]}\n"

    def update_board(self):
        self.game_board = f"\n\t\t {self.symbols[0]} | {self.symbols[1]} | {self.symbols[2]}\t\t\t\t 1 | 2 | 3\n" \
                          f"\t\t-----------\t\t\t\t-----------\n" \
                          f"\t\t {self.symbols[3]} | {self.symbols[4]} | {self.symbols[5]}\t\t\t\t 4 | 5 | 6\n" \
                          f"\t\t-----------\t\t\t\t-----------\n" \
                          f"\t\t {self.symbols[6]} | {self.symbols[7]} | {self.symbols[8]}\t\t\t\t 7 | 8 | 9\n"

    @staticmethod
    def display_players(player1, player2):
        print(f"\t{player1.name}: '{player1.symbol}'\t\t{player2.name}: '{player2.symbol}'")

    def print_board(self):
        return print(self.game_board)

    def check_score(self, player1, player2):
        # Diagonal lines
        if self.symbols[0] == self.symbols[4] == self.symbols[8] and self.symbols[0] != " ":
            if self.symbols[0] == player1.symbol:
                print(f"{player1.name} wins!")
                return True
            else:
                print(f"{player2.name} wins!")
                return True

        if self.symbols[2] == self.symbols[4] == self.symbols[6] and self.symbols[2] != " ":
            if self.symbols[2] == player1.symbol:
                print(f"{player1.name} wins!")
                return True
            else:
                print(f"{player2.name} wins!")
                return True

        # Horizontal lines
        for i in range(0, 9, 3):
            if self.symbols[i] == self.symbols[i+1] == self.symbols[i] == self.symbols[i+2] and self.symbols[i] != " ":
                if self.symbols[i] == player1.symbol:
                    print(f"{player1.name} wins!")
                    return True
                else:
                    print(f"{player2.name} wins!")
                    return True

        # Vertical lines
        for i in range(0, 3):
            if self.symbols[i] == self.symbols[i + 3] and self.symbols[i] == self.symbols[i + 6] and self.symbols[i] != " ":
                if self.symbols[i] == player1.symbol:
                    print(f"{player1.name} wins!")
                    return True
                else:
                    print(f"{player2.name} wins!")
                    return True


class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = ""

    def __str__(self):
        return f"{self.name}, symbol: {self.symbol}"

    def choose_symbol(self):
        self.symbol = input("Whait is your symbol? 'X' / 'O': ").upper()
        while self.symbol not in ["X", "O"]:
            self.symbol = input("Whait is your symbol? 'X' / 'O': ").upper()


class Symbols(Board):
    def __init__(self, current_game_board):
        self.symbols = current_game_board.symbols

    def get_player_symbol(self, player):
        try:
            player_index = int(input(f"{player.name}, please choose a spot: "))
            while player_index not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Choose from range 1 to 9!")
                player_index = int(input("Spot: "))

            while self.symbols[player_index-1] != " ":
                available_spots = [str(index+1) for index, symbol in enumerate(self.symbols) if symbol == " "]
                print(f"Spot number {player_index} already taken! Please choose from: ", ", ". join(available_spots))
                player_index = int(input("Spot: "))

            return player_index-1, player.symbol
        except ValueError:
            print("Choose from range 1 to 9!")
            return None

def check_game_status(board, player_moves):
    game_status = input("Would you like to continue? (Y/N): ").upper()
    while game_status not in ["Y", "Yes", "N", "NO"]:
        game_status = input("Type 'Y' to CONTINUE or 'N' to EXIT: ").upper()
    if game_status in ["Y", "YES"]:
        board.__init__()
        player_moves.__init__(board)
        return True
    else:
        return False


def main():
    board = Board()
    player_moves = Symbols(board)
    player1 = Player(input("Player 1 name: "))
    player1.choose_symbol()
    player2 = Player(input("Player 2 name: "))

    if player1.symbol == "X":
        player2.symbol = "O"
    else:
        player2.symbol = "X"

    turn = 0

    while True:
        # Check whos turn it is
        if turn % 2 == 0:
            player = player1
        else:
            player = player2

        player_move = player_moves.get_player_symbol(player)
        while not player_move:
            player_move = player_moves.get_player_symbol(player)
        board.symbols[player_move[0]] = player_move[1]

        board.update_board()
        board.display_players(player1, player2)
        board.print_board()
        if board.check_score(player1, player2):
            if check_game_status(board, player_moves):
                turn = 0
            else:
                break
        else:
            if turn == 8:
                print("It's a tie!")
                if check_game_status(board, player_moves):
                    turn = 0
                else:
                    break
            else:
                turn += 1
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()

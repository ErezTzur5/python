class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            self.print_board()
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

# Main game loop
game = TicTacToe()
while True:
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    if game.make_move(row, col):
        winner = game.check_winner()
        if winner:
            print(f"Player {winner} wins!")
            break
        elif game.is_board_full():
            print("It's a tie!")
            break

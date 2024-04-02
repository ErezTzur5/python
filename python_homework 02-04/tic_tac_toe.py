import time
from colorama import Fore,Style,init

init(autoreset=True)

class TicTacToe:
    def __init__(self):
        # Initialize the board
        self.board = [[' ' for _ in range(3)] for _ in range(3)] #list comprehension that iterates 3 times help us create 3X3 grid.
        self.current_player = 'X'
        self.players = {'X': '', 'O': ''}
        self.wins = {'X': 0, 'O': 0}
        self.games_played = 0
        self.game_results = []

    def print_board(self):
        """
        This func prints the current board.

        """
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if j != 0:
                    print('|', end='')
                if cell == 'X':
                    print(Fore.RED + 'X', end='')
                elif cell == 'O':
                    print(Fore.BLUE + 'O', end='')
                else:
                    print(' ', end='')
            print(Style.RESET_ALL)
            if i != 2:
                print('-' * 5)

    def make_move(self, row:int, col:int):
        """
        This func takes from the player an integer from 1 - 3 , and make the move on the board.
        this func checks that the space is not taken.
        
        """
        try:
            if self.board[row][col] == ' ': #checks if the place is empty
                self.board[row][col] = self.current_player
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Invalid move. That space is already taken.")
        except IndexError:
            print("please enter number from 1-3")

    def check_winner(self):
        """
        This func checks for a winner while trying to run all the available combination and checks for a win
        
        """
        
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_full(self):
        """
        This func checks if the board is full.
        incase the board is full the game stops as draw.    
        """
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def start_game(self):
        """
        This func is the main func to start a game in tic tac toe

        """
        print("Welcome to Tic-Tac-Toe!")
        self.players['X'] = input("Enter name for Player 1: ")
        self.players['O'] = input("Enter name for Player 2: ")

        while True:
            x_choice = input(f"{self.players['X']}, do you want to be X or O? (X/O): ").upper()
            if x_choice == 'O' or x_choice == 'X':
                break
            else:
                print("Invalid choice. Please enter 'X' or 'O'.")

        if x_choice == 'O':
            self.players['X'], self.players['O'] = self.players['O'], self.players['X']

        start_time = time.time()

        while True:
            game.print_board()
            try:
                row = int(input(f"{self.players[self.current_player]}, enter the row (1-3): ")) - 1
                col = int(input(f"{self.players[self.current_player]}, enter the column (1-3): ")) - 1
            except:
                print("Please input a number!")
            game.make_move(row, col)
            winner = game.check_winner()
            if winner: #incase theres a winner the game will end
                game.print_board()
                print(f"Congratulations, {self.players[winner]} wins!")
                self.wins[winner] += 1
                break
            elif game.is_full(): #if winner condition doesnt heppend it will check if the board is full , if it is then its a DRAW!
                game.print_board()
                print("It's a draw!")
                break

            print("\n" * 10)  # Clear the screen for the next player's turn

        end_time = time.time()
        game_duration = end_time - start_time
        print(f"Game duration: {game_duration:.2f} seconds") #.2f make the number rounded to 2 decimal places.

        self.games_played += 1
        self.game_results.append((self.players['X'], self.players['O'], self.wins['X'], self.wins['O'], game_duration))

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'yes':
            self.board = [[' ' for _ in range(3)] for _ in range(3)] #creates a new board for a new game
            self.current_player = 'X'
            self.start_game()
        else:
            with open("game_results.txt", "a") as file: #incase user chose to stop the game , a log of the game will be saved as txt file.
                file.write(f"Game {self.games_played} results:\n")
                for result in self.game_results:
                    file.write(f"{result[0]} vs {result[1]} - {result[2]} wins for {result[0]}, {result[3]} wins for {result[1]}, duration: {result[4]:.2f} seconds\n")
                file.write("\n")

# Main loop
game = TicTacToe()
game.start_game()

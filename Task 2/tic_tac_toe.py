def print_board(board):
    print("---------")
    for row in board:
        print("|".join(row))
        print("---------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    print("Welcome to Tic Tac Toe!")
    
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)
            print(f"Player {current_player}'s turn.")
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
                if row not in range(3) or col not in range(3) or board[row][col] != " ":
                    print("Invalid move. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
            
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

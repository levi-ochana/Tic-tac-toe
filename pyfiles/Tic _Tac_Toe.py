import random

def display_board(board, player1_marker, player2_marker):
    print("\n" * 100)
    print(f'Player 1: {player1_marker} | Player 2: {player2_marker}')
    print('   |   |   ')
    print(f' {board[0][2]} | {board[1][2]} | {board[2][2]} ')
    print('---|---|---')
    print(f' {board[0][1]} | {board[1][1]} | {board[2][1]} ')
    print('---|---|---')
    print(f' {board[0][0]} | {board[1][0]} | {board[2][0]} ')
    print('   |   |   ')

def player_input():
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input("Player 1, please choose 'X' or 'O': ").lower()
        if marker == 'x':
            player_2 = 'o'
        elif marker == 'o':
            player_2 = 'x'
        else:
            print("Invalid choice. Please choose 'X' or 'O'.")
    return marker.upper(), player_2.upper()

def place_marker(board, marker, row, col):
    board[row][col] = marker

def win_check(board, mark):

    for row in board:
        if row.count(mark) == 3:
            return True

    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True

    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[2][0] == board[1][1] == board[0][2] == mark:
        return True
    return False

def choose_first():
    return 'player 1' if random.randint(0, 1) == 0 else 'player 2'

def space_check(board, row, col):
    return board[row][col] == ' '

def full_board_check(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_choice(board, player_name):
    position = None
    valid_positions = {7: (0, 2), 8: (1, 2), 9: (2, 2),
                       4: (0, 1), 5: (1, 1), 6: (2, 1),
                       1: (0, 0), 2: (1, 0), 3: (2, 0)}
    while position not in valid_positions:
        try:
            position = int(input(f'{player_name}, choose your next position (1-9): '))
            if position not in valid_positions:
                print("Please choose a valid number between 1 and 9.")
            else:
                row, col = valid_positions[position]
                if not space_check(board, row, col):
                    print("That position is already taken.")
                    position = None
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
    return row, col

def replay():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input('Do you want to play again? Enter Yes (y) or No (n): ').lower()
        if choice not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
    return choice == 'y'

def start_game():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input('Are you ready to play? Enter Yes (y) or No (n): ').lower()
        if choice not in ['y', 'n']:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
    return choice == 'y'

# Main game
print('Welcome to Tic Tac Toe Game!')

while True:
    theBoard = [[' ' for _ in range(3)] for _ in range(3)]
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_on = start_game()

    while game_on:
        if turn == 'player 1':
            display_board(theBoard, player1_marker, player2_marker)
            row, col = player_choice(theBoard, 'Player 1')
            place_marker(theBoard, player1_marker, row, col)

            if win_check(theBoard, player1_marker):
                display_board(theBoard, player1_marker, player2_marker)
                print('Congratulations! Player 1 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, player1_marker, player2_marker)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player 2'

        else:
            display_board(theBoard, player1_marker, player2_marker)
            row, col = player_choice(theBoard, 'Player 2')
            place_marker(theBoard, player2_marker, row, col)

            if win_check(theBoard, player2_marker):
                display_board(theBoard, player1_marker, player2_marker)
                print('Congratulations! Player 2 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard, player1_marker, player2_marker)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player 1'

    if not replay():
        break

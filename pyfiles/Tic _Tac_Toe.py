import random

def display_board(board):
   print('-----')
   print(board[7], board[8], board[9])
   print(board[4], board[5], board[6])
   print(board[1], board[2], board[3])
   print('-----')

def player_input():
   marker = ''
   while marker != 'x' and marker != 'o':
      marker = input("Player 1, please choose 'x' or 'o': ").lower()
      if marker == 'x':
         player_2 = 'o'
      elif marker == 'o':
         player_2 = 'x'
      else:
         print("Invalid choice. Please choose 'x' or 'o'.")
   return marker, player_2

def place_marker(board, marker, position):
   board[position] = marker

def win_check(board, mark):
   return ((board[7] == board[8] == board[9] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[1] == board[2] == board[3] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[7] == board[5] == board[3] == mark) or
           (board[9] == board[5] == board[1] == mark))

def choose_first():
   if random.randint(0, 1) == 0:
      return 'player 2'
   else:
      return 'player 1'

def space_check(board, position):
   return board[position] == ' '

def full_board_check(board):
   for i in range(1, 10):
      if space_check(board, i):
         return False
   return True

def player_choice(board):
   position = 0
   while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
      position = int(input('Choose your next position (1-9): '))
   return position

def replay():
   return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Main game
print('Welcome to Tic Tac Toe Game!')

while True:
   theBoard = [' '] * 10
   player1_marker, player2_marker = player_input()
   turn = choose_first()
   print(turn + ' will go first.')

   play_game = input('Are you ready to play? Enter Yes or No: ').lower()
   if play_game[0] == 'y':
      game_on = True
   else:
      game_on = False

   while game_on:
      if turn == 'player 1':
         display_board(theBoard)
         position = player_choice(theBoard)
         place_marker(theBoard, player1_marker, position)

         if win_check(theBoard, player1_marker):
            display_board(theBoard)
            print('Congratulations! Player 1 won the game!')
            game_on = False
         else:
            if full_board_check(theBoard):
               display_board(theBoard)
               print('The game is a draw!')
               break
            else:
               turn = 'player 2'

      else:
         display_board(theBoard)
         position = player_choice(theBoard)
         place_marker(theBoard, player2_marker, position)

         if win_check(theBoard, player2_marker):
            display_board(theBoard)
            print('Congratulations! Player 2 won the game!')
            game_on = False
         else:
            if full_board_check(theBoard):
               display_board(theBoard)
               print('The game is a draw!')
               break
            else:
               turn = 'player 1'

   if not replay():
      break

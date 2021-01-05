"""TIC TAC TOE GAME"""
from models.PlayerModel import Player
from models.BoardModel import Board
from helper import *
from menu import load_menu


# START
print('{}'.format('\n') * 10)
print("\n\n\n\t\tWelcome!\n------------------------\n")
restart = 'y'


# Start/Restart Game
while restart.lower() == 'y':
    # Player/Board Instances
    player1 = Player(player_number=1)
    player2 = Player(player_number=2)
    load_menu()
    board = Board()

    icon_dict = {k: '' for k in [i for i in range(1, 10)]}

    player_select(player1, player2)

    # Game Loop
    while board.did_win is False:

        board.print_board(icon_dict)

        if board.victory_check(icon_dict):
            break

        # Using turn variable to decide which player is next
        player_move(player1, icon_dict) if board.turn % 2 == 0 else player_move(player2, icon_dict)

        # Incrementing turn and prints newlines between board displays
        board.increment()

        print('{}'.format('\n') * 15)

    # End Game Notification
    board.handle_win_loss()
    restart = input('Would you like to play Tic Tac Toe again? (Y/N): ')

print("\n-------------------------------")
print("*\t\t\t\t\t\t\t  *")
print("*\tThank you for playing!!\t  *")
print("*\t\t\t\t\t\t\t  *")
print("-------------------------------")

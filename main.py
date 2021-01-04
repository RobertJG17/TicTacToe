"""TIC TAC TOE GAME"""
import time
from PlayerModel import Player
from BoardModel import Board


# Helper Functions
def player_select():
    while player1.player_icon not in ('X', 'O'):
        player1.player_icon = input('Player 1, Do you want to be X or O?: ').upper()
        player1.player_icon.replace(" ", "")

    if player1.player_icon == 'X':
        player2.player_icon = 'O'
    else:
        player2.player_icon = 'X'

    print('\nPlayer 1 --> {} <-- will go first\n\n'.format(player1.player_icon))
    print('Please wait for the screen to display')

    time.sleep(3.75)
    print('{}'.format('\n') * 20)


def player_move(player):
    player.player_input = input('Player {}, please enter a number (1 - 9) to input '
                                'an {} in the corresponding location:\n'.format(player.player_number,
                                                                                player.player_icon))
    player.check_logic(icon_dict)
    icon_dict[player.player_input] = player.player_icon


# START
print('{}'.format('\n') * 10)
print("\n\n\n\t\tWelcome!\n------------------------\n")
restart = 'y'

# Start/Restart Game
while restart.lower() == 'y':
    # Player/Board Instances
    player1 = Player(player_icon='', player_number=1)
    player2 = Player(player_icon='', player_number=2)
    board = Board()
    icon_dict = {k: '' for k in [i for i in range(1, 10)]}

    player_select()

    # Game Loop
    while board.did_win is False:

        board.print_board(icon_dict)
        if board.victory_check(icon_dict):
            break

        # Using turn variable to decide which player is next
        player_move(player1) if board.turn % 2 == 0 else player_move(player2)

        # Incrementing turn and prints newlines between board displays
        board.increment()

        print('{}'.format('\n') * 15)

    # End Game Notification
    board.handle_win_loss()
    restart = input('Would you like to play again? (Y/N): ')


print("\n\n\n\t\tThank you for playing!!\n------------------------\n")

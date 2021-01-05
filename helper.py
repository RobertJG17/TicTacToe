import time


# Helper Functions
def player_select(p1, p2):
    while p1.player_icon not in ('X', 'O'):
        p1.player_icon = input('Player 1, Do you want to be X or O?: ').upper()
        p1.player_icon.replace(" ", "")

    if p1.player_icon == 'X':
        p2.player_icon = 'O'
    else:
        p2.player_icon = 'X'

    print('\nPlayer 1 --> {} <-- will go first\n\n'.format(p1.player_icon))
    print('Please wait for the screen to display')

    time.sleep(3.75)
    print('{}'.format('\n') * 20)


def player_move(player, icon_dict):
    player.player_input = input('Player {}, please enter a number (1 - 9) to input '
                                'an {} in the corresponding location:\n'.format(player.player_number,
                                                                                player.player_icon))
    player.check_logic(icon_dict)
    icon_dict[player.player_input] = player.player_icon

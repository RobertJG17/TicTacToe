"""TIC TAC TOE GAME"""
import time
import Player


# Logic checker for board input
def check_logic(player, p_input, p_number):
    valid = False

    while not valid:

        # Make sure the input is an Integer Value
        try:
            p_input = int(p_input)
        except ValueError:
            print('\nInvalid entry')
            p_input = input('Player {}, please enter a number (1 - 9) to input '
                            'an {} in the corresponding location:\n'.format(p_number, player))
            continue

        # Make sure they enter a number between 1-10
        if p_input not in range(1, 10):
            p_input = input('Player {} out of range index, please enter a number (1 - 9) to input '
                            'an {} in the corresponding location:\n'.format(p_number, player))
            continue

        # Make sure that cell is not already taken
        if dictionary[p_input] is not '':
            print('That cell has already been taken, please choose a valid cell!\n')
            p_input = input('Player {}, please enter a number (1 - 9) to input '
                            'an {} in the corresponding location:\n'.format(player_number, player))
            continue

        valid = True

    return p_input


print("\n\n\n\t\tWelcome!\n------------------------\n")
dictionary = {k: '' for k in [i for i in range(1, 10)]}
won = False
turn = 0

player1 = ''
while player1 not in ('X', 'O'):
    print("Please enter a valid choice (X, O)")
    player1 = input('Player 1, Do you want to be X or O?: ').upper()
    player1 = player1.replace(" ", "")

if player1 == 'X':
    player2 = 'O'
else:
    player2 = 'X'

print('\nPlayer 1 --> {} <-- will go first\n\n'.format(player1))
print('Please wait for the screen to display')

time.sleep(3.75)
print('{}'.format('\n') * 20)

# Game Loop
while won is False:
    # Board Layout
    print('Board layout is as follows: 7 | 8 | 9\n\t\t\t\t\t\t'
          '   -----------'
          '\n\t\t\t\t\t\t\t4 | 5 | 6\n\t\t\t\t\t\t   '
          '-----------\n\t\t\t\t\t\t\t1 | 2 | 3')
    print('\t\t|\t\t|\t')
    print('\t{}\t|\t{}\t|\t{}'.format(dictionary[7], dictionary[8], dictionary[9]))
    print('\t\t|\t\t|')
    print('-------------------------')
    print('\t\t|\t\t|')
    print('\t{}\t|\t{}\t|\t{}'.format(dictionary[4], dictionary[5], dictionary[6]))
    print('\t\t|\t\t|')
    print('-------------------------')
    print('\t\t|\t\t|')
    print('\t{}\t|\t{}\t|\t{}'.format(dictionary[1], dictionary[2], dictionary[3]))
    print('\t\t|\t\t|\t')

    # Victory Check

    # Rows
    if '' not in (dictionary[7], dictionary[8], dictionary[9]) and dictionary[7] == dictionary[8] == dictionary[9]:
        won = True
    elif '' not in (dictionary[4], dictionary[5], dictionary[6]) and dictionary[4] == dictionary[5] == dictionary[6]:
        won = True
    elif '' not in (dictionary[1], dictionary[2], dictionary[3]) and dictionary[1] == dictionary[2] == dictionary[3]:
        won = True

    #Columns
    elif '' not in (dictionary[7], dictionary[4], dictionary[1]) and dictionary[7] == dictionary[4] == dictionary[1]:
        won = True
    elif '' not in (dictionary[2], dictionary[5], dictionary[8]) and dictionary[2] == dictionary[5] == dictionary[8]:
        won = True
    elif '' not in (dictionary[9], dictionary[6], dictionary[3]) and dictionary[9] == dictionary[6] == dictionary[3]:
        won = True

    # Diagonals
    elif '' not in (dictionary[7], dictionary[5], dictionary[3]) and dictionary[7] == dictionary[5] == dictionary[3]:
        won = True
    elif '' not in (dictionary[9], dictionary[5], dictionary[1]) and dictionary[9] == dictionary[5] == dictionary[1]:
        won = True
    else:
        pass

    # If all spaces on the board are filled or player won
    if won is True or turn == 9:
        break

    # Using turn variable to decide which player is next
    if turn % 2 == 0:

        player_number = 1
        player_input = input('Player 1, please enter a number (1 - 9) to input '
                             'an {} in the corresponding location:\n'.format(player1))
        player_input = check_logic(player1, player_input, player_number)
        dictionary[player_input] = player1

    else:

        player_number = 2
        player_input = input('Player 2, please enter a number (1 - 9) to input '
                             'an {} in the corresponding location:\n'.format(player2))
        player_input = check_logic(player2, player_input, player_number)
        dictionary[player_input] = player2

    # Incrementing turn and prints newlines between board displays
    turn += 1
    print('{}'.format('\n') * 15)

# End Game Notification
if turn == 9 and won is False:
    print('Cat\'s game!')
elif turn % 2 == 0:
    print('Player 2 has won!')
else:
    print('Player 1 has won!')


class Board:

    def __init__(self, did_win=False, turn=0):
        self.did_win = did_win
        self.turn = turn

    def increment(self):
        self.turn += 1

    @staticmethod
    def print_board(icon_dict):
        # Board Layout
        print('Board layout is as follows: 7 | 8 | 9\n\t\t\t\t\t\t'
              '   -----------'
              '\n\t\t\t\t\t\t\t4 | 5 | 6\n\t\t\t\t\t\t   '
              '-----------\n\t\t\t\t\t\t\t1 | 2 | 3')
        print('\t\t|\t\t|\t')
        print('\t{}\t|\t{}\t|\t{}'.format(icon_dict[7], icon_dict[8], icon_dict[9]))
        print('\t\t|\t\t|')
        print('-------------------------')
        print('\t\t|\t\t|')
        print('\t{}\t|\t{}\t|\t{}'.format(icon_dict[4], icon_dict[5], icon_dict[6]))
        print('\t\t|\t\t|')
        print('-------------------------')
        print('\t\t|\t\t|')
        print('\t{}\t|\t{}\t|\t{}'.format(icon_dict[1], icon_dict[2], icon_dict[3]))
        print('\t\t|\t\t|\t')

    def victory_check(self, icon_dict):
        # Victory Check

        # Rows
        if '' not in (icon_dict[7], icon_dict[8], icon_dict[9]) and icon_dict[7] == icon_dict[8] == icon_dict[9]:
            self.did_win = True
        elif '' not in (icon_dict[4], icon_dict[5], icon_dict[6]) and icon_dict[4] == icon_dict[5] == icon_dict[6]:
            self.did_win = True
        elif '' not in (icon_dict[1], icon_dict[2], icon_dict[3]) and icon_dict[1] == icon_dict[2] == icon_dict[3]:
            self.did_win = True

        # Columns
        elif '' not in (icon_dict[7], icon_dict[4], icon_dict[1]) and icon_dict[7] == icon_dict[4] == icon_dict[1]:
            self.did_win = True
        elif '' not in (icon_dict[2], icon_dict[5], icon_dict[8]) and icon_dict[2] == icon_dict[5] == icon_dict[8]:
            self.did_win = True
        elif '' not in (icon_dict[9], icon_dict[6], icon_dict[3]) and icon_dict[9] == icon_dict[6] == icon_dict[3]:
            self.did_win = True

        # Diagonals
        elif '' not in (icon_dict[7], icon_dict[5], icon_dict[3]) and icon_dict[7] == icon_dict[5] == icon_dict[3]:
            self.did_win = True
        elif '' not in (icon_dict[9], icon_dict[5], icon_dict[1]) and icon_dict[9] == icon_dict[5] == icon_dict[1]:
            self.did_win = True
        else:
            pass

        # If all spaces on the board are filled or player won
        return self.did_win or self.turn == 9

    def handle_win_loss(self):
        # End Game Notification
        if self.turn == 9 and self.did_win is False:
            print('Cat\'s game!')
        elif self.turn % 2 == 0:
            print('\nPlayer 2 has won!\n\n')
        else:
            print('\nPlayer 1 has won!\n\n')

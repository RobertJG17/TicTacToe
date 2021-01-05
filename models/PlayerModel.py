
class Player:

    def __init__(self, player_icon='', player_number=None, player_input=None):
        self.player_icon = player_icon
        self.player_number = player_number
        self.player_input = player_input

    def check_logic(self, icon_dict):
        valid = False

        while not valid:

            # Make sure the input is an Integer Value
            try:
                self.player_input = int(self.player_input)
            except ValueError:
                print('\nInvalid entry')
                self.player_input = input('Player {}, please enter a number (1 - 9) to input '
                                          'an {} in the corresponding location:\n'.format(self.player_number,
                                                                                          self.player_icon))
                continue

            # Make sure they enter a number between 1-10
            if self.player_input not in range(1, 10):
                self.player_input = input('Player {} out of range index, please enter a number (1 - 9) to input '
                                          'an {} in the corresponding location:\n'.format(self.player_number,
                                                                                          self.player_icon))
                continue

            # Make sure that cell is not already taken
            if icon_dict[self.player_input] != '':
                print('That cell has already been taken, please choose a valid cell!\n')
                self.player_input = input('Player {}, please enter a number (1 - 9) to input '
                                          'an {} in the corresponding location:\n'.format(self.player_number,
                                                                                          self.player_icon))
                continue

            valid = True

        return self.player_input

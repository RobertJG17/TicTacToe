from models.BoardModel import Board
from models.PlayerModel import Player
import time
import pygame


# Helper Functions
def player_select(player1, player2):
    while player1.player_icon not in ('X', 'O'):
        # player1.player_icon = input('Player 1, Do you want to be X or O?: ').upper()
        # player1.player_icon.replace(" ", "")

        if player2.player_icon == 'X':
            player2.player_icon = 'O'
        else:
            player2.player_icon = 'X'

    print('\nPlayer 1 --> {} <-- will go first\n\n'.format(player1.player_icon))
    print('Please wait for the screen to display')

    time.sleep(3.75)
    print('{}'.format('\n') * 20)


def player_move(player, icon_dict):
    player.player_input = input('Player {}, please enter a number (1 - 9) to input '
                                'an {} in the corresponding location:\n'.format(player.player_number,
                                                                                player.player_icon))
    player.check_logic(icon_dict)
    icon_dict[player.player_input] = player.player_icon


def start_game():
    # START
    game_res = (600, 600)
    x_o_screen = pygame.display.set_mode(game_res)
    pygame.display.set_caption('Tic Tac Toe: Game Time')
    pygame.display.set_mode(game_res)
    background_color = (28, 170, 156)
    white = (255, 255, 255)
    line_color = (23, 145, 135)
    circle_color = (240, 231, 200)
    cross_color = (75, 75, 85)
    width = 600
    height = 600
    line_width = 15
    square_size = 200  # square size is

    x_o_screen.fill(background_color)

    # defining font
    small_font = pygame.font.SysFont('Corbel', 35)

    # screen text
    welcome = small_font.render("Welcome", True, white)
    ask_user = small_font.render('Player 1, Do you want to be X or O?', True, white)

    # superimpose onto screen
    x_o_screen.blit(welcome, (600 // 3 + 25, 600 / 2 - 200))
    x_o_screen.blit(ask_user, (600 // 3 - 150, 600 / 2 - 100))

    #
    # draw box1
    #
    # 1 vertical
    pygame.draw.line(x_o_screen, line_color, (square_size - 100, square_size + 100),
                     (square_size - 100, square_size + 300), line_width)
    # 2 vertical
    pygame.draw.line(x_o_screen, line_color, (square_size + 50, square_size + 100),
                     (square_size + 50, square_size + 300), line_width)

    # 1 horizontal
    pygame.draw.line(x_o_screen, line_color, (square_size - 107, square_size + 100),
                     (square_size + 57, square_size + 100), line_width)
    # 2 horizontal
    pygame.draw.line(x_o_screen, line_color, (square_size - 107, square_size + 300),
                     (square_size + 57, square_size + 300), line_width)

    # draw x for box1
    pygame.draw.line(x_o_screen, cross_color, (square_size - 80, square_size + 150),
                     (square_size + 40, square_size + 245), line_width)
    pygame.draw.line(x_o_screen, cross_color, (square_size + 30, square_size + 150),
                     (square_size - 80, square_size + 245), line_width)

    #
    # draw box2 #
    #
    # 1 horizontal
    pygame.draw.line(x_o_screen, line_color, (square_size + 120, square_size + 100),
                     (square_size + 270, square_size + 100), line_width)
    # 2 horizontal
    pygame.draw.line(x_o_screen, line_color, (square_size + 120, 2 * square_size + 100),
                     (square_size + 270, 2 * square_size + 100), line_width)

    # 1 vertical
    pygame.draw.line(x_o_screen, line_color, (square_size + 125, square_size + 93), (square_size + 125, 507),
                     line_width)
    # 2 vertical
    pygame.draw.line(x_o_screen, line_color, (square_size + 275, square_size + 93), (square_size + 275, 507),
                     line_width)

    # draw O for box2
    pygame.draw.circle(x_o_screen, circle_color, (400, 400), 50, 15)

    pygame.display.update()

    restart = 'y'

    # Start/Restart Game
    while restart.lower() == 'y':
        # Player/Board Instances
        player1 = Player(player_number=1)
        player2 = Player(player_number=2)

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

# PART ONE #

# to start
import pygame
import sys

# initialize pygame
pygame.init()

# set constants for screen
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

# create the screen (at this point we have a screen but will go away since there is main loop)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND_COLOR)

# add a title to your screen
pygame.display.set_caption('Tic Tac Toe')


# draw lines

def draw_lines():
    # 1 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2 horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # 1 vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2 vertical
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # update the screen
    pygame.display.update()

# PART TWO #


# Board
board = numpy.zeros((BOARD_ROWS, BOARD_COLS))
print(board)


# create functionality for board #

# create function 'mark square'
def mark_square(row, col, player):
    board[row][col] = player


# check if square is empty
def available_square(row, col):
    return board[row][col] == 0


# check if board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False


# PART THREE #

# create more constants
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 50
CROSS_COLOR = (75, 75, 85)

CIRCLE_COLOR = (240, 231, 200)


# Create X's and O's
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100),
                                                          int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

        # Create the logic for MOUSEBUTTONDOWN #

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            # print(clicked_row)
            # print(clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1

                draw_figures()


# PART FOUR #


# create the check win functions


# win Function
def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # asc_diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # desc_diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False


# Draw Winning Vertical Line
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


# Draw Winning Horizontal line
def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


# Draw / diagonal line
def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


# Draw \ diagonal line
def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


# Create Restart Function
def restart():
    screen.fill(BACKGROUND_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

            # update the available square logic to include the check win function

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                # if player == 1:
                #   mark_square(clicked_row, clicked_col, 1)
                #   if check_win(player):
                #       game_over = True
                #   player = 2
                # elif player == 2:
                #   mark_square(clicked_row, clicked_col, 2)
                #   if check_win(player):
                #       game_over = True
                #   player = 1
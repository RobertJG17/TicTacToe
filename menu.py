import pygame
from main import *
from helper import *


def load_menu():
    # initializing the constructor
    pygame.init()

    # screen resolution
    res = (720, 720)

    # opens up a window
    screen = pygame.display.set_mode(res)

    # white color
    color = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

    # stores the width of the
    # screen into a variable
    width = screen.get_width()

    # stores the height of the
    # screen into a variable
    height = screen.get_height()

    # defining a font
    small_font = pygame.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    title = small_font.render("**   WELCOME TO TIC-TAC-TO   **", True, color)
    play = small_font.render('play', True, color)
    text = small_font.render('quit', True, color)

    while True:

        pygame.draw.rect(screen, color_light, [width / 8 + 25, height / 8 + 40, 140, 40])

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    pygame.quit()
                elif width / 4 + 100 <= mouse[0] and height / 4 + 100 <= mouse[1]:
                    player_select(player1, player2)

                    # fills the screen with a color
        screen.fill((25, 25, 255))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 4 + 100, height / 2, 140, 40])
        else:
            pygame.draw.rect(screen, color_dark, [width / 4 + 100, height / 3 + 40, 140, 40])
            #pygame.draw.rect(screen, color_dark, [width / 4 + 100, height / 2, 140, 40])

            # superimposing the text onto our button
        screen.blit(title, (width / 8 + 25, height / 8 + 40, 140, 40))
        screen.blit(play, (width / 4 + 100, height / 4 + 100))
        screen.blit(text, (width / 4 + 100, height / 2))

        # updates the frames of the game
        pygame.display.update()

"""TIC TAC TOE GAME"""
from views.select_view import start_game
from views.menu_view import load_menu
# from views.game_view import load_game
import pygame


# initialize pygame
pygame.init()

# screen resolution
res = (600, 600)

# opens up a welcome Window
screen = pygame.display.set_mode(res)
pygame.display.set_caption('Tic Tac Toe: by Bobby & Dad')
pygame.display.update()

# call load_menu method
load_menu(screen)

# call game start method
start_game(screen)

# commented out 2-6-21
# load in game assets
#load_game(screen)



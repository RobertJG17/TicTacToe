"""TIC TAC TOE GAME"""
from game_start import start_game
from menu import load_menu
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
start_game()


"""TIC TAC TOE GAME"""
from game_start import start_game
from menu import load_menu
import pygame

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# call load_menu method
load_menu(screen)

# call game start method
start_game()


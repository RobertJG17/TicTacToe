import pygame


def load_menu(scr):

    # white color
    white = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # stores the width of the
    # screen into a variable
    width = scr.get_width()

    # stores the height of the
    # screen into a variable
    height = scr.get_height()

    print(width, height)

    # defining a font
    small_font = pygame.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    welcome = small_font.render("   Welcome To ", True, white)
    title = small_font.render("TIC-TAC-TOE!", True, white)
    play_button = small_font.render('play', True, white)
    quit_button = small_font.render('quit', True, white)

    did_press_play = False
    mouse = None

    while not did_press_play:

        pygame.draw.rect(scr, color_light, [width / 8 + 25, height / 8 + 40, 140, 40])

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated

                # if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                #     pygame.quit()

                # PLAY BUTTON
                if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 55 <= mouse[1] <= height / 2 - 15:
                    did_press_play = True

                # QUIT BUTTON
                elif width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 5 <= mouse[1] <= height / 2 + 35:
                    pygame.quit()
                # elif width / 4 + 100 <= mouse[0] and height / 4 + 100 <= mouse[1]:
                #     player_select(player1, player2)

        # fills the screen with a color
        scr.fill((28, 170, 156))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 5 <= mouse[1] <= height / 2 + 35:
            pygame.draw.rect(scr, color_light, [width / 2 - 70, height / 2 - 5, 140, 40])
        elif width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 55 <= mouse[1] <= height / 2 - 15:
            pygame.draw.rect(scr, color_light, [width / 2 - 70, height / 2 - 55, 140, 40])

        # superimposing the text onto our button
        scr.blit(welcome, (width / 8 + 120, height / 8 + 40, 140, 40))
        scr.blit(title, (width / 4 + 50, height / 4 + 20, 140, 40))
        scr.blit(play_button, (width / 2 - 25, height / 2 - 50))
        scr.blit(quit_button, (width / 2 - 25, height / 2))

        # updates the frames of the game
        pygame.display.update()

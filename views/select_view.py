import pygame


def start_game(scr):
    # START

    BACKGROUND_COLOR = (28, 170, 156)
    white = (255, 255, 255)
    line_color = (23, 145, 135)
    circle_color = (240, 231, 200)
    cross_color = (75, 75, 85)
    color_light = (170, 170, 170)
    line_width = 15
    square_size = 200  # square size is
    mouse = None

    # scr.fill(BACKGROUND_COLOR)

    # defining font
    small_font = pygame.font.SysFont('Corbel', 35)

    # screen text
    welcome = small_font.render("Welcome", True, white)
    ask_user = small_font.render('Player 1, Do you want to be X or O?', True, white)

    test_select = False

    while not test_select:

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated

                # if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                #     pygame.quit()

                # X BUTTON
                if square_size - 92 <= mouse[0] <= square_size + 42 and square_size + 108 <= mouse[1] <= square_size + 292 or\
                        square_size + 133 <= mouse[0] <= square_size + 267 and square_size + 108 <= mouse[1] <= square_size + 292:
                    test_select = True

            scr.fill(BACKGROUND_COLOR)

            # Grabbing mouse coordinates
            mouse = pygame.mouse.get_pos()

            # superimpose onto screen
            scr.blit(welcome, (600 // 3 + 25, 600 / 2 - 200))
            scr.blit(ask_user, (600 // 3 - 150, 600 / 2 - 100))

            # Create Light Boxes around selection areas
            if square_size - 92 <= mouse[0] <= square_size + 42 and square_size + 108 <= mouse[1] <= square_size + 292:
                pygame.draw.rect(scr, color_light, [square_size - 92, square_size + 108, 135, 187])
            elif square_size + 133 <= mouse[0] <= square_size + 267 and square_size + 108 <= mouse[1] <= square_size + 292:
                pygame.draw.rect(scr, color_light, [square_size + 133, square_size + 108, 135, 187])

            #
            # draw box1
            #
            # 1 vertical
            pygame.draw.line(scr, line_color, (square_size - 100, square_size + 100),
                             (square_size - 100, square_size + 300), line_width)
            # 2 vertical
            pygame.draw.line(scr, line_color, (square_size + 50, square_size + 100),
                             (square_size + 50, square_size + 300), line_width)

            # 1 horizontal
            pygame.draw.line(scr, line_color, (square_size - 107, square_size + 100),
                             (square_size + 57, square_size + 100), line_width)
            # 2 horizontal
            pygame.draw.line(scr, line_color, (square_size - 107, square_size + 300),
                             (square_size + 57, square_size + 300), line_width)

            # draw x for box1
            pygame.draw.line(scr, cross_color, (square_size - 80, square_size + 150),
                             (square_size + 30, square_size + 245), line_width)
            pygame.draw.line(scr, cross_color, (square_size + 30, square_size + 150),
                             (square_size - 80, square_size + 245), line_width)

            #
            # draw box2 #
            #
            # 1 horizontal
            pygame.draw.line(scr, line_color, (square_size + 120, square_size + 100),
                             (square_size + 270, square_size + 100), line_width)
            # 2 horizontal
            pygame.draw.line(scr, line_color, (square_size + 120, 2 * square_size + 100),
                             (square_size + 270, 2 * square_size + 100), line_width)

            # 1 vertical
            pygame.draw.line(scr, line_color, (square_size + 125, square_size + 93), (square_size + 125, 507),
                             line_width)
            # 2 vertical
            pygame.draw.line(scr, line_color, (square_size + 275, square_size + 93), (square_size + 275, 507),
                             line_width)

            # draw O for box2
            pygame.draw.circle(scr, circle_color, (400, 400), 50, 15)

            # if mouse is hovered on a button it
            # changes to lighter shade

            pygame.display.update()

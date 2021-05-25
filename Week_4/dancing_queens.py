import pygame
from queen_sprite import QueenSprite


def draw_board(the_board):
    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]

    n = len(the_board)
    surface_size = 480
    square_size = surface_size // n
    surface_size = n * square_size

    surface = pygame.display.set_mode((surface_size, surface_size))

    queen = pygame.image.load("queen.png")
    queen = pygame.transform.scale(queen, (square_size, square_size))

    all_sprites = []

    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(queen, (col * square_size, row * square_size))
        all_sprites.append(a_queen)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = event.dict["pos"]
            # print(posn_of_click)

            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break

        for sprite in all_sprites:
            sprite.update()

        for row in range(n):
            color_index = row % 2
            for col in range(n):
                the_square = (col * square_size, row * square_size, square_size, square_size)
                surface.fill(colors[color_index], the_square)
                color_index = (color_index + 1) % 2

        # for col, row in enumerate(the_board):
        #     surface.blit(queen, (col * square_size, row * square_size))
        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit()


draw_board([6, 4, 2, 0, 5, 7, 1, 3])


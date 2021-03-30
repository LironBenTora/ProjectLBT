import pygame
from grid import Grid

import os   # window position controler
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'


surface = pygame.display.set_mode((600, 600))    # The surface of the game
pygame.display.set_caption('Tic-tac-toe')   # The name of the surface

grid = Grid()


running = True
player = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # When to start or quit the game
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                if player == "X":
                    player = "O"
                else:
                    player = "X"

                grid.print_grid()

    surface.fill((0, 0, 0))

    grid.draw(surface)

    pygame.display.flip()

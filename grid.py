import pygame
import os

letterX = pygame.image.load(os.path.join('res', 'letterX.png'))
letterO = pygame.image.load(os.path.join('res', 'letterO.png'))


class Grid:
    def __init__(self):
        self.grid_lines = [((0, 200), (600, 200)),    # first horizontal line
                           ((0, 400), (600, 400)),    # second horizontal line
                           ((200, 0), (200, 600)),    # first vertical line
                           ((400, 0), (400, 600))]    # second vertical line

        self.grid = [[0 for x in range(3)] for y in range(3)]



    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

            for y in range(len(self.grid)):
                for x in range(len(self.grid[y])):
                    if self.get_cell_value(x, y) == "X":
                        surface.blit(letterX, (x*200, y*200))
                    elif self.get_cell_value(x, y) == "O":
                        surface.blit(letterO,(x*200, y*200))


    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse(self, x, y, player):
        if player == "X":
            self.set_cell_value(x, y, "X")
        elif player == "O":
            self.set_cell_value(x, y, "O")


    def print_grid(self):
        for row in self.grid:
            print(row)

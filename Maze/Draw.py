import pygame
from Maze import Draw

white = (255, 255, 255)
black = (0, 0, 0)
green = (4, 243, 64)
red = (250, 15, 15)
blue = (26, 182, 255)
pink = (255, 100, 150)
yellow = (238, 243, 90)
blue_a_little_darker = (1, 4, 239)


# x-axis - width - column
# y-axis - height - row

def draw_rectangle_with_border(screen, color, coordinates):
    x, y, dist1, dist2 = coordinates
    pygame.draw.rect(screen, color, (x + 4, y + 4, dist1 - 4, dist2 - 4))


def draw_board(screen, maze, dimension, dist):
    width, height = dimension

    maze.matrix[maze.start[0]][maze.start[1]].color = Draw.green

    for x in range(0, width, dist):
        for y in range(0, height, dist):
            draw_rectangle_with_border(screen, maze.matrix[x // dist][y // dist].color,
                                       (x, y, dist, dist))

    pygame.display.update()


def clear(maze, dimension, dist):
    width, height = dimension
    for x in range(0, width, dist):
        for y in range(0, height, dist):
            maze.matrix[x // dist][y // dist].color = white


def back(maze, dimension, dist):
    width, height = dimension
    for x in range(0, width, dist):
        for y in range(0, height, dist):
            if maze.matrix[x // dist][y // dist].color == blue or \
                    maze.matrix[x // dist][y // dist].color == pink:
                maze.matrix[x // dist][y // dist].color = white

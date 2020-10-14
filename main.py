from Maze import Maze
from Maze import Draw
import pygame
import ctypes
import sys


def main():
    pygame.init()
    pygame.display.set_caption('Maze Solver')

    icon = pygame.image.load('.\\images\\maze.png')
    pygame.display.set_icon(icon)

    width = 1000  # columns
    height = 800  # rows
    dist = 50

    dimension = (width, height)
    screen = pygame.display.set_mode(dimension)

    start = (0, 0)
    end = (width // dist - 1, height // dist - 1)

    maze = Maze.Maze(screen, width // dist, height // dist, start, end)

    Draw.draw_board(screen, maze, dimension, dist)

    solved = False

    colors = [Draw.green, Draw.red, Draw.white, Draw.black]

    Draw.draw_board(screen, maze, dimension, dist)

    pygame.display.update()

    clock = pygame.time.Clock()

    while not solved:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                solved = True
            elif keys[pygame.K_c]:
                Draw.clear(maze, dimension, dist)
                Draw.draw_board(screen, maze, dimension, dist)

            elif keys[pygame.K_s]:
                Draw.back(maze, dimension, dist)
                Draw.draw_board(screen, maze, dimension, dist)

                path = maze.lee(screen, dist)
                if path:
                    ctypes.windll.user32.MessageBoxW(0, f"Destination reached in {maze.matrix[end[0]][end[1]].data} steps!",
                                                     "Path Found!", 1)
                else:
                    ctypes.windll.user32.MessageBoxW(0, f"No path between {start[0]}, {start[1]} and {end[0]}, {end[1]}",
                                                     "Failed Search", 1)
            elif mouse[0]:
                x_click, y_click = pygame.mouse.get_pos()

                choice = 3

                if keys[pygame.K_g]:
                    choice = 0
                elif keys[pygame.K_r]:
                    choice = 1
                elif keys[pygame.K_w]:
                    choice = 2
                elif keys[pygame.K_b]:
                    choice = 3

                for x in range(0, width, dist):
                    for y in range(0, height, dist):
                        if x <= x_click <= x + dist and y <= y_click <= y + dist:
                            if choice == 0:
                                if maze.matrix[maze.start[0]][maze.start[1]].color == Draw.green:
                                    maze.matrix[maze.start[0]][maze.start[1]].color = Draw.white
                                maze.start = (x // dist, y // dist)
                            elif choice == 1:
                                if maze.matrix[maze.end[0]][maze.end[1]].color == Draw.red:
                                    maze.matrix[maze.end[0]][maze.end[1]].color = Draw.white
                                maze.end = (x // dist, y // dist)

                            maze.matrix[x // dist][y // dist].color = colors[choice]
                            break

                Draw.draw_board(screen, maze, dimension, dist)


            elif keys[pygame.K_b]:
                Draw.back(maze, dimension, dist)
                Draw.draw_board(screen, maze, dimension, dist)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

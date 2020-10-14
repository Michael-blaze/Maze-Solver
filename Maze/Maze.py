import queue
import pygame
from Maze import Draw
from Linked_List import Linked_List


class Maze:
    dir_x = [1, 0, -1, 0]
    dir_y = [0, 1, 0, -1]
    dir = 4

    def __init__(self, screen, x_max, y_max, start, end):
        self.screen = screen
        self.x_max = x_max
        self.y_max = y_max
        self.start = start
        self.end = end
        self.matrix = self.create_matrix(self.x_max, self.y_max)

    # self.matrix[x][y] = top left (x, y)
    def create_matrix(self, x_max, y_max):
        matrix = []

        for x in range(x_max + 2):
            temp = []
            for y in range(y_max + 2):
                temp.append(Linked_List.Node(color=Draw.white))
            matrix.append(temp)

        matrix[self.start[0]][self.start[1]].color = Draw.green
        matrix[self.end[0]][self.end[1]].color = Draw.red
        return matrix

    def is_obstacle(self, x, y):
        return self.matrix[x][y].color == Draw.black or self.matrix[x][y].color == Draw.blue or self.matrix[x][y].color == Draw.yellow or \
                self.matrix[x][y].color == Draw.green

    def is_valid_move(self, x, y):
        if x >= self.x_max or x < 0:
            return False
        if y >= self.y_max or y < 0:
            return False

        if self.is_obstacle(x, y):
            return False

        return True

    def lee(self, screen, dist):
        matrix = self.matrix

        x_start, y_start = self.start
        x_end, y_end = self.end

        matrix[x_start][y_start].data = 1

        dim = pygame.display.get_surface().get_size()

        matrix[x_start][y_start].x = x_start
        matrix[x_start][y_start].y = y_start

        q = queue.Queue()
        q.put([x_start, y_start])

        ok = True

        while not q.empty() and ok:
            x, y = q.get()

            for k in range(Maze.dir):
                next_x = x + Maze.dir_x[k]
                next_y = y + Maze.dir_y[k]

                if self.is_valid_move(next_x, next_y):
                    q.put([next_x, next_y])

                    matrix[next_x][next_y].data = matrix[x][y].data + 1

                    matrix[next_x][next_y].color = Draw.yellow

                    matrix[next_x][next_y].x = next_x
                    matrix[next_x][next_y].y = next_y

                    matrix[next_x][next_y].next = matrix[x][y]

                    if next_x == x_end and next_y == y_end:
                        ok = False
                        break

            matrix[x][y].color = Draw.blue
            Draw.draw_board(screen, self, dim, dist)
            
	
        if matrix[x_end][y_end].color == Draw.red:
            return False

        temp = matrix[x_end][y_end]

        while temp.next is not None:
            self.matrix[temp.x][temp.y].color = Draw.pink
            temp = temp.next

        matrix[x_start][y_start].color = Draw.green
        matrix[x_end][y_end].color = Draw.red

        Draw.draw_board(screen, self, dim, dist)

        return True

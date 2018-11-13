import random
import pygame
from tile import Tile 
from pygame.locals import *


class Labyrinthe:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.canvas = [
            [Tile() for j in range(self.column)]
            for _ in range(self.row)
        ]
        self.draw_labyrinthe()


    def draw_labyrinthe(self):
        for line in range(self.row):
            for row in range(self.column):
                random_number = random.randint(0, 15)
                if random_number == 0:
                    self.canvas[line][row].tile_type = 'wall'
                elif random_number == 1 or random_number == 2:
                    self.canvas[line][row].tile_type = 'water'
                elif random_number >= 3 and random_number <= 7:
                    self.canvas[line][row].tile_type = 'floor'
                else:
                    self.canvas[line][row].tile_type = 'floor'
        
        return self.canvas

    def is_mouvable(self, x, y):
        if self.canvas[x][y].tile_type != 'floor':
            return True
        else:
            return False




    def __str__(self):
        l = ""
        for line in self.canvas:
            for row in line:
                l += str(row) + "  "
            l += '\n'
        return l

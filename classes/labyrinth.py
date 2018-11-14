import random
import pygame
from tile import Tile 
from pygame.locals import *



class Labyrinth:
    def __init__(self, pattern_file):
        self.pattern = pattern_file
        self.canvas = []
        self.draw()

    def draw(self):
        with open(self.pattern, "r") as file:
            for line in file:
                line_list = []
                for row in line:
                    if row != '\n':
                        if row == '0':
                            tile = Tile()
                        elif row == 'W':
                            tile = Tile(tile_type='water')
                        line_list.append(tile)
                self.canvas.append(line_list)
            return self.canvas
    
    def __str__(self):
        l = ""
        for line in self.canvas:
            for row in line:
                l += str(row) + "  "
            l += '\n'
        return l

import random
import pygame
from tile import Tile
from lab_item import LabItem
from pygame.locals import *



class Labyrinth:
    def __init__(self, pattern_file):
        self.pattern = pattern_file
        self.height = 15
        self.width = 15
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

    def move_player(self, player):
        pass

    def add_random_items(self, num_item):
        self.list_item = []
        for i in range(num_item):
            item = LabItem(item_type='object')
            item.x = random.randint(0,self.width - 1)
            item.y = random.randint (0,self.height - 1)
            if item.x == 0 and item.y == 0 or item.x == 5 and item.y == 5:
                item.x = random.randint (0, self.width - 1)
                item.y = random.randint (0, self.height - 1)
            if self.canvas[item.x][item.y].tile_type != 'floor':
                item.x = random.randint (0, self.width - 1)
                item.y = random.randint (0, self.height - 1)
            self.canvas[item.x][item.y].add_lab_item(item)

            self.list_item.append(item)

    def is_item(self, x, y):
        if self.canvas[x][y].tile_type == 'item':
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

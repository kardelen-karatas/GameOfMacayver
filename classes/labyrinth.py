import random
import pygame
from classes.tile import Tile
from classes.lab_item import LabItem
from pygame.locals import *


class InvalidPattern(Exception):
    pass


class Labyrinth:
    """
    Labyrinth of the game. It has 15 rows, 15 columns and is composed of the F and W. F represents the floor, W represents water.  
    """
    def __init__(self, pattern_file):
        self.pattern = pattern_file
        self.height = 0
        self.width = 0
        self.canvas = []
        self.draw()

    def draw(self):
        """
        Read the file that contains the labyrinth pattern and draw the canvas of the labyrinth if the pattern if valid.
        Returns:
            canvas (list): the canvas of the labyrinth
        Raises:
            InvalidPattern: the pattern of the labyrinth does not correspond to he requests 
        """
        if self.is_pattern_valid():
            with open(self.pattern, "r") as file:
                for line in file:
                    line = line.rstrip()
                    self.height = len(line)
                    line_list = []
                    for col in line:
                        if col == 'F':
                            tile = Tile()
                        elif col == 'W':
                            tile = Tile(tile_type='water')
                        elif col == 'G':
                            tile = Tile(tile_type='guard')
                        line_list.append(tile)
                    self.width = len(line_list)
                    self.canvas.append(line_list)
                return self.canvas   
        else: 
            raise InvalidPattern("invalid labyrinth pattern")

    def is_pattern_valid(self):
        """
        Check if uploaded pattern file is valid
        """
        with open(self.pattern, "r") as file:
            for i, line in enumerate(file):
                for j, col in enumerate(line):
                    if col != '\n':
                        if col not in ('F', 'G', 'W'):
                            return False
                        elif i == 14 and j == 14 and col != 'G':
                            return False
                        elif i == 0 and j == 0 and col != 'F':
                            return False
        return True 

    def add_random_items(self, num_item):
        """
        Distibute items randomly on the labyrinth with a given quantity. 
        Args: 
            num_item (int): quantity of items that will be distributed on the labyrinth
        """
        self.list_item = []
        for i in range(num_item):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            item = LabItem(item_type='object', x=x, y=y)
            while not (item.x == 0 and item.y == 0 or item.x == self.width - 1 and item.y == self.height - 1) and self.canvas[item.x][item.y].tile_type != 'floor':
                item.x = random.randint(0, self.width - 1)
                item.y = random.randint(0, self.height - 1)
            self.canvas[item.x][item.y].add_lab_item(item)
            self.list_item.append(item)

    def is_winner(self, player):
        """
        Check if the player is in front of the door and picked up all the items. 
        Args: 
            player (Player): the player of the game
        """
        if player.counter == len(self.list_item) and self.in_front_of_guard(player):
            return True
        elif player.counter < len(self.list_item) and self.in_front_of_guard(player):
            return False
    
    def in_front_of_guard(self, player):
        """
        Check if the player is in front of the door. 
        Args: 
            player (Player): the player of the game
        """
        if player.x == self.width - 2 and player.y == self.height - 1:
            return True
        return False

    def __str__(self):
        l = ""
        for line in self.canvas:
            for col in line:
                l += str(col) + "  "
            l += '\n'
        return l

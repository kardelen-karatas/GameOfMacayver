import random
import pygame
from pygame.locals import *



class LabItem:
    def __init__(self, item_type = 'player'):
        self.x = 0
        self.y = 0
        self.item_type = item_type

    def move_right(self):
        self.x += 1
    
    def move_left(self):
        self.x -= 1
    
    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1
    
    def __str__(self):
        return "{}, {}, {}".format(self.item_type, self.x, self.y) 


# class Guard(LabObject):
#     def __init__(self, type = 'guard'):
#         super().__init__()

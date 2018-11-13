import time
from tile import Tile
from lab_item import LabItem
from labyrinthe import Labyrinthe
import pygame
import sys
from pygame.locals import *


class Game:
    def __init__(self):
        self.tile_images = {
            'floor': pygame.image.load('../../tuto/pics/green.png'),
            'wall': pygame.image.load('../../tuto/pics/grey.png'),
            'water': pygame.image.load('../../tuto/pics/blue.png'),
            #'dirt': pygame.image.load('../../tuto/pics/brown.png'),
        }

        self.item_images = {
            'player': pygame.image.load('../../tuto/pics/octopus.png'),
        }

        self.width = 15
        self.height = 15
        self.tile_size = 20
        self.labyrinthe = Labyrinthe(self.width, self.height)
        self.labyrinthe.draw_labyrinthe()

        self.player = LabItem()
        self.labyrinthe.canvas[self.player.x][self.player.y].add_lab_item(self.player) 

        self.display_surface = pygame.display.set_mode(
            (self.width * self.tile_size, self.height * self.tile_size))

    def display_tiles(self):
        for line in range(self.width):
            for column in range(self.height):
                tile = self.labyrinthe.canvas[line][column]
                self.display_surface.blit(
                    self.tile_images[tile.tile_type], (line * self.tile_size, column * self.tile_size))
#                print(tile.lab_item)
#                time.sleep(1.5)
                if tile.lab_item:
                    self.display_surface.blit(self.item_images[self.player.item_type], (self.player.x * self.tile_size, self.player.y * self.tile_size))

        pygame.display.flip()                    
                

    def run(self):
        # clock = pygame.time.Clock()
        while True:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    tiles = self.labyrinthe.canvas
                    if (event.key == K_RIGHT) and self.player.x < self.width - 1 and tiles[self.player.x+1][self.player.y].tile_type != 'water':
                        self.player.move_right()
                        tiles[self.player.x][self.player.y].add_lab_item(self.player)

                    if (event.key == K_LEFT) and self.player.x !=0 :
                        self.player.move_left()
                        tiles[self.player.x][self.player.y].add_lab_item(self.player)

                    if (event.key == K_DOWN)  and self.player.y < self.height - 1:
                        self.player.move_down()
                        tiles[self.player.x][self.player.y].add_lab_item(self.player)
                        print(self.player.y)

                    if (event.key == K_UP) and self.player.y != 0:
                        self.player.move_up()
                        tiles[self.player.x][self.player.y].add_lab_item(self.player)
                        
            self.display_tiles()

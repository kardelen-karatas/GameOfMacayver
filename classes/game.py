import time
from tile import Tile
from lab_item import LabItem, Player
from labyrinth import Labyrinth
import pygame
import sys
from pygame.locals import *


class Game:
    def __init__(self):
        self.tile_images = {
            'floor': pygame.image.load('../../tuto/pics/green.png'),
            'water': pygame.image.load('../../tuto/pics/blue.png'),
            'gate': pygame.image.load('../../tuto/pics/black.png'),
        }

        self.item_images = {
            'player': pygame.image.load('../../tuto/pics/octopus.png'),
            'guard': pygame.image.load('../../tuto/pics/black.png'),
            'object': pygame.image.load('../../tuto/pics/perso.png'),
            #'item': pygame.image.load ('../../tuto/pics/plankton.png'),
        }

        self.tile_size = 20
        self.labyrinth = Labyrinth('pattern_file')
        self.width = self.labyrinth.width
        self.height = self.labyrinth.height

        self.player = Player()
        self.labyrinth.canvas[self.player.x][self.player.y].add_lab_item(
            self.player)
        self.guard = LabItem(
            item_type='guard', x=self.width - 1, y=self.height - 1)
        self.labyrinth.canvas[self.guard.x][self.guard.y].add_lab_item(
            self.guard)
        self.labyrinth.add_random_items(2)
        self.display_surface = pygame.display.set_mode(
            (self.width * self.tile_size, self.height * self.tile_size))

    def display_tiles(self):
        for line in range(self.height):
            for column in range(self.width):
                tile = self.labyrinth.canvas[line][column]
                self.display_surface.blit(
                    self.tile_images[tile.tile_type], (column * self.tile_size, line * self.tile_size))
                if tile.lab_item:
                    self.display_surface.blit(self.item_images[tile.lab_item.item_type], (
                        column * self.tile_size, line * self.tile_size))

        pygame.display.flip()

    def run(self):
        # clock = pygame.time.Clock()
        while True:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT or self.labyrinth.is_winner(self.player):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    tiles = self.labyrinth.canvas
                    if (event.key == K_RIGHT) and self.player.x < self.width - 1 and tiles[self.player.y][self.player.x + 1].tile_type == 'floor':
                        self.player.pick_up(tiles[self.player.y][self.player.x + 1])
                        self.player.move_right(tiles)
                        
                    if (event.key == K_LEFT) and self.player.x != 0 and tiles[self.player.y][self.player.x - 1].tile_type == 'floor':
                        self.player.pick_up(tiles[self.player.y][self.player.x - 1])
                        self.player.move_left(tiles)                    

                    if (event.key == K_DOWN) and self.player.y < self.height - 1 and tiles[self.player.y + 1][self.player.x].tile_type == 'floor':
                        self.player.pick_up(tiles[self.player.y + 1][self.player.x])
                        self.player.move_down(tiles)                           

                    if (event.key == K_UP) and self.player.y != 0 and tiles[self.player.y - 1][self.player.x].tile_type == 'floor':
                        self.player.pick_up(tiles[self.player.y - 1][self.player.x])
                        self.player.move_up(tiles)                       

                self.display_tiles()

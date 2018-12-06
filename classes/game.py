import pygame
from pygame.locals import *
from classes.lab_item import Player
from classes.labyrinth import Labyrinth, InvalidPattern
from config import Config


class Game:
    """
    Create the graphical environment of the game. It takes as a parameter a text file that contains the pattern
    Raise:
        IndexError: if the pattern does not composed of 15 lines and 15 columns
        InvalidPattern: the pattern of the labyrinth does not correspond to he requests 
    """

    def __init__(self, pattern_file):
        self.tile_images = {
            'floor': pygame.image.load(Config.get_image_path('green.png')),
            'water': pygame.image.load(Config.get_image_path('blue.png')),
            'guard': pygame.image.load(Config.get_image_path('guard.png')),
        }

        self.item_images = {
            'player': pygame.image.load(Config.get_image_path('octopus.png')),
            'item': pygame.image.load(Config.get_image_path('item.png')),
            'item0': pygame.image.load(Config.get_image_path('item0.png')),
            'item1': pygame.image.load(Config.get_image_path('item1.png')),
            'item2': pygame.image.load(Config.get_image_path('item2.png')),
        }
        self.tile_size = 60
        try:
            self.labyrinth = Labyrinth(Config.get_pattern_path(pattern_file))
            self.width = self.labyrinth.width
            self.height = self.labyrinth.height

            self.player = Player()
            self.labyrinth.canvas[self.player.x][self.player.y].add_lab_item(
                self.player)

            pygame.init()
            self.labyrinth.add_random_items(3)
            self.display_surface = pygame.display.set_mode(
                (self.width * self.tile_size, self.height * self.tile_size + self.tile_size))
            self.text_font = pygame.font.Font('freesansbold.ttf', 54)
        except (IndexError, InvalidPattern) as e:
            print('error: {}'.format(e))
            quit(0)
            # sys.exit(1)

    def display_tiles(self):
        """
        Display tile map of the labyrinth on the display screen.
        Raise:
            IndexError: if the pattern does not composed of 15 lines and 15 columns
        """
        try:
            for line in range(self.height):
                for column in range(self.width):
                    tile = self.labyrinth.canvas[line][column]
                    self.display_surface.blit(
                        self.tile_images[tile.tile_type], (column * self.tile_size, line * self.tile_size))
                    if tile.lab_item:
                        self.display_surface.blit(self.item_images[tile.lab_item.item_type], (
                            column * self.tile_size, line * self.tile_size))
        except IndexError:
            print('error: labyrinth size have to be 15 x 15.')
            quit(0)

    def display_text(self, text, color, text_place):
        """
        Display text on the display screen
        Args :
            text (str): text that wanted to be displayed.
            color (tuple): RGB codes of the text color.
            text_place (tuple): the coordinates in pixels of the text position on the screen. 
        """
        text_surface = pygame.Surface(
            (self.width * self.tile_size, self.tile_size))
        text_surface.fill((19, 157, 255))
        text_render = self.text_font.render(text, True, color)
        self.display_surface.blit(
            text_surface, (0, self.height * self.tile_size))
        self.display_surface.blit(text_render, text_place)

    def footer(self):
        """ 
        Display number of collected item on the screen   
        """
        text = ' X ' + str(self.player.counter)
        text_position = (self.tile_size, self.height * self.tile_size)
        self.display_text(text, (0, 0, 0), text_position)
        self.display_surface.blit(
            self.item_images['item'], (0, self.height * self.tile_size))

    def game_loop(self):
        """
        Run the game on the display screen 
        """
        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_exit = True

                elif event.type == KEYDOWN:
                    tiles = self.labyrinth.canvas
                    if (event.key == K_RIGHT) and self.player.x < self.width - 1 \
                            and tiles[self.player.y][self.player.x + 1].tile_type == 'floor':
                        self.player.pick_up(
                            tiles[self.player.y][self.player.x + 1])
                        self.player.move_right(tiles)

                    if (event.key == K_LEFT) and self.player.x != 0 \
                            and tiles[self.player.y][self.player.x - 1].tile_type == 'floor':
                        self.player.pick_up(
                            tiles[self.player.y][self.player.x - 1])
                        self.player.move_left(tiles)

                    if (event.key == K_DOWN) and self.player.y < self.height - 1 \
                            and tiles[self.player.y + 1][self.player.x].tile_type == 'floor':
                        self.player.pick_up(
                            tiles[self.player.y + 1][self.player.x])
                        self.player.move_down(tiles)

                    if (event.key == K_UP) and self.player.y != 0 \
                            and tiles[self.player.y - 1][self.player.x].tile_type == 'floor':
                        self.player.pick_up(
                            tiles[self.player.y - 1][self.player.x])
                        self.player.move_up(tiles)

                self.display_tiles()
                self.footer()

                if self.labyrinth.items_collected(self.player) and self.labyrinth.in_front_of_guard(self.player):
                    self.display_text("YOU WON", (255, 0, 0), ((
                        self.height * self.tile_size)/2, (self.width * self.tile_size)/2))
                    game_exit = True

                if not self.labyrinth.items_collected(self.player) and self.labyrinth.in_front_of_guard(self.player):
                    self.display_text("GAME OVER", (255, 0, 0), ((
                        self.height * self.tile_size)/2, (self.width * self.tile_size)/2))
                    game_exit = True

                pygame.display.flip()
                pygame.time.Clock().tick(30)

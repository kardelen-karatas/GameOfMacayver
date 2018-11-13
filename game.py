"""
Openclassrooms Project no:3
Model of MacGayver's Labyrinth Game
Author: Kardelen Karatas
Date: 23 october 2018
"""
import random


class Lab:

    def __init__(self, rows, columns, wall, floor):
        self._game_over = False
        self._player = None
        self._moving_object = None
        self._guard = None
        self._rows = rows
        self._columns = columns
        self._wall = wall
        self._floor = floor
        self._lab = [
            [self._floor for j in range(self._columns)]
            for _ in range(self._rows)
        ]
        self.build_wall()

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns

    def wall(self):
        return self._wall

    def build_wall(self):

        for i in range(self._rows):

            if i == 0 or i == self._rows - 1:
                self._lab[i] = [self._wall for _ in self._lab[i]]
            else:
                self._lab[i][0] = self._wall
                self._lab[i][-1] = self._wall

        return self._lab

    def add_guard(self, guard):
        self._guard = guard
        guard_y = random.randint(0, self._rows - 1)
        if guard_y == self._rows - 1 or guard_y == 0:
            guard_x = random.randint(1, self._columns - 2)
            self._lab[guard_y][guard_x] = self._guard.symbol()
        else:
            guard_x = random.randrange(0, self._columns, self._columns - 1)
            self._lab[guard_y][guard_x] = self._guard.symbol()
        return self._lab

    def add_moving_object(self, moving_object):

        self._moving_object = moving_object
        if self._lab[moving_object.y()][moving_object.x()] == self._floor:
            self._lab[moving_object.y()][moving_object.x()
                                         ] = moving_object.symbol()
        else:
            pass
        return self._lab

    def add_player(self, player):
        self._player = player
        self._lab[player.y()][player.x()] = player.symbol()
        return self._lab

    def move_player(self, dest_x, dest_y):

        if not self._update_game_state(dest_x, dest_y):
            if not self._is_wall(dest_x, dest_y):
                self._lab[self._player.y()][self._player.x()] = self._floor
                self._lab[dest_y][dest_x] = self._player.symbol()
                self._player.set_coords(dest_x, dest_y)

    def _is_wall(self, dest_x, dest_y):
        if self._lab[dest_y][dest_x] == self._wall:
            return True

    def _is_object(self, dest_x, dest_y):
        if self._lab[dest_y][dest_x] == self._moving_object:
            return True

    def _update_game_state(self, dest_x, dest_y):
        if self._lab[dest_y][dest_x] == self._guard.symbol():
            self._game_over = True
        else:
            self._game_over = False

    def __str__(self):
        return '\n'.join([repr(l) for l in self._lab])


class Player:
    def __init__(self, x, y, symbol, lab):
        self._x = x
        self._y = y
        self._symbol = symbol
        self._lab = lab

    def x(self):
        return self._x

    def y(self):
        return self._y

    def set_coords(self, x, y):TILE_IMAGES = {
    'floor': './images/floor.png'
    'wall': './images/wall.png'
}

class Tile():
    
    def __init__(self, type):
        self._type = type

        self._x, self._y = x, yTILE_IMAGES = {
    'floor': './images/floor.png'
    'wall': './images/wall.png'
}

class Tile():
    
    def __init__(self, type):
        self._type = type


    def symbol(self):
        return self._symbol

    def move_right(self):
        self._lab.move_player(self._x + 1, self._y)

    def move_left(self):
        self._lab.move_player(self._x - 1, self._y)

    def move_down(self):
        self._lab.move_player(self._x, self._y + 1)
        return self._x, self._y + 1

    def move_up(self):
        self._lab.move_player(self._x, self._y - 1)


class MovingObject:
    def __init__(self, symbol):
        self._x = random.randint(2, 9)
        self._y = random.randint(2, 9)
        self._symbol = symbol

    def x(self):
        return self._x

    def y(self):
        return self._y

    def symbol(self):
        return self._symbol


class Guard:
    def __init__(self, symbol):
        self._symbol = symbol

    def symbol(self):
        return self._symbol

"""
Openclassrooms Project no:3
Model of MacGayver's Labyrinth Game
Author: Kardelen Karatas
Date: 23 october 2018 
"""
import random


class Lab:

    def __init__(self, rows, columns, wall):
        self._player = None
        self._moving_object = None
        self._rows = rows
        self._columns = columns
        self._wall = wall
        self._lab = [
            [" "for j in range(self._columns)]
            for _ in range(self._rows)
        ]

    def rows(self):
        return self._rows

    def wall(self):
        return self._wall

    def create_lab(self, guard):

        for i in range(self._rows):

            if i == 0 or i == self._rows - 1:
                self._lab[i] = [self._wall for _ in self._lab[i]]
            else:
                self._lab[i][0] = self._wall
                self._lab[i][-1] = self._wall

        guard_y = random.randint(0, self._rows - 1)
        if guard_y == self._rows - 1 or guard_y == 0:
            guard_x = random.randint(1, self._columns - 1)
            self._lab[guard_y][guard_x] = guard
        else:
            guard_x = random.randrange(0, self._columns, self._columns - 1)
            self._lab[guard_y][guard_x] = guard

        return self._lab

    def add_moving_object(self, moving_object):

        self._moving_object = moving_object
        if self._lab[moving_object.y()][moving_object.x()] == ' ':
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
        if self._is_wall(dest_x, dest_y):
            return
        self._lab[self._player.y()][self._player.x()] = " "
        self._lab[dest_y][dest_x] = self._player.symbol()

    def _is_wall(self, dest_x, dest_y):
        if self._lab[dest_y][dest_x] == self._wall:
            print("Danger for y : {}, x : {}".format(dest_y, dest_x))
            return True

    def counter(self):
        pass

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

    def symbol(self):
        return self._symbol

    def move_right(self):
        self._lab.move_player(self._x + 1, self._y)
        self._x += 1

    def move_left(self):
        self._lab.move_player(self._x - 1, self._y)
        self._x -= 1

    def move_down(self):
        self._lab.move_player(self._x, self._y + 1)
        self._y += 1

    def move_up(self):
        self._lab.move_player(self._x, self._y - 1)
        self._y -= 1


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

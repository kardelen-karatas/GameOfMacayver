"""
Openclassrooms Project no:3
Model of MacGayver's Labyrinth Game
Author: Kardelen Karatas
Date: 23 october 2018 
"""


class Lab:

    def __init__(self, rows, wall):
        self._player = None
        self._rows = rows
        self._wall = wall
        self._lab = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            for _ in range(self._rows)
        ]

    def rows(self):
        return self._rows

    def wall(self):
        return self._wall

    def create_lab(self):

        for i in range(self._rows):

            if i == 0 or i == self._rows - 1:
                self._lab[i] = [self._wall for _ in self._lab[i]]
            else:
                self._lab[i][0] = self._wall
                self._lab[i][-1] = self._wall

        return self._lab

    def add_player(self, player):
        self._player = player
        self._lab[player.y()][player.x()] = player.symbol()
        return self._lab

    def move_player(self, dest_x, dest_y):
        self._lab[self._player.y()][self._player.x()] = " "
        self._lab[dest_y][dest_x] = self._player.symbol()

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
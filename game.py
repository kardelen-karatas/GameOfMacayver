"""
Openclassrooms Project no:3
Model of MacGayver's Labyrinth Game
Author: Kardelen Karatas
Date: 23 october 2018 
"""


class Lab:

    def __init__(self, rows, wall):
        self._rows = rows
        self._wall = wall
        # self._moving_object = moving_obect
        # self._player = player
        self._lab = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            for _ in range(self._rows)
        ]

    def rows(self):
        return self._rows

    def wall(self):
        return self._wall

    # def moving_object(self):
    #     return self._moving_object

    # def player_x(self):
    #     return self._player.x()

    # def player_y(self):
    #     return self._player.y()

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
        self._lab[player.y()][player.x()] = 'P'

        return self._lab

    def __str__(self):
        return '\n'.join([repr(l) for l in self._lab])


class Player:

    def __init__(self, x, y,lab):
        self._x = x
        self._y = y
        self._lab = lab

    def x(self):
        return self._x

    def y(self):
        return self._y


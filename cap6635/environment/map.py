
import numpy as np
import random

from cap6635.utilities.constants import (
    STATE_CLEAN, STATE_DIRTY, STATE_OBSTACLE,
    TTT_NONE, TTT_X, TTT_O
)


class Map2D:
    def __init__(self, m=10, n=10, wall=True):
        self._x = m
        self._y = n
        self._map = np.zeros((m, n))
        if wall:
            self.buildWall()

    def buildWall(self):
        self._map[:, 0] = STATE_OBSTACLE
        self._map[0, :] = STATE_OBSTACLE
        self._map[-1, :] = STATE_OBSTACLE
        self._map[:, -1] = STATE_OBSTACLE

    @property
    def map(self):
        return self._map


class Carpet(Map2D):

    def __init__(self, m=10, n=10):
        super(Carpet, self).__init__(m, n)
        self.randomizeDirt()
        self.generateDirt()

    def randomizeDirt(self):
        for x in range(1, self._x-1):
            for y in range(1, self._y-1):
                self._map[x, y] = random.uniform(0.1, 0.6)

    def generateDirt(self):
        for x in range(1, self._x-1):
            for y in range(1, self._y-1):
                if random.random() < self._map[x, y]:
                    self._map[x, y] = STATE_DIRTY
                else:
                    self._map[x, y] = STATE_CLEAN

    def dirtPresent(self):
        return STATE_DIRTY in self._map


class TicTacToe(Map2D):

    def __init__(self, x=3, y=3):
        super(TicTacToe, self).__init__(x, y, wall=False)
        self._win = False

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, v):
        self._win = v

    def is_empty(self, x, y):
        if self.map[x, y] == TTT_NONE:
            return True
        return False

    def is_valid(self, x, y):
        if x >= 0 and x < self._x:
            if y >= 0 and y < self._y:
                if self.map[x, y] == TTT_NONE:
                    return True
        return False

    def is_win(self):
        # Horizontal win
        for x in range(0, self._x):
            if (self.map[x] == [self.map[x][0]] * self._x).all() and \
               self.map[x][0] != TTT_NONE:
                self.win = self.map[x][0]
                return True

        # Vertical win
        # TODO: make this work for more than 3
        for y in range(0, self._y):
            if self.map[0][y] != TTT_NONE and \
               self.map[0][y] == self.map[1][y] == self.map[2][y]:
                self.win = self.map[0][y]
                return True

        # Diagonal win
        # TODO: make this work for more than 3
        if self.map[1][1] != TTT_NONE:
            if self.map[0][0] == self.map[1][1] == self.map[2][2] or \
               self.map[0][2] == self.map[1][1] == self.map[2][0]:
                self.win = self.map[1][1]
                return True

        # Full board
        if TTT_NONE not in self.map:
            self.win = TTT_NONE
            return True

        return False

    def print_board(self):
        for i in range(0, self._x):
            for j in range(0, self._y):
                char = ' '
                if self.map[i][j] == TTT_X:
                    char = 'X'
                elif self.map[i][j] == TTT_O:
                    char = 'O'
                elif self.map[i][j] == TTT_NONE:
                    char = '.'
                print('{}|'.format(char), end=" ")
            print()
        print()

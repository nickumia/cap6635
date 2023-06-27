
import numpy as np
import random

from cap6635.utilities.constants import (
    STATE_CLEAN, STATE_DIRTY, STATE_OBSTACLE
)


class Map2D:
    def __init__(self, m=10, n=10):
        self._x = m
        self._y = n
        self._map = np.zeros((m, n))
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

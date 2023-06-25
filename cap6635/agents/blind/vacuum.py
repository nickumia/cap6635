
import random

from cap6635.utilities.constants import (
    MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT,
    MOVE_CLEAN, MOVE_STOP, MOVE_IDLE
)


class Vacuum:

    def __init__(self, environ, start=(1,1)):
        self._e = environ
        self._x = start[0]
        self._y = start[1]
        self._x_path = []
        self._y_path = []
        self._utility = 0
        self._time = 0

    @property
    def utility(self):
        return self._utility

    @utility.setter
    def utility(self, val):
        self._utility += val

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, val):
        self._time += val

    def move(self):
        action = self.clean()
        if not action:
            action = self.chooseMove()
        if (action == MOVE_UP):
            print("up")
            self._x -= 1
            self.utility = -1
        elif (action == MOVE_DOWN):
            print("down")
            self._x += 1
            self.utility = -1
        elif (action == MOVE_LEFT):
            print("left")
            self._y -= 1
            self.utility = -1
        elif (action == MOVE_RIGHT):
            print("right")
            self._y += 1
            self.utility = -1
        elif (action == MOVE_CLEAN):
            print("clean")
            self._e.map[self._x][self._y] = 0
            self.utility = 10
        elif (action == MOVE_IDLE):
            print("idle")
            self.utility = 0

        self.add_to_path((self._x, self._y))
        self.time = 1

    def clean(self):
        if self._e.map[self._x][self._y] == 2:
            return MOVE_CLEAN

    @property
    def x_path(self):
        return self._x_path

    @property
    def y_path(self):
        return self._y_path

    def add_to_path(self, point):
        self._x_path.append(point[0])
        self._y_path.append(point[1])


class SimpleVacuum(Vacuum):

    def chooseMove(self):
        actions = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_IDLE]
        if self._x == 1:
            actions.remove(MOVE_UP)
        if self._x == self._e._x-2:
            actions.remove(MOVE_DOWN)
        if self._y == 1:
            actions.remove(MOVE_LEFT)
        if self._y == self._e._y-2:
            actions.remove(MOVE_RIGHT)

        return random.choice(actions)


class ModelVacuum(Vacuum):

    def chooseMove(self):
        # last column
        if self._y == self._e._y-2:
            # even # of columns
            if self._e._x % 2 == 0:
                # stop at the top
                if self._x == 1:
                    return MOVE_STOP
            else:
                # stop at the bottom
                if self._x == self._e._x-2:
                    return MOVE_STOP
        # odd columns
        if self._y % 2 == 1:
            # bottom tile
            if self._x == self._e._x-2:
                return MOVE_RIGHT
            return MOVE_DOWN
        # even columns
        if self._y % 2 == 0:
            # top tile
            if self._x == 1:
                return MOVE_RIGHT
            return MOVE_UP


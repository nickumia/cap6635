
import random


class Vacuum:

    def __init__(self, environ, start=(1,1)):
        self._e = environ
        self._x = start[0]
        self._y = start[1]
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


class SimpleVacuum(Vacuum):

    def __init__(self, environ):
        super(SimpleVacuum, self).__init__(environ)
        self._x_path = []
        self._y_path = []

    def chooseMove(self):
        if self._e.map[self._x][self._y] == 2:
            return 4

        actions = [0, 1, 2, 3, 6]
        if self._x == 1:
            actions.remove(0)
        if self._x == self._e._x-2:
            actions.remove(1)
        if self._y == 1:
            actions.remove(2)
        if self._y == self._e._y-2:
            actions.remove(3)

        return random.choice(actions)

    def move(self):
        action = self.chooseMove()
        if (action == 0):
            print("up")
            self._x -= 1
            self.utility = -1
        elif (action == 1):
            print("down")
            self._x += 1
            self.utility = -1
        elif (action == 2): # go left
            print("left")
            self._y -= 1
            self.utility = -1
        elif (action == 3): # go right
            print("right")
            self._y += 1
            self.utility = -1
        elif (action == 4): # clean
            print("clean")
            self._e.map[self._x][self._y] = 0
            self.utility = 10
        elif (action == 6): # idle
            print("idle")
            self.utility = 0

        self.add_to_path((self._x, self._y))
        self.time = 1

    @property
    def x_path(self):
        return self._x_path

    @property
    def y_path(self):
        return self._y_path

    def add_to_path(self, point):
        self._x_path.append(point[0])
        self._y_path.append(point[1])

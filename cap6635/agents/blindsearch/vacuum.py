
from copy import deepcopy
import random

from cap6635.utilities.constants import (
    MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT,
    MOVE_CLEAN, MOVE_STOP, MOVE_IDLE,
    STATE_DIRTY, STATE_VISITED, STATE_OBSTACLE
)
from cap6635.utilities.node import SearchPoint
from cap6635.utilities.location import Location


class Vacuum:
    '''
    Base Vacuum Class
    - Tracks environment state
    - (current) Vacuum x, y location
    - (historical) Vacuum x, y path
    - Time spent operating (one move = one unit of time)
    - Utility (i.e. effectiveness at cleaning)
        - (-1) for each move
        - (+10) for cleaning a dirty spot
    '''

    def __init__(self, environ, start=(1, 1)):
        self._e = environ
        self._x = start[0]
        self._y = start[1]
        self._x_path = [self._x]
        self._y_path = [self._y]
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

    def buildPath(self, action):
        return [action]

    def move(self):
        action = self.chooseMove()
        actions = self.buildPath(action)

        first = self.clean()
        if first is not None:
            actions = [first]

        while len(actions) > 0:
            next_move = actions.pop(0)
            if (next_move == MOVE_UP):
                print("up")
                self._x -= 1
                self.utility = -1
            elif (next_move == MOVE_DOWN):
                print("down")
                self._x += 1
                self.utility = -1
            elif (next_move == MOVE_LEFT):
                print("left")
                self._y -= 1
                self.utility = -1
            elif (next_move == MOVE_RIGHT):
                print("right")
                self._y += 1
                self.utility = -1
            elif (next_move == MOVE_CLEAN):
                print("clean")
                self._e.map[self._x][self._y] = 0
                self.utility = 10
            elif (next_move == MOVE_IDLE):
                print("idle")
                self.utility = 0

            self.add_to_path((self._x, self._y))
            self.time = 1

        self.search = 1
        self.stack = SearchPoint((Location(self._x, self._y), MOVE_CLEAN))

    def clean(self):
        if self._e.map[self._x][self._y] == STATE_DIRTY:
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


class ReflexVacuum(Vacuum):
    '''
    Only unique element of Reflex Vacuum is random move choice
    - May revisit past spots
    - Random chance of moving to a dirty spot
    - May not get to all dirty spots (not complete)
    '''

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
    '''
    Only unique element of Reflex Vacuum is structured move choice
    - Will not revisit spots
    - Guaranteed to move to every spot
    - Will get to all dirty spots (complete)
    '''

    def chooseMove(self):
        # last column
        if self._y == self._e._y-2:
            # even # of columns
            if self._e._y % 2 == 0:
                # stop at the top
                if self._x == 1:
                    print("stop")
                    return MOVE_STOP
            else:
                # stop at the bottom
                if self._x == self._e._x-2:
                    print("stop")
                    return MOVE_STOP
        # odd columns
        if self._y % 2 == 1:
            # bottom tile
            if self._x == self._e._x-2:
                print("right")
                return MOVE_RIGHT
            print("down")
            return MOVE_DOWN
        # even columns
        if self._y % 2 == 0:
            # top tile
            if self._x == 1:
                print("right")
                return MOVE_RIGHT
            print("up")
            return MOVE_UP


class GoalVacuum(Vacuum):
    '''
    Looks for the nearest dirty spot favoring left, right, up then down.
    - May revisit past spots if equidistant between two dirty spots
    - Will find all dirty spots (complete)
    - Local minimum optimal (i.e. the closest dirty spot may not lead
        to the best overall path)
    '''

    def __init__(self, environ, start=(1, 1)):
        super(GoalVacuum, self).__init__(environ, start)
        self._stack = [SearchPoint((Location(start[0], start[1]), MOVE_CLEAN))]
        self._search_map = deepcopy(self._e.map)

    @property
    def stack(self):
        return self._stack

    @stack.setter
    def stack(self, val):
        self._stack = [val]

    @property
    def search(self):
        return self._search_map

    @search.setter
    def search(self, val):
        if val == 1:
            self._search_map = deepcopy(self._e.map)

    def moveable(self, x, y):
        if self._e.map[x, y] == STATE_OBSTACLE:
            return False
        return True

    def visit(self, node):
        position, action = node.data
        if self._e.map[position.x, position.y] == STATE_DIRTY:
            return True
        if self._search_map[position.x, position.y] != STATE_VISITED:
            self._stack.append(node)
            self._search_map[position.x, position.y] = STATE_VISITED

    def buildPath(self, node):
        path = []
        todo = node
        while True:
            position, action = todo.data
            path.append(action)
            if todo.parent is None:
                break
            todo = todo.parent

        return path

    def chooseMove(self):
        while len(self._stack) != 0:
            node = self._stack.pop(0)
            position, action = node.data

            # Looking left
            if self.moveable(position.x, position.y-1):
                new_node = SearchPoint(
                    (Location(position.x, position.y-1), MOVE_LEFT), node)
                if self.visit(new_node):
                    return new_node

            # Looking right
            if self.moveable(position.x, position.y+1):
                new_node = SearchPoint(
                    (Location(position.x, position.y+1), MOVE_RIGHT), node)
                if self.visit(new_node):
                    return new_node

            # Looking up
            if self.moveable(position.x-1, position.y):
                new_node = SearchPoint(
                    (Location(position.x-1, position.y), MOVE_UP), node)
                if self.visit(new_node):
                    return new_node

            # Looking down
            if self.moveable(position.x+1, position.y):
                new_node = SearchPoint(
                    (Location(position.x+1, position.y), MOVE_DOWN), node)
                if self.visit(new_node):
                    return new_node

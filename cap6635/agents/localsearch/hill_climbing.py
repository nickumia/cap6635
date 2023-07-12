
from copy import deepcopy
import random


class HillClimbing():

    def __init__(self, board):
        self._solution_located = False
        self._board = board
        self._answer = board._chess_board
        self._cost = [self._board.eval_cost(self._answer)]

    def random_init(self):
        self._board.random_init()
        self._answer = self._board._chess_board
        self._cost = [self._board.eval_cost(self._answer)]

    def climb(self):
        pairs = self._board.successors()
        for i in range(len(pairs)):
            pair = random.choice(pairs)
            pairs.remove(pair)
            new_position = deepcopy(self._answer)
            old_pair = new_position[pair[0]]
            new_position[pair[0]] = new_position[pair[1]]
            new_position[pair[1]] = old_pair
            new_cost = self._board.eval_cost(new_position)
            if new_cost < self._cost[-1]:
                self._answer = new_position
                self._cost.append(new_cost)
                if self._cost[-1] == 0:
                    self._solution_located = True
                    self._board._chess_board = self._answer
                self.climb()
        return "Failed"


from copy import deepcopy
from math import exp
import random


class SimulatedAnnealing():

    def __init__(self, board, temperature, cooling_rate=0.99):
        self._solution_located = False
        self._board = board
        self._answer = board._chess_board
        self._starting_temperature = temperature
        self._t = self._starting_temperature
        self._cooling_rate = cooling_rate
        self._cost = [self._board.eval_cost(self._answer)]

    def random_init(self):
        self._board.random_init()
        self._answer = self._board._chess_board
        self._cost = [self._board.eval_cost(self._answer)]
        self._t = self._starting_temperature

    def anneal(self):
        while self._t > 0.0000001:
            self._t *= self._cooling_rate
            pairs = self._board.successors()
            for i in range(len(pairs)):
                pair = random.choice(pairs)
                pairs.remove(pair)
                new_position = deepcopy(self._answer)
                old_pair = new_position[pair[0]]
                new_position[pair[0]] = new_position[pair[1]]
                new_position[pair[1]] = old_pair
                new_cost = self._board.eval_cost(new_position)
                delta = new_cost - self._cost[-1]
                if delta < 0 or (random.uniform(0, 1) < exp(-delta / self._t)):
                    self._answer = new_position
                    self._cost.append(new_cost)
                    if self._cost[-1] == 0:
                        self._solution_located = True
                        self._board._chess_board = self._answer
                    return True
        return False

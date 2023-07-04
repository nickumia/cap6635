
from copy import deepcopy


class HillClimbing():

    def __init__(self, board):
        self._solution_located = False
        self._board = board
        self._answer = board._chess_board
        self._cost = [self._board.total_tension(self._answer)]

    def random_init(self):
        self._board.random_init()
        self._answer = self._board._chess_board
        self._cost = [self._board.total_tension(self._answer)]

    def climb(self):
        for pair in self._board.successors():
            new_position = deepcopy(self._answer)
            old_pair = new_position[pair[0]]
            new_position[pair[0]] = new_position[pair[1]]
            new_position[pair[1]] = old_pair
            new_cost = self._board.total_tension(new_position)
            if new_cost < self._cost[-1]:
                self._answer = new_position
                self._cost.append(new_cost)
                if self._cost[-1] == 0:
                    self._solution_located = True
                self.climb()
        return "Failed"

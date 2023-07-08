
from itertools import combinations
import random


class NQueens:

    def __init__(self, n):
        self._n = n
        self._chess_board = {}
        self.random_init()

    def max_cost(self):
        return self._n * (self._n - 1)

    def random_init(self):
        rows = list(range(self._n))
        random.shuffle(rows)
        for column in range(self._n):
            self._chess_board[column] = random.choice(rows)
            rows.remove(self._chess_board[column])

    def royal_tension(self, q1, q2):
        ''' 1 if queens threaten each other, otherwise 0'''
        if q1[0] == q2[0]:
            return 1
        if q1[1] == q2[1]:
            return 1
        if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
            return 1
        return 0

    def eval_cost(self, board):
        tension = 0
        indexes = [(col, row) for col, row in board.items()]
        for pair in list(combinations(indexes, 2)):
            tension += self.royal_tension(pair[0], pair[1])
        return tension

    def successors(self):
        ''' All successor swaps '''
        return list(combinations(list(range(self._n)), 2))

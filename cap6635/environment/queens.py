
from itertools import combinations
# import math
import random


class NQueens:

    def __init__(self, n):
        self._n = n
        self._chess_board = {}
        self.random_init()

    def max_cost(self):
        return self._n * (self._n - 1)

    def random_init(self):
        rows = list(range(1, self._n+1))
        random.shuffle(rows)
        for column in range(1, self._n+1):
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
        return list(combinations(list(range(1, self._n+1)), 2))


class NQueensGeneticEncoding(NQueens):

    def __init__(self, n):
        super(NQueensGeneticEncoding, self).__init__(n)
        self._sequence = []
        self._perfect_form = self.max_cost() / 2
        self._survival_rate = 0
        self._permutation = []
        self.convert_board()

    def compute_permutation(self):
        not_missing = set(self._sequence)
        self._permutation = []
        for i, v in enumerate(self._sequence):
            if v in not_missing:
                not_missing.remove(v)
            else:
                self._permutation.append(i)

    def compute_survival(self):
        self._survival_rate = \
            (self._perfect_form - self.eval_cost(self._chess_board)) /\
            self._perfect_form
        # self._survival_rate += random.uniform(
        #         math.pow(10, -10), math.pow(10, -20))

    def convert_board(self):
        self._sequence = []
        for i in range(1, self._n+1):
            self.sequence.append(self._chess_board[i])
        self._survival_rate = \
            self.eval_cost(self._chess_board) / self._perfect_form
        self.compute_permutation()

    @property
    def perfect_form(self):
        return self._perfect_form

    @property
    def sequence(self):
        return self._sequence

    @property
    def survival_rate(self):
        return self._survival_rate

    @property
    def permutation(self):
        return self._permutation

    @survival_rate.setter
    def survival_rate(self, val):
        self.compute_survival()

    @sequence.setter
    def sequence(self, val):
        self._sequence = val
        for i, v in enumerate(val):
            self._chess_board[i+1] = int(v)
        self.compute_survival()
        self.compute_permutation()

    def swap(self, r1, r2):
        self._sequence[r2-1] = self._chess_board[r1]
        self._sequence[r1-1] = self._chess_board[r2]
        self._chess_board[r1] = self._sequence[r1-1]
        self._chess_board[r2] = self._sequence[r2-1]
        self.compute_survival()
        self.compute_permutation()

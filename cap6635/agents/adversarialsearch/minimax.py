
from cap6635.utilities.constants import TTT_X, TTT_O, TTT_NONE


class MiniMax:

    def __init__(self, board, player, ai, free, worst_case=-100):
        self._worst_case = worst_case
        self._board = board
        self._player = player
        self._ai = ai
        self._free = free
        self.count = 0

    def _win(self):
        # TODO: make this reward parameterized for more options
        self.count += 1
        # print(self.count)
        if self._board.win == TTT_X:
            return (-1, 0, 0)
        elif self._board.win == TTT_O:
            return (1, 0, 0)
        elif self._board.win == TTT_NONE:
            return (0, 0, 0)
        # return (self._board.win, 0, 0)

    def _max(self):
        mv = self._worst_case
        pqx = None
        pqy = None

        if self._board.is_win():
            return self._win()

        for x in range(self._board._x):
            for y in range(self._board._y):
                if self._board.is_empty(x, y):
                    self._board.map[x, y] = self._player
                    (m, m_x, m_y) = self._min()
                    if m > mv:
                        mv = m
                        pqx = x
                        pqy = y
                    self._board.map[x, y] = self._free

        return (mv, pqx, pqy)

    def _min(self):
        mv = -self._worst_case
        pqx = None
        pqy = None

        if self._board.is_win():
            return self._win()

        for x in range(self._board._x):
            for y in range(self._board._y):
                if self._board.is_empty(x, y):
                    self._board.map[x, y] = self._ai
                    (m, m_x, m_y) = self._max()
                    if m < mv:
                        mv = m
                        pqx = x
                        pqy = y
                    self._board.map[x, y] = self._free

        return (mv, pqx, pqy)


class MiniMaxAlphaBeta(MiniMax):

    def __init__(self, board, player, ai, free, worst_case=-100):
        super(MiniMaxAlphaBeta, self).__init__(
            board, player, ai, free, worst_case=worst_case)

    def _max(self, alpha, beta):
        mv = self._worst_case
        pqx = None
        pqy = None

        if self._board.is_win():
            return self._win()

        for x in range(self._board._x):
            for y in range(self._board._y):
                if self._board.is_empty(x, y):
                    self._board.map[x, y] = self._player
                    (m, m_x, m_y) = self._min(alpha, beta)
                    if m > mv:
                        mv = m
                        pqx = x
                        pqy = y
                    self._board.map[x, y] = self._free
                    if mv >= beta:
                        return (mv, pqx, pqy)
                    if mv > alpha:
                        alpha = mv

        return (mv, pqx, pqy)

    def _min(self, alpha, beta):
        mv = -self._worst_case
        pqx = None
        pqy = None

        if self._board.is_win():
            return self._win()

        for x in range(self._board._x):
            for y in range(self._board._y):
                if self._board.is_empty(x, y):
                    self._board.map[x, y] = self._ai
                    (m, m_x, m_y) = self._max(alpha, beta)
                    if m < mv:
                        mv = m
                        pqx = x
                        pqy = y
                    self._board.map[x, y] = self._free
                    if mv <= alpha:
                        return (mv, pqx, pqy)
                    if mv < beta:
                        beta = mv

        return (mv, pqx, pqy)


from cap6635.utilities.constants import TTT_NONE, TTT_X, TTT_O


class MiniMax:
    def __init__(self, board, player):
        self._board = board
        self._player = player
        self._turn = TTT_X
        self.count = 0

    def _win(self):
        # TODO: make this reward parameterized for more options
        self.count += 1
        # print(self.count)
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        ai = TTT_X if self._player == TTT_O else TTT_O
        if self._board.win == ai:
            return (1, 0, 0)
        elif self._board.win == self._player:
            return (-1, 0, 0)
        return (0, 0, 0)

    def max(self, dum1=0, dum2=0):
        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2
        ai = TTT_O if self._player == TTT_X else TTT_X

        px = None
        py = None

        if self._board.is_win():
            return self._win()

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.map[i][j] == TTT_NONE:
                    self._board.map[i][j] = ai
                    (m, min_i, min_j) = self.min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self._board.map[i][j] = TTT_NONE
        return (maxv, px, py)

    def min(self, dum1=0, dum2=0):
        # We're initially setting it to 2 as worse than the worst case:
        minv = 2
        ai = TTT_X if self._player == TTT_X else TTT_O

        qx = None
        qy = None

        if self._board.is_win():
            return self._win()

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.map[i][j] == TTT_NONE:
                    self._board.map[i][j] = ai
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self._board.map[i][j] = TTT_NONE

        return (minv, qx, qy)


class MiniMaxAlphaBeta(MiniMax):

    def __init__(self, board, player):
        super(MiniMaxAlphaBeta, self).__init__(board, player)

    def max(self, alpha, beta):
        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2
        ai = TTT_O if self._player == TTT_X else TTT_X

        px = None
        py = None

        if self._board.is_win():
            return self._win()

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.map[i][j] == TTT_NONE:
                    self._board.map[i][j] = ai
                    (m, min_i, min_j) = self.min(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self._board.map[i][j] = TTT_NONE
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv
        return (maxv, px, py)

    def min(self, alpha, beta):
        # We're initially setting it to 2 as worse than the worst case:
        minv = 2
        ai = TTT_X if self._player == TTT_X else TTT_O

        qx = None
        qy = None

        if self._board.is_win():
            return self._win()

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.map[i][j] == TTT_NONE:
                    self._board.map[i][j] = ai
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self._board.map[i][j] = TTT_NONE
                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv
        return (minv, qx, qy)

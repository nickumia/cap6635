
from cap6635.utilities.constants import TTT_X, TTT_O


class MiniMax:

    def __init__(self, board, worst_case=-100):
        self._worst_case = worst_case
        self._board = board

    def _minimax(self, turn):
        mv = self._worst_case
        pqx = None
        pqy = None

        if self._board.is_win():
            if self._board.win == TTT_X:
                return (-1, 0, 0)
            elif self._board.win == TTT_O:
                return (1, 0, 0)
            return (0, 0, 0)
            # return (self._board.win, 0, 0)

        for x in range(self._board._x):
            for y in range(self._board._y):
                if self._board.is_empty(x, y):
                    self._board.map[x, y] = turn[0]
                    (m, m_x, m_y) = self._minimax(turn[1::-1] + [turn[2]])
                    if m > mv:
                        mv = m
                        pqx = x
                        pqy = y
                    self._board.map[x, y] = turn[2]

        return (mv, pqx, pqy)

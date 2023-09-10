
from cap6635.utilities.constants import TTT_X, TTT_O


class MiniMax:

    def __init__(self, board, player, ai, free, worst_case=-100):
        self._worst_case = worst_case
        self._board = board
        self._player = player
        self._ai = ai
        self._free = free

    def _minimax(self, turn):
        if turn == self._player:
            mv = -self._worst_case
        else:
            mv = self._worst_case
        pqx = None
        pqy = None

        if self._board.is_win():
            if turn == self._player:
                if self._board.win == self._player:
                    return (1, 0, 0)
                elif self._board.win == self._ai:
                    return (-1, 0, 0)
            elif turn == self._ai:
                if self._board.win == self._player:
                    return (-1, 0, 0)
                elif self._board.win == self._ai:
                    return (1, 0, 0)
            return (0, 0, 0)
            # return (self._board.win, 0, 0)

        for x in range(self._board._x):
            for y in range(self._board._y):
                if self._board.is_empty(x, y):
                    self._board.map[x, y] = turn
                    if turn == self._player:
                        (m, m_x, m_y) = self._minimax(self._ai)
                    elif turn == self._ai:
                        (m, m_x, m_y) = self._minimax(self._player)
                    if self._player == turn:
                        if m < mv:
                            mv = m
                            pqx = x
                            pqy = y
                    else:
                        if m > mv:
                            mv = m
                            pqx = x
                            pqy = y
                    self._board.map[x, y] = self._free

        return (mv, pqx, pqy)

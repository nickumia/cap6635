
from cap6635.utilities.constants import TTT_NONE, TTT_X, TTT_O


class MiniMax:
    def __init__(self, board):
        self._board = board
        # Player X always plays first
        self.player_turn = TTT_X
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
        if self._board.win == TTT_O:
            return (1, 0, 0)
        elif self._board.win == TTT_X:
            return (-1, 0, 0)
        return (0, 0, 0)

    # Player 'O' is max, in this case AI
    def max(self):
        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        if self._board.is_win():
            return self._win()

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.map[i][j] == TTT_NONE:
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self._board.map[i][j] = TTT_O
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self._board.map[i][j] = TTT_NONE
        return (maxv, px, py)

    # Player 'X' is min, in this case human
    def min(self):
        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        if self._board.is_win():
            return self._win()

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.map[i][j] == TTT_NONE:
                    self._board.map[i][j] = TTT_X
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self._board.map[i][j] = TTT_NONE

        return (minv, qx, qy)

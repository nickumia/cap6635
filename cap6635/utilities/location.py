
class Location:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, val):
        self._x = val

    @y.setter
    def y(self, val):
        self._y = val

    @z.setter
    def z(self, val):
        self._z = val


def generateNumber(i):
    max_length = 8
    num_str = str(i)
    digits = len(num_str)
    zeros = max_length - digits
    return '0'*zeros + num_str

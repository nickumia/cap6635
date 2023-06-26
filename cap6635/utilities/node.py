
class SearchPoint:
    def __init__(self, data, parent=None):
        self._data = data
        self._parent = parent

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, val):
        self._parent = val

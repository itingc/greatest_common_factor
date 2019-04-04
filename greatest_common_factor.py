

class GreatestCommonFactor:
    def __init__(self, x, y):
        if not isinstance(x, int) or x < 0:
            raise ValueError("X must be a positive int")
        if not isinstance(y, int) or y < 0:
            raise ValueError("Y must be a positive int")

        self._x = x
        self._y = y


    """ Calculate the greatest common factor of number x and y"""
    def calculate_gcf(self):
        while(self._y):
            temp_x = self._x
            self._x = self._y
            self._y = temp_x % self._y

        return self._x
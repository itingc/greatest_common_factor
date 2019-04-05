


class GreatestCommonFactor:
    def __init__(self, x, y):
        try:
            x = int(x)
            y = int(y)
            if x < 0 or y < 0:
                raise ValueError("The numbers must be positive integer")
        except:
            raise ValueError("The numbers must be positive integer")
        self._x = x
        self._y = y


    """ Calculate the greatest common factor of number x and y"""
    def calculate_gcf(self):
        while self._y:
            temp_x = self._x
            self._x = self._y
            self._y = temp_x % self._y

        return self._x


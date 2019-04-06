from sqlalchemy import Column, Integer
from app.base import Base


class Gcf(Base):
    __tablename__ = "gcf"
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    gcf = Column(Integer)

    def __init__(self, x, y):
        try:
            x, y = int(x), int(y)
        except:
            raise ValueError("The numbers must be positive integer")

        if x <= 0 or y <= 0:
            raise ValueError("The numbers must be positive integer")

        self._x, self._y, self.gcf = x, y, 1

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_gcf(self):
        return self.gcf


    """ Calculate the greatest common factor of number x and y"""
    def calculate_gcf(self):
        while self._y:
            temp_x = self._x
            self._x = self._y
            self._y = temp_x % self._y

        self.gcf = self.x
        return self.gcf




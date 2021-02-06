import abc
from math import pi


class Figure(abc.ABC):

    @abc.abstractmethod
    def get_area(self):
        pass


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(pi * self.r ** 2)


class Triangle(Figure):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def get_area(self):
        return (self.a * self.h) / 2

class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a*self.b


from abc import ABC, abstractmethod
from math import pi


class IShape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Pizza(object):
    def __init__(self, _price: float, _shape: IShape):
        self.price = _price

    def get_price(self):
        return self.price


class Circle(IShape):
    def __init__(self, __radius: float):
        self.radius = __radius

    def to_string(self):
        return str(self.get_area())

    def get_area(self):
        return pi * self.radius * self.radius

class Rectangle(IShape):
    def __init__(self, __height: float, __width: float):
        self.height = __height
        self.width = __width

    def get_area(self):
        return self.height * self.width

    def to_string(self):
        return str(self.get_area())


class PizzaDeal:
    def deal(self, deal: float, pizza: Pizza):
        return pizza.get_price() / deal

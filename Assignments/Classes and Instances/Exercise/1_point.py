import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def distance(self, x: int, y: int):
        distance = math.sqrt(((self.x - x) ** 2) + ((self.y - y) ** 2))
        return distance

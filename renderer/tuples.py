import math


class Tuple:

    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        return Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Tuple(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, other):
        return Tuple(self.x * other, self.y * other, self.z * other, self.w * other)

    def __truediv__(self, other):
        return Tuple(self.x / other, self.y / other, self.z / other, self.w / other)

    def normalize(self):
        return Tuple(self.x / self.length(), self.y / self.length(), self.z / self.length(), self.w / self.length())

    def is_point(self):
        return self.w == 1

    def is_vector(self):
        return self.w == 0

    def __str__(self) -> str:
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ',' + str(self.w) + ')'

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Tuple): return False
        return self.x == o.x and self.y == o.y and self.z == o.z and self.w == o.w

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def red(self):
        return self.x

    def green(self):
        return self.y

    def blue(self):
        return self.z


def point(x, y, z):
    return Tuple(x, y, z, 1)


def vector(x, y, z):
    return Tuple(x, y, z, 0)


def color(x, y, z):
    return Tuple(x, y, z, 0)


red = color(1, 0, 0)
green = color(0, 1, 0)
blue = color(0, 0, 1)
black = color(0, 0, 0)
white = color(1, 1, 1)

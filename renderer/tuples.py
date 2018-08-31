import unittest
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
        return  Tuple(-self.x, -self.y, -self.z, -self.w)

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
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

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


class TestStringMethods(unittest.TestCase):

    def test_is_point(self):
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        self.assertEqual(4.3, a.x)
        self.assertEqual(-4.2, a.y)
        self.assertEqual(3.1, a.z)
        self.assertEqual(1.0, a.w)
        self.assertTrue(a.is_point())
        self.assertFalse(a.is_vector())

    def test_is_vector(self):
        a = Tuple(4.3, -4.2, 3.1, 0.0)
        self.assertEqual(4.3, a.x)
        self.assertEqual(-4.2, a.y)
        self.assertEqual(3.1, a.z)
        self.assertEqual(0.0, a.w)
        self.assertFalse(a.is_point())
        self.assertTrue(a.is_vector())

    def test_point_method(self):
        p = point(4, -4, 3)
        self.assertEqual(Tuple(4, -4, 3, 1), p)

    def test_vector_method(self):
        v = vector(4, -4, 3)
        self.assertEqual(Tuple(4, -4, 3, 0), v)

    def test_add_two_tuples(self):
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        self.assertEqual(Tuple(1, 1, 6, 1), a1 + a2)

    def test_substract_tuples(self):
        a1 = point(3, 2, 1)
        a2 = point(5, 6, 7)
        self.assertEqual(vector(-2, -4, -6), a1 - a2)

    def test_negation_tuples(self):
        a1 = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(-1, 2, -3, 4), -a1)

    def test_multiple_by_scalar(self):
        a1 = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(3.5, -7, 10.5, -14), a1 * 3.5)

    def test_divide_by_scalar(self):
        a1 = Tuple(1, -2, 3, -4)
        self.assertEqual(Tuple(0.5, -1, 1.5, -2), a1 / 2)

    def test_length(self):
        a1 = vector(1, 2, 3)
        self.assertEqual(math.sqrt(14.0), a1.length())

    def compare_tuples(self, t1, t2, delta=0.0001):
        self.assertTrue((t1 - t2).length() < delta)

    def test_normalize(self):
        v1 = vector(1, 2, 3)
        self.compare_tuples(vector(0.26726, 0.53452, 0.80178), v1.normalize())

    def test_dot_product(self):
        v1 = vector(1, 2, 3)
        v2 = vector(2, 3, 4)
        self.assertEqual(20, v1.dot(v2))

    def test_colors_as_tuples(self):
        c = color(-0.5, 0.4, 1.7)
        self.assertEqual(-0.5, c.red())
        self.assertEqual(0.4, c.green())
        self.assertEqual(1.7, c.blue())


if __name__ == '__main__':
    unittest.main()

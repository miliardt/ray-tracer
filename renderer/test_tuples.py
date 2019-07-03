import math, unittest

from renderer.test_utils import CommonTestBase
from renderer.tuples import Tuple, point, vector, color


class TuplesTest(CommonTestBase):

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

    def test_subtract_tuples(self):
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

    def test_reflecting_vector_approaching_45_degrees(self):
        v = vector(1, -1, 0)
        n = vector(0, 1, 0)
        r = v.reflect(n)

        self.assertEqual(vector(1, 1, 0), r)

    def test_reflecting_vector_of_slanted_surface(self):
        v = vector(0, -1, 0)
        n = vector(math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
        r = v.reflect(n)

        self.assert_tuple_equals(vector(1, 0, 0), r, 0.001)

    def test_cross_product_of_two_vectors(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)

        self.assertEqual(vector(-1, 2, -1), a.cross(b))
        self.assertEqual(vector(1, -2, 1), b.cross(a))


if __name__ == '__main__':
    unittest.main()

import unittest

from renderer.test_utils import CommonTestBase
from renderer.transformations import translation, scaling
from renderer.tuples import point, vector


class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def transform(self, transformation):
        return Ray(transformation * self.origin, transformation * self.direction)


class RayTest(CommonTestBase):

    def test_creating_ray(self):
        p = point(1, 2, 3)
        v = vector(4, 5, 6)
        r = Ray(p, v)
        self.assertEqual(p, r.origin)
        self.assertEqual(v, r.direction)

    def test_computing_point_from_distance(self):
        r = Ray(point(2, 3, 4), vector(1, 0, 0))
        self.assertEqual(point(2, 3, 4), r.position(0))
        self.assertEqual(point(3, 3, 4), r.position(1))
        self.assertEqual(point(1, 3, 4), r.position(-1))
        self.assertEqual(point(4.5, 3, 4), r.position(2.5))

    def test_translating_ray(self):
        r = Ray(point(1, 2, 3), vector(0, 1, 0))
        m = translation(3, 4, 5)
        r2 = r.transform(m)
        self.assertEqual(point(4, 6, 8), r2.origin)
        self.assertEqual(vector(0, 1, 0), r2.direction)

    def test_scaling_ray(self):
        r = Ray(point(1, 2, 3), vector(0, 1, 0))
        m = scaling(2, 3, 4)
        r2 = r.transform(m)
        self.assertEqual(point(2, 6, 12), r2.origin)
        self.assertEqual(vector(0, 3, 0), r2.direction)


if __name__ == '__main__':
    unittest.main()

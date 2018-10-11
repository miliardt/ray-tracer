from _pytest import unittest

from renderer import sphere
from renderer.intersections import intersections, Intersection, hit
from renderer.rays import Ray
from renderer.sphere import Sphere
from renderer.test_utils import CommonTestBase
from renderer.tuples import point, vector


class SphereTest(CommonTestBase):

    def test_create_intersection(self):
        s = sphere.Sphere()
        i = Intersection(3.5, s)
        self.assertEqual(3.5, i.t)
        self.assertEqual(s, i.shape)

    def test_aggregating_intersections(self):
        s = sphere.Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = intersections(i1, i2)

        self.assertEqual(2, len(xs))
        self.assertEqual(1, xs[0].t)
        self.assertEqual(2, xs[1].t)

    def test_intersect_sets_object_on_intersection(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = sphere.Sphere()
        xs = s.intersect(r)

        self.assertEqual(2, len(xs))
        self.assertEqual(s, xs[0].shape)
        self.assertEqual(s, xs[1].shape)

    def test_hit_when_all_intersections_have_positive_t(self):
        s = Sphere()
        i1 = Intersection(1, s)
        i2 = Intersection(2, s)
        xs = intersections(i1, i2)
        h = hit(xs)

        self.assertEqual(i1, h)

    def test_hit_when_some_intersections_have_negative_t(self):
        s = Sphere()
        i1 = Intersection(-1, s)
        i2 = Intersection(1, s)
        xs = intersections(i1, i2)
        h = hit(xs)

        self.assertEqual(i2, h)

    def test_hit_when_all_intersections_have_negative_t(self):
        s = Sphere()
        i1 = Intersection(-2, s)
        i2 = Intersection(-1, s)
        xs = intersections(i1, i2)
        h = hit(xs)

        self.assertIsNone(h)

    def test_hit_is_always__lowest_negative_intersection(self):
        s = Sphere()
        i1 = Intersection(5, s)
        i2 = Intersection(7, s)
        i3 = Intersection(-3, s)
        i4 = Intersection(2, s)
        xs = intersections(i1, i2, i3, i4)
        h = hit(xs)

        self.assertEqual(i4, h)


if __name__ == '__main__':
    unittest.main()

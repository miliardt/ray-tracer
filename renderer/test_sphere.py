import math
import unittest

from renderer.materials import Material
from renderer.matrices import identity_matrix
from renderer.rays import Ray
from renderer.sphere import Sphere
from renderer.test_utils import CommonTestBase
from renderer.transformations import translation, scaling
from renderer.tuples import point, vector


class SphereTest(CommonTestBase):
    def test_ray_intersects_sphere_at_two_points(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)

        self.assertEqual(2, len(xs))
        self.assertEqual(4, xs[0].t)
        self.assertEqual(6, xs[1].t)

    def test_ray_intersects_sphere_at_tangent(self):
        r = Ray(point(0, 1, -5), vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)

        self.assertEqual(2, len(xs))
        self.assertEqual(5, xs[0].t)
        self.assertEqual(5, xs[1].t)

    def test_ray_misses_sphere(self):
        r = Ray(point(0, 2, -5), vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)

        self.assertEqual(0, len(xs))

    def test_ray_originates_inside_sphere(self):
        r = Ray(point(0, 0, 0), vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)

        self.assertEqual(2, len(xs))
        self.assertEqual(-1, xs[0].t)
        self.assertEqual(1, xs[1].t)

    def test_sphere_behind_ray(self):
        r = Ray(point(0, 0, 5), vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)

        self.assertEqual(2, len(xs))
        self.assertEqual(-6, xs[0].t)
        self.assertEqual(-4, xs[1].t)

    def test_sphere_default_transformation(self):
        s = Sphere()

        self.assertEqual(identity_matrix, s.transform)

    def test_set_transform(self):
        s = Sphere()
        t = translation(2, 3, 4)
        s.set_transform(t)
        self.assertEqual(t, s.transform)

    def test_intersecting_scaled_sphere_with_ray(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()

        s.set_transform(scaling(2, 2, 2))
        xs = s.intersect(r)

        self.assertEqual(2, len(xs))
        self.assertEqual(3, xs[0].t)
        self.assertEqual(7, xs[1].t)

    def test_intersecting_translated_sphere_with_ray(self):
        r = Ray(point(0, 0, -5), vector(0, 0, 1))
        s = Sphere()

        s.set_transform(translation(5, 0, 0))
        xs = s.intersect(r)

        self.assertEqual(0, len(xs))

    def test_normal_on_sphere_at_point_on_x_axis(self):
        s = Sphere()

        n = s.normal_at(point(1, 0, 0))

        self.assertEqual(vector(1, 0, 0), n)

    def test_normal_on_sphere_at_point_on_y_axis(self):
        s = Sphere()

        n = s.normal_at(point(0, 1, 0))

        self.assertEqual(vector(0, 1, 0), n)

    def test_normal_on_sphere_at_point_on_z_axis(self):
        s = Sphere()

        n = s.normal_at(point(0, 0, 1))

        self.assertEqual(vector(0, 0, 1), n)

    def test_normal_on_sphere_at_point_on_none_axial_point(self):
        s = Sphere()

        n = s.normal_at(point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))

        self.assertEqual(n.normalize(), n)

    def test_normal_is_normalized_vector(self):
        s = Sphere()

        n = s.normal_at(point(math.sqrt(3) / 3, math.sqrt(3) / 3, math.sqrt(3) / 3))

        self.assertEqual(n.normalize(), n)

    def test_computing_normal_on_translated_sphere(self):
        s = Sphere()
        s.set_transform(translation(0, 1, 0))

        n = s.normal_at(point(0, 1.70711, -0.70711))

        self.assert_tuple_equals(vector(0, 0.70711, -0.70711), n, 0.001)

    def test_computing_normal_on_scaled_sphere(self):
        s = Sphere()
        s.set_transform(scaling(1, 0.5, 1))

        n = s.normal_at(point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2))

        self.assert_tuple_equals(vector(0, 0.97014, -0.24254), n, 0.001)

    def test_sphere_has_default_material(self):
        s = Sphere()
        m = s.material

        self.assertEqual(Material(), m)

    def test_sphere_may_be_assigned_material(self):
        s = Sphere()
        m = Material(ambient=1)
        s.material = m

        self.assertEqual(m, s.material)


if __name__ == '__main__':
    unittest.main()

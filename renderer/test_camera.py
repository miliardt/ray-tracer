import unittest
from math import pi, sqrt

from renderer.camera import Camera, ray_for_pixel, render
from renderer.matrices import identity_matrix
from renderer.rays import Ray
from renderer.test_utils import CommonTestBase
from renderer.transformations import rotation_y, translation, view_transform
from renderer.tuples import point, vector, color
from renderer.world import default_world


class CameraTest(CommonTestBase):

    def test_constructing_camera(self):
        hsize = 160
        vsize = 120
        field_of_view = pi / 2.0

        c = Camera(hsize, vsize, field_of_view)

        self.assertEqual(160, c.hsize)
        self.assertEqual(120, c.vsize)
        self.assertEqual(pi / 2.0, c.field_of_view)
        self.assert_matrix_equals(identity_matrix, c.transform)

    def test_the_pixel_size_for_horizontal_canvas(self):
        c = Camera(200, 125, pi / 2.0)
        self.assertAlmostEqual(0.01, c.pixel_size, delta=0.001)

    def test_pixel_size_for_vertical_canvas(self):
        c = Camera(125, 200, pi / 2)
        self.assertAlmostEqual(0.01, c.pixel_size, delta=0.001)

    def test_construct_ray_through_the_center_of_the_canvas(self):
        c = Camera(201, 101, pi / 2.0)

        r = ray_for_pixel(c, 100, 50)

        self.assert_tuple_equals(point(0, 0, 0), r.origin, 0.001)
        self.assert_tuple_equals(vector(0, 0, -1), r.direction, 0.001)

    def test_construct_ray_through_corner_of_the_canvas(self):
        c = Camera(201, 101, pi / 2.0)

        r = ray_for_pixel(c, 0, 0)

        self.assert_tuple_equals(point(0, 0, 0), r.origin, 0.001)
        self.assert_tuple_equals(vector(0.66519, 0.33259, -0.66851), r.direction, 0.001)

    def test_construct_ray_when_camera_is_transformed(self):
        c = Camera(201, 101, pi / 2.0, transform=rotation_y(pi / 4.0) * translation(0, -2, 5))
        r = ray_for_pixel(c, 100, 50)

        self.assert_tuple_equals(point(0, 2, -5), r.origin, 0.001)
        self.assert_tuple_equals(vector(sqrt(2) / 2, 0, -sqrt(2) / 2), r.direction, 0.001)

    def test_rendering_world_with_camera(self):
        w = default_world()
        c = Camera(11, 11, pi / 2.0)
        from_where = point(0, 0, -5)
        to = point(0, 0, 0)
        up = vector(0, 1, 0)
        c.transform = view_transform(from_where, to, up)

        image = render(c, w)

        self.assert_tuple_equals(color(0.38066, 0.47583, 0.2855), image.pixel_at(5, 5), 0.001)


if __name__ == '__main__':
    unittest.main()

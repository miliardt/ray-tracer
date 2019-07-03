import math

from _pytest import unittest

from renderer.lights import PointLight
from renderer.materials import Material
from renderer.test_utils import CommonTestBase
from renderer.tuples import point, color, vector
from renderer.world import default_world


class MaterialTest(CommonTestBase):

    def setUp(self):
        self.material = Material()
        self.position = point(0, 0, 0)

    def test_default_material(self):
        m = Material()

        self.assertEqual(color(1, 1, 1), m.color)
        self.assertEqual(0.1, m.ambient)
        self.assertEqual(0.9, m.diffuse)
        self.assertEqual(0.9, m.specular)
        self.assertEqual(200, m.shininess)

    def test_lighting_with_eye_between_light_and_surface(self):
        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), color(1, 1, 1))

        self.assertEqual(color(1.9, 1.9, 1.9), self.material.lighting(light, self.position, eyev, normalv))

    def test_lighting_with_eye_between_light_and_surface_eye_offset_45_deg(self):
        eyev = vector(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), color(1, 1, 1))

        self.assertEqual(color(1, 1, 1), self.material.lighting(light, self.position, eyev, normalv))

    def test_lighting_with_eye_opposite_surface_light_offset_45_deg(self):
        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 10, -10), color(1, 1, 1))

        self.assert_tuple_equals(color(0.7364, 0.7364, 0.7364),
                                 self.material.lighting(light, self.position, eyev, normalv), 0.001)

    def test_lighting_with_eye_in_path_of_reflection_vector(self):
        eyev = vector(0, -math.sqrt(2) / 2, -math.sqrt(2) / 2)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 10, -10), color(1, 1, 1))

        self.assert_tuple_equals(color(1.6364, 1.6364, 1.6364),
                                 self.material.lighting(light, self.position, eyev, normalv), 0.001)

    def test_lighting_with_light_behind_surface(self):
        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, 10), color(1, 1, 1))

        self.assertEqual(color(0.1, 0.1, 0.1), self.material.lighting(light, self.position, eyev, normalv))

    def test_lighting_with_the_surface_in_shadow(self):
        eyev = vector(0, 0, -1)
        normal = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), color(1, 1, 1))
        in_shadow = True

        result = self.material.lighting(light, self.position, eyev, normal, in_shadow)

        self.assert_tuple_equals(color(0.1, 0.1, 0.1), result, 0.001)


if __name__ == '__main__':
    unittest.main()

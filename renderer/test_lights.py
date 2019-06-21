import unittest

from renderer.lights import PointLight
from renderer.test_utils import CommonTestBase
from renderer.tuples import color, point


class PointLightTest(CommonTestBase):

    def test_point_light_has_position_and_intensity(self):
        intensity = color(1, 1, 1)
        position = point(0, 0, 0)

        light = PointLight(position, intensity)

        self.assertEqual(position, light.position)
        self.assertEqual(intensity, light.intensity)


if __name__ == '__main__':
    unittest.main()

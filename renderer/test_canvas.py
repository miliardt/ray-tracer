from _pytest import unittest

from renderer.canvas import Canvas
from renderer.test_utils import CommonTestBase
from renderer.tuples import color


class CanvasTest(CommonTestBase):

    def test_is_canvas(self):
        c = Canvas(10, 20)
        self.assertEqual(10, c.width)
        self.assertEqual(20, c.height)
        for y in range(c.height):
            for x in range(c.width):
                self.assertEqual(color(0, 0, 0), c.pixel_at(x, y))

    def test_write_pixels(self):
        c = Canvas(10, 20)
        red = color(1, 0, 0)
        c.write_pixel(2, 3, red)
        self.assertEqual(red, c.pixel_at(2, 3))
        self.assertEqual(color(0, 0, 0), c.pixel_at(0, 0))

    def test_canvas_to_ppm(self):
        c = Canvas(5, 3)
        ppm = c.to_ppm()
        file_lines_list = ['P3', '5 3', '255']
        self.assertEqual(file_lines_list, ppm.split('\n')[0:3])

    def test_ppm_pixel_data(self):
        c = Canvas(5, 3)
        c1 = color(1.5, 0, 0)
        c2 = color(0, 0.5, 0)
        c3 = color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = c.to_ppm()
        file = ['255 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 128 0 0 0 0 0 0 0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 255']

        self.assertEqual(file, ppm.split('\n')[3:6])


if __name__ == '__main__':
    unittest.main()

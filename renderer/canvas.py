import unittest
from renderer.tuples import color


class Canvas():

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.canvas = [[color(0, 0, 0) for x in range(width)]
            for y in range(height)]

    def write_pixel(self, column, row, color):
        if column < 0 or column >= self.width: return
        if row < 0 or row >= self.height: return
        self.canvas[row][column] = color

    def pixel_at(self, column, row):
        return self.canvas[row][column]

    @staticmethod
    def clamp(k, lowest=0, highest=255):
        return min(max(k, lowest), highest)

    @staticmethod
    def map_to_ppm(k):
        return Canvas.clamp(round(k * 255))


    def to_ppm(self):
        file_contents = 'P3\n' + \
                 str(self.width) + ' ' + str(self.height) + '\n' \
                 '255\n'

        for y in range(self.height):
            for x in range(self.width):
                cell_color = self.pixel_at(x, y)
                r = cell_color.red()
                g = cell_color.green()
                b = cell_color.blue()

                if x > 0: file_contents += ' '

                file_contents += str(Canvas.map_to_ppm(r)) + ' '
                file_contents += str(Canvas.map_to_ppm(g)) + ' '
                file_contents += str(Canvas.map_to_ppm(b))

            file_contents += '\n'

        return file_contents

    def save_to_file(self, path):
        with open(path,'w') as file:
            file.write(self.to_ppm())


class TestStringMethods(unittest.TestCase):

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

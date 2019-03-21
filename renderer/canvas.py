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
        with open(path, 'w') as file:
            file.write(self.to_ppm())

from math import pi

from renderer.canvas import Canvas
from renderer.transformations import rotation_y
from renderer.tuples import point, vector, red

size = 200
center_vector = vector(size / 2, 0, size / 2)
twelve = point(0, 0, 3 * size / 8)
hours = [rotation_y(i * pi / 6) * twelve for i in range(12)]

c = Canvas(size, size)

for hour in hours:
    hour_point = hour + center_vector
    c.write_pixel(int(hour_point.x), int(hour_point.z), red)

c.save_to_file('clock.ppm')

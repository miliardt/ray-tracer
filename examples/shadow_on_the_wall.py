import time

from renderer.canvas import Canvas
from renderer.intersections import hit
from renderer.rays import Ray
from renderer.sphere import Sphere
from renderer.tuples import point, color

s = Sphere()
ray_origin = point(0, 0, -5)
wall_z = 10
wall_size = 7.0
canvas_pixels = 1000
pixel_size = wall_size / canvas_pixels
half = wall_size / 2

c = Canvas(canvas_pixels, canvas_pixels)
col = color(1, 0, 0)

start_time = time.time()
for y in range(canvas_pixels):
    elapsed_time = time.time() - start_time
    if elapsed_time > 0 and y > 0:
        print("time_to_finish: " + str(1.0 * (canvas_pixels-y) / (1.0 * y / elapsed_time)))
    world_y = half - pixel_size * y
    for x in range(canvas_pixels):
        world_x = - half + pixel_size * x
        position = point(world_x, world_y, wall_z)
        ray = Ray(ray_origin, (position - ray_origin))
        xs = s.intersect(ray)
        if hit(xs):
            c.write_pixel(x, y, col)


c.save_to_file('shadow_on_the_wall.ppm')
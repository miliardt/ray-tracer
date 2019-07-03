from math import tan

from renderer.canvas import Canvas
from renderer.matrices import identity_matrix
from renderer.rays import Ray
from renderer.tuples import point
from renderer.world import color_at


class Camera():
    def __init__(self, hsize, vsize, field_of_view, transform=identity_matrix):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform

        self.half_view = tan(self.field_of_view / 2)
        self.aspect = self.hsize / self.vsize

        if self.aspect >= 1:
            self.half_width = self.half_view
            self.half_height = self.half_view / self.aspect
        else:
            self.half_width = self.half_view * self.aspect
            self.half_height = self.half_view

        self.pixel_size = (self.half_width * 2) / self.hsize


def ray_for_pixel(camera, px, py):
    x_offset = (px + 0.5) * camera.pixel_size
    y_offset = (py + 0.5) * camera.pixel_size

    world_x = camera.half_width - x_offset
    world_y = camera.half_height - y_offset

    pixel = camera.transform.inverse() * point(world_x, world_y, -1)
    origin = camera.transform.inverse() * point(0, 0, 0)
    direction = (pixel - origin).normalize()

    return Ray(origin, direction)


def render(camera, world):
    image = Canvas(camera.hsize, camera.vsize)

    for y in range(camera.vsize - 1):
        for x in range(camera.hsize - 1):
            ray = ray_for_pixel(camera, x, y)
            color = color_at(world, ray)
            image.write_pixel(x, y, color)
    return image

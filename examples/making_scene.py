import time
from math import pi
from renderer.camera import Camera, render
from renderer.lights import PointLight
from renderer.materials import Material
from renderer.sphere import Sphere
from renderer.transformations import scaling, translation, rotation_y, rotation_x, view_transform
from renderer.tuples import point, color, vector
from renderer.world import World

floor = Sphere()
floor.transform = scaling(10, 0.01, 10)
floor.material.color = color(1, 0.9, 0.9)
floor.material.specular = 0

left_wall = Sphere()
left_wall.transform = translation(0, 0, 5) * rotation_y(-pi / 4) * rotation_x(pi / 2) * scaling(10, 0.01, 10)
left_wall.material.color = color(1, 0.9, 0.9)
left_wall.material.specular = 0

right_wall = Sphere()
right_wall.transform = translation(0, 0, 5) * rotation_y(pi / 4) * rotation_x(pi / 2) * scaling(10, 0.01, 10)
right_wall.material.color = color(1, 0.9, 0.9)
right_wall.material.specular = 0

middle = Sphere()
middle.transform = translation(-0.5, 1, 0.5)
middle.material.color = color(0.1, 1, 0.5)
middle.material.ambient = 0.1
middle.material.diffuse = 0.7
middle.material.specular = 0.3

right = Sphere()
right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
right.material.color = color(0.5, 1, 0.1)
right.material.diffuse = 0.7
right.material.specular = 0.3

left = Sphere()
left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
left.material.color = color(1, 0.8, 0.1)
left.material.diffuse = 0.7
left.material.specular = 0.3

light_position = point(-10, 10, -10)
light_color = color(1, 1, 1)
light = PointLight(light_position, light_color)

world = World(
    light=light,
    objects=[left, right, middle, left_wall, right_wall, floor]
)

camera = Camera(200, 100, pi / 3)
camera.transform = view_transform(point(0, 1.5, -5),
                                  point(0, 1, 0),
                                  vector(0, 1, 0))

r = render(camera, world)
r.save_to_file('scene2.ppm')

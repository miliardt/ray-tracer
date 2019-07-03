from renderer.intersections import intersections, hit
from renderer.lights import PointLight
from renderer.sphere import Sphere
from renderer.transformations import scaling
from renderer.tuples import point, color, black


class World:
    def __init__(self, **kwargs):
        self.light = kwargs.get('light')
        self.objects = kwargs.get('objects', [])


def default_world():
    light = PointLight(point(-10, 10, -10), color(1, 1, 1))

    s1 = Sphere()
    s2 = Sphere()

    s1.material.color = color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2

    s2.set_transform(scaling(0.5, 0.5, 0.5))

    return World(light=light, objects=[s1, s2])


def intersect_world(world, ray):
    xs = []

    for obj in world.objects:

        for xss in obj.intersect(ray):
            xs.append(xss)

    return sorted(xs, key=lambda val: val.t)


def shade_hit(world, h):
    return h.shape.material.lighting(world.light, h.point, h.eyev, h.normalv)


def color_at(world, ray):
    xss = intersect_world(world, ray)
    xs = intersections(xss)
    for item in xs:
        h = hit(item)
        if h is None:
            return black
        else:
            h.prepare_hit(ray)
            return shade_hit(world, h)

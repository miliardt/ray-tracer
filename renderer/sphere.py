from math import sqrt

import renderer.intersections as intersections
from renderer.matrices import identity_matrix
from renderer.rays import Ray
from renderer.tuples import point


class Sphere:

    def __init__(self):
        self.transform = identity_matrix

    def intersect(self, r: Ray):
        ray2 = r.transform(self.transform.inverse())
        sphere_to_ray = ray2.origin - point(0, 0, 0)
        a = ray2.direction.dot(ray2.direction)
        b = 2 * ray2.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        delta = b * b - 4 * a * c

        if delta < 0:
            return []

        t1 = (-b - sqrt(delta)) / (2 * a)
        t2 = (-b + sqrt(delta)) / (2 * a)

        i1 = intersections.Intersection(t1, self)
        i2 = intersections.Intersection(t2, self)

        return [i1, i2]

    def set_transform(self, t):
        self.transform = t

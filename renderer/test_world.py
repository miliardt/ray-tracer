import unittest

from renderer.intersections import Intersection
from renderer.lights import PointLight
from renderer.rays import Ray
from renderer.sphere import Sphere
from renderer.test_utils import CommonTestBase
from renderer.transformations import scaling
from renderer.tuples import point, color, vector
from renderer.world import World, intersect_world, shade_hit, color_at, default_world


class WorldTest(CommonTestBase):

    def test_creating_a_world(self):
        world = World()

        self.assertEqual([], world.objects)
        self.assertEqual(None, world.light)

    def test_default_world(self):
        light = PointLight(point(-10, 10, -10), color(1, 1, 1))

        s1 = Sphere()
        s2 = Sphere()

        s1.material.color = color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2

        s2.set_transform(scaling(0.5, 0.5, 0.5))

        world = default_world()

        self.assertEqual(light.position, world.light.position)
        self.assertEqual(light.intensity, world.light.intensity)

        self.assertEqual(s1.material.color, world.objects[0].material.color)
        self.assertEqual(s1.material.diffuse, world.objects[0].material.diffuse)
        self.assertEqual(s1.material.specular, world.objects[0].material.specular)

        self.assertEqual(s2.material.color, world.objects[1].material.color)
        self.assertEqual(s2.material.diffuse, world.objects[1].material.diffuse)
        self.assertEqual(s2.material.specular, world.objects[1].material.specular)

    def test_intersect_world_with_ray(self):
        world = default_world()
        ray = Ray(point(0, 0, -5), vector(0, 0, 1))

        xs = intersect_world(world, ray)

        self.assertEqual(4, len(xs))
        self.assertEqual(4, xs[0].t)
        self.assertEqual(4.5, xs[1].t)
        self.assertEqual(5.5, xs[2].t)
        self.assertEqual(6, xs[3].t)

    def test_shading_and_intersection(self):
        world = default_world()
        ray = Ray(point(0, 0, -5), vector(0, 0, 1))
        shape = world.objects[0]
        xs = Intersection(4, shape)

        xs.prepare_hit(ray)
        c = shade_hit(world, xs)

        self.assert_tuple_equals(color(0.38066, 0.47583, 0.2855), c, 0.001)

    def test_shading_an_intersection_form_the_inside(self):
        world = default_world()
        world.light = PointLight(point(0, 0.25, 0), color(1, 1, 1))
        ray = Ray(point(0, 0, 0), vector(0, 0, 1))
        shape = world.objects[1]
        xs = Intersection(0.5, shape)

        xs.prepare_hit(ray)
        c = shade_hit(world, xs)

        self.assert_tuple_equals(color(0.90498, 0.90498, 0.90498), c, 0.001)

    def test_the_color_when_ray_misses(self):
        world = default_world()
        ray = Ray(point(0, 0, -5), vector(0, 1, 0))

        c = color_at(world, ray)

        self.assertEqual(color(0, 0, 0), c)

    def test_the_color_when_ray_hits(self):
        world = default_world()
        ray = Ray(point(0, 0, -5), vector(0, 0, 1))

        c = color_at(world, ray)

        self.assert_tuple_equals(color(0.38066, 0.47583, 0.2855), c, 0.001)

    def test_the_color_with_an_intersection_behind_the_ray(self):
        world = default_world()
        outer = world.objects[0]
        outer.material.ambient = 1
        inner = world.objects[1]
        inner.material.ambient = 1
        ray = Ray(point(0, 0, 0.75), vector(0, 0, -1))

        c = color_at(world, ray)

        self.assertEqual(inner.material.color, c)


if __name__ == '__main__':
    unittest.main()

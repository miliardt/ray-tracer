import unittest
from math import pi, sqrt

from renderer.test_utils import CommonTestBase
from renderer.transformations import translation, scaling, rotation_x, rotation_y, rotation_z
from renderer.tuples import point, vector


class TestMatrixMethods(CommonTestBase):

    def test_multiplying_by_translation_matrix(self):
        p = point(-3, 4, 5)
        self.assertEqual(point(2, 1, 7), translation(5, -3, 2) * p)

    def test_multiplying_by_inverse_of_translation(self):
        self.assertEqual(point(-8, 7, 3), translation(5, -3, 2).inverse() * point(-3, 4, 5))

    def test_translation_does_not_affect_vectors(self):
        self.assertEqual(vector(-3, 4, 5), translation(5, -3, 2) * vector(-3, 4, 5))

    def test_scaling_matrix_applied_to_point(self):
        self.assertEqual(point(-8, 18, 32), scaling(2, 3, 4) * point(-4, 6, 8))

    def test_scaling_matrix_applied_to_vector(self):
        self.assertEqual(vector(-8, 18, 32), scaling(2, 3, 4) * vector(-4, 6, 8))

    def test_multiplying_by_inverse_of_scaling_matrix(self):
        self.assertEqual(vector(-2, 2, 2), scaling(2, 3, 4).inverse() * vector(-4, 6, 8))

    def test_reflection_scaling_by_a_negative_value(self):
        self.assertEqual(vector(-2, 3, 4), scaling(-1, 1, 1) * vector(2, 3, 4))

    def test_rotating_point_around_axis_x(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        full_quarter = rotation_x(pi / 2)
        self.assert_tuple_equals(point(0, sqrt(2) / 2, sqrt(2) / 2), half_quarter * p, 1e-5)
        self.assert_tuple_equals(point(0, 0, 1), full_quarter * p, 1e-5)

    def test_inverse_of_an_x_rotation(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        inv = half_quarter.inverse()
        self.assert_tuple_equals(point(0, sqrt(2) / 2, -sqrt(2) / 2), inv * p, 1e-5)

    def test_rotating_point_around_axis_y(self):
        p = point(0, 0, 1)
        half_quarter = rotation_y(pi / 4)
        full_quarter = rotation_y(pi / 2)
        self.assert_tuple_equals(point(sqrt(2) / 2, 0, sqrt(2) / 2), half_quarter * p, 1e-5)
        self.assert_tuple_equals(point(1, 0, 0), full_quarter * p, 1e-5)

    def test_rotating_point_around_axis_z(self):
        p = point(0, 1, 0)
        half_quarter = rotation_z(pi / 4)
        full_quarter = rotation_z(pi / 2)
        self.assert_tuple_equals(point(-sqrt(2) / 2, sqrt(2) / 2, 0), half_quarter * p, 1e-5)
        self.assert_tuple_equals(point(-1, 0, 0), full_quarter * p, 1e-5)

    def test_individual_transformation_are_applied_in_sequence(self):
        p = point(1, 0, 1)
        a = rotation_x(pi / 2)
        b = scaling(5, 5, 5)
        c = translation(10, 5, 7)

        p2 = a * p
        p3 = b * p2
        p4 = c * p3

        self.assertEqual(point(15, 0, 7), p4)

    def test_chain_transformation_must_be_applied_in_reverse_order(self):
        p = point(1, 0, 1)
        a = rotation_x(pi / 2)
        b = scaling(5, 5, 5)
        c = translation(10, 5, 7)

        t = c * b * a

        self.assertEqual(point(15, 0, 7), t * p)


if __name__ == '__main__':
    unittest.main()

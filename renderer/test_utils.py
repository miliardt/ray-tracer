import unittest


class CommonTestBase(unittest.TestCase):

    def compare_tuples(self, t1, t2, delta=0.0001):
        self.assertTrue((t1 - t2).length() < delta)

    def assert_matrix_equals(self, expected, actual):
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(expected[i, j], actual[i, j], delta=0.0001)

    def assert_tuple_equals(self, expected, actual, delta):
        self.assertAlmostEqual(expected.x, actual.x, delta=delta)
        self.assertAlmostEqual(expected.y, actual.y, delta=delta)
        self.assertAlmostEqual(expected.z, actual.z, delta=delta)
        self.assertAlmostEqual(expected.w, actual.w, delta=delta)

import unittest

from renderer.test_utils import CommonTestBase
from renderer.tuples import Tuple


class Matrix4:

    def __init__(self, *args):
        if len(args) == 16:
            self.l = [[args[0], args[1], args[2], args[3]],
                      [args[4], args[5], args[6], args[7]],
                      [args[8], args[9], args[10], args[11]],
                      [args[12], args[13], args[14], args[15]]]
        elif len(args) == 1:
            self.l = args[0]
        elif len(args) == 0:
            self.l = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        self._cached_inverse = None

    def __getitem__(self, item):
        m, n = item
        return self.l[m][n]

    def __setitem__(self, key, value):
        m, n = key
        self.l[m][n] = value

    def __mul__(self, other):

        if type(other) == Matrix4:
            outcome = Matrix4()
            for row in range(4):
                for col in range(4):
                    outcome[row, col] = self[row, 0] * other[0, col] + \
                                        self[row, 1] * other[1, col] + \
                                        self[row, 2] * other[2, col] + \
                                        self[row, 3] * other[3, col]
            return outcome
        elif type(other) == Tuple:
            return Tuple(self[0, 0] * other.x + self[0, 1] * other.y + self[0, 2] * other.z + self[0, 3] * other.w,
                         self[1, 0] * other.x + self[1, 1] * other.y + self[1, 2] * other.z + self[1, 3] * other.w,
                         self[2, 0] * other.x + self[2, 1] * other.y + self[2, 2] * other.z + self[2, 3] * other.w,
                         self[3, 0] * other.x + self[3, 1] * other.y + self[3, 2] * other.z + self[3, 3] * other.w)

    def submatrix(self, row, col):
        return Matrix3([[self[i, j] for j in range(4) if j != col] for i in range(4) if i != row])

    def minor(self, row, col):
        return self.submatrix(row, col).determinant()

    def cofactor(self, row, col):
        return self.minor(row, col) * ((-1) ** (row + col))

    def determinant(self):
        return self[0, 0] * self.cofactor(0, 0) + \
               self[0, 1] * self.cofactor(0, 1) + \
               self[0, 2] * self.cofactor(0, 2) + \
               self[0, 3] * self.cofactor(0, 3)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Matrix4): return False
        return self.l == o.l

    def transpose(self):
        outcome = Matrix4()
        for row in range(4):
            for col in range(4):
                outcome[row, col] = self[col, row]
        return outcome

    def inverse(self):
        if self._cached_inverse is None:
            d = self.determinant()
            self._cached_inverse = Matrix4([[self.cofactor(j, i) / d for j in range(4)] for i in range(4)])
        return self._cached_inverse

    def then(self, matrix):
        return matrix * self

    def __repr__(self):
        return str(self.l)





class Matrix3:

    def __init__(self, *args):
        if len(args) == 9:
            self.l = [[args[0], args[1], args[2]],
                      [args[3], args[4], args[5]],
                      [args[6], args[7], args[8]]]
        elif len(args) == 1:
            self.l = args[0]

    def __getitem__(self, item):
        m, n = item
        return self.l[m][n]

    def submatrix(self, row, col):
        return Matrix2([[self[i, j] for j in range(3) if j != col] for i in range(3) if i != row])

    def minor(self, row, col):
        return self.submatrix(row, col).determinant()

    def cofactor(self, row, col):
        return self.minor(row, col) * ((-1) ** (row + col))

    def determinant(self):
        return self[0, 0] * self.cofactor(0, 0) + self[0, 1] * self.cofactor(0, 1) + self[0, 2] * self.cofactor(0, 2)

    def __eq__(self, other):
        if type(other) != Matrix3: return False
        return self.l == other.l

    def __repr__(self):
        return str(self.l)


class Matrix2:

    def __init__(self, *args):

        if len(args) == 4:
            self.l = [[args[0], args[1]],
                      [args[2], args[3]]]
        elif len(args) == 1:
            self.l = args[0]

    def determinant(self):
        return self.l[0][0] * self.l[1][1] - self.l[0][1] * self.l[1][0]

    def __eq__(self, other):
        if type(other) != Matrix2: return False
        return self.l == other.l

    def __repr__(self):
        return str(self.l)


identity_matrix = Matrix4(1, 0, 0, 0,
                          0, 1, 0, 0,
                          0, 0, 1, 0,
                          0, 0, 0, 1)


class TestMatrixMethods(CommonTestBase):

    def test_create_matrix(self):
        m = Matrix4(1, 2, 3, 4,
                    5.5, 6.5, 7.5, 8.5,
                    9, 10, 11, 12,
                    13.5, 14.5, 15.5, 16.5)

        self.assertEqual(1, m[0, 0])
        self.assertEqual(4, m[0, 3])
        self.assertEqual(5.5, m[1, 0])
        self.assertEqual(7.5, m[1, 2])
        self.assertEqual(11, m[2, 2])
        self.assertEqual(13.5, m[3, 0])
        self.assertEqual(15.5, m[3, 2])

    def test_multiply_matrix(self):
        a = Matrix4(1, 2, 3, 4,
                    2, 3, 4, 5,
                    3, 4, 5, 6,
                    4, 5, 6, 7)
        b = Matrix4(0, 1, 2, 4,
                    1, 2, 4, 8,
                    2, 4, 8, 16,
                    4, 8, 16, 32)
        expected = Matrix4(24, 49, 98, 196,
                           31, 64, 128, 256,
                           38, 79, 158, 316,
                           45, 94, 188, 376)

        self.assertEqual(expected, a * b)

    def test_then_method(self):
        a = Matrix4(1, 2, 3, 4,
                    2, 3, 4, 5,
                    3, 4, 5, 6,
                    4, 5, 6, 7)
        b = Matrix4(0, 1, 2, 4,
                    1, 2, 4, 8,
                    2, 4, 8, 16,
                    4, 8, 16, 32)
        expected = Matrix4(24, 49, 98, 196,
                           31, 64, 128, 256,
                           38, 79, 158, 316,
                           45, 94, 188, 376)

        self.assertEqual(expected, b.then(a))


    def test_multiply_matrix_by_tuple(self):
        a = Matrix4(1, 2, 3, 4,
                    2, 4, 4, 2,
                    8, 6, 4, 1,
                    0, 0, 0, 1)
        b = Tuple(1, 2, 3, 1)

        self.assertEqual(Tuple(18, 24, 33, 1), a * b)

    def test_multiply_matrix_by_identity(self):
        a = Matrix4(0, 1, 2, 4,
                    1, 2, 4, 8,
                    2, 4, 8, 16,
                    4, 8, 16, 32)
        self.assertEqual(a, identity_matrix * a)

    def test_transpose_matrix(self):
        a = Matrix4(0, 9, 3, 0,
                    9, 8, 0, 8,
                    1, 8, 5, 3,
                    0, 0, 5, 8)

        expected = Matrix4(0, 9, 1, 0,
                           9, 8, 8, 0,
                           3, 0, 5, 5,
                           0, 8, 3, 8)

        self.assertEqual(expected, a.transpose())

    def test_det_matrix2(self):
        a = Matrix2(1, 5,
                    -3, 2)
        self.assertEqual(17, a.determinant())

    def test_sub_matrix3(self):
        a = Matrix3(1, 5, 0,
                    -3, 2, 7,
                    0, 6, -3)
        b = Matrix2(-3, 2,
                    0, 6)
        self.assertEqual(b, a.submatrix(0, 2))

    def test_sub_matrix4(self):
        a = Matrix4(-6, 1, 1, 6,
                    -8, 5, 8, 6,
                    -1, 0, 8, 2,
                    -7, 1, -1, 1)
        b = Matrix3(-6, 1, 6,
                    -8, 8, 6,
                    -7, -1, 1)
        self.assertEqual(b, a.submatrix(2, 1))

    def test_minor3(self):
        a = Matrix3(3, 5, 0,
                    2, -1, -7,
                    6, -1, 5)
        b = a.submatrix(1, 0)
        self.assertEqual(25, b.determinant())
        self.assertEqual(25, a.minor(1, 0))

    def test_cofactor3(self):
        a = Matrix3(3, 5, 0,
                    2, -1, -7,
                    6, -1, 5)
        self.assertEqual(-12, a.minor(0, 0))
        self.assertEqual(-12, a.cofactor(0, 0))
        self.assertEqual(25, a.minor(1, 0))
        self.assertEqual(-25, a.cofactor(1, 0))

    def test_det_matrix3(self):
        a = Matrix3(1, 2, 6,
                    -5, 8, -4,
                    2, 6, 4)
        self.assertEqual(56, a.cofactor(0, 0))
        self.assertEqual(12, a.cofactor(0, 1))
        self.assertEqual(-46, a.cofactor(0, 2))
        self.assertEqual(-196, a.determinant())

    def test_det_matrix4(self):
        a = Matrix4(-2, -8, 3, 5,
                    -3, 1, 7, 3,
                    1, 2, -9, 6,
                    -6, 7, 7, -9)
        self.assertEqual(690, a.cofactor(0, 0))
        self.assertEqual(447, a.cofactor(0, 1))
        self.assertEqual(210, a.cofactor(0, 2))
        self.assertEqual(51, a.cofactor(0, 3))
        self.assertEqual(-4071, a.determinant())

    def test_inverse(self):
        a = Matrix4(-5, 2, 6, -8,
                    1, -5, 1, 8,
                    7, 7, -6, -7,
                    1, -3, 7, 4)
        b = a.inverse()
        self.assertEqual(532, a.determinant())
        self.assertEqual(-160, a.cofactor(2, 3))
        self.assertEqual(-160 / 532, b[3, 2])
        self.assertEqual(105, a.cofactor(3, 2))
        self.assertEqual(105/532, b[2, 3])

        expected = Matrix4(0.21805, 0.45113, 0.24060, -0.04511,
                           -0.80827, -1.45677, -0.44361, 0.52068,
                           -0.07895, -0.22368, -0.05263, 0.19737,
                           -0.52256, -0.81391, -0.30075, 0.30639)
        self.assert_matrix_equals(expected, b)
        self.assert_matrix_equals(identity_matrix, a* b)


if __name__ == '__main__':
    unittest.main()
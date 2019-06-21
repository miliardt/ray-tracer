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

    def multiply3x3matrix(self, other):
        return Tuple(self[0, 0] * other.x + self[0, 1] * other.y + self[0, 2] * other.z,
                     self[1, 0] * other.x + self[1, 1] * other.y + self[1, 2] * other.z,
                     self[2, 0] * other.x + self[2, 1] * other.y + self[2, 2] * other.z,
                     0)

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

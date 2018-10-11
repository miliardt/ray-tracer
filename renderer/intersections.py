class Intersection:

    def __init__(self, t, shape):
        self.t = t
        self.shape = shape


def hit(intersections):
    return min([i for i in intersections if i.t > 0],
               default=None, key=lambda i: i.t)


def intersections(*args):
    return args

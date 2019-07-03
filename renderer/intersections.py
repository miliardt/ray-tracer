class Intersection:

    def __init__(self, t, shape):
        self.t = t
        self.shape = shape
        self.point = None
        self.eyev = None
        self.normalv = None
        self.inside = None

    def prepare_hit(self, ray):
        self.point = ray.position(self.t)
        self.eyev = - ray.direction
        self.normalv = self.shape.normal_at(self.point)

        if self.eyev.dot(self.normalv) < 0:
            self.inside = True
            self.normalv = -self.normalv
        else:
            self.inside = False


def hit(intersections):
    return min([i for i in intersections if i.t > 0],
               default=None, key=lambda i: i.t)


def intersections(*args):
    return args

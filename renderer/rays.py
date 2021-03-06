class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position(self, t):
        return self.origin + self.direction * t

    def transform(self, transformation):
        return Ray(transformation * self.origin, transformation * self.direction)

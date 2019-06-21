from renderer.tuples import Tuple


class PointLight:

    def __init__(self, position: Tuple, intensity: Tuple):
        self.intensity = intensity
        self.position = position

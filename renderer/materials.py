from math import pow

from renderer import tuples
from renderer.tuples import black


class Material:

    def __init__(self, color=tuples.color(1, 1, 1), ambient=0.1, diffuse=0.9, specular=0.9, shininess=200):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.shininess = shininess

    def __eq__(self, o: object) -> bool:
        return self.color == o.color and \
               self.ambient == o.ambient and \
               self.diffuse == o.diffuse and \
               self.specular == o.specular and \
               self.shininess == o.shininess

    def lighting(self, light, position, eyev, normalv, in_shadow=False):
        effective_color = self.color.mul(light.intensity)
        lightv = (light.position - position).normalize()

        ambient = effective_color * self.ambient
        light_dot_normal = lightv.dot(normalv)

        if light_dot_normal < 0 or in_shadow:
            diffuse = black
            specular = black
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal

            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye <= 0:
                specular = black
            else:
                factor = pow(reflect_dot_eye, self.shininess)
                specular = light.intensity * factor * self.specular

        return ambient + diffuse + specular

from renderer.tuples import point, vector, green
from renderer.canvas import Canvas


class Projectile:

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return 'Projectile (position: ' + str(self.position) + ', velocity: ' + self.velocity.__str__() + ')'

class World:

    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind

def tick(world, projectile):
    position = projectile.position + projectile.velocity
    velocity = projectile.velocity + world.gravity + world.wind
    return Projectile(position, velocity)


if __name__ == '__main__':
    w = World(vector(0, -0.1, 0), vector(-0.01, 0, 0))
    p = Projectile(position=point(0, 1, 0), velocity=vector(1, 1.8, 0).normalize() * 11.25)

    c = Canvas(900, 550)

    t = 0

    while p.position.y > 0:
        p = tick(w, p)
        t += 1

        c.write_pixel(round(p.position.x), c.height - round(p.position.y), green)

    c.save_to_file('projectile.ppm')

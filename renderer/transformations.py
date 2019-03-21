from math import sin, cos

from renderer.matrices import Matrix4


def translation(x, y, z):
    return Matrix4(1, 0, 0, x,
                   0, 1, 0, y,
                   0, 0, 1, z,
                   0, 0, 0, 1)


def scaling(x, y, z):
    return Matrix4(x, 0, 0, 0,
                   0, y, 0, 0,
                   0, 0, z, 0,
                   0, 0, 0, 1)


def rotation_x(r):
    return Matrix4(1, 0, 0, 0,
                   0, cos(r), -sin(r), 0,
                   0, sin(r), cos(r), 0,
                   0, 0, 0, 1)


def rotation_y(r):
    return Matrix4(cos(r), 0, sin(r), 0,
                   0, 1, 0, 0,
                   -sin(r), 0, cos(r), 0,
                   0, 0, 0, 1)


def rotation_z(r):
    return Matrix4(cos(r), -sin(r), 0, 0,
                   sin(r), cos(r), 0, 0,
                   0, 0, 1, 0,
                   0, 0, 0, 1)

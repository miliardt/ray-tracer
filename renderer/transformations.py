from math import sin, cos

from renderer.matrices import Matrix4
from renderer.tuples import vector


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


def view_transform(from_where, to, up):
    forward_vector = (to - from_where)
    if forward_vector != vector(0, 0, 0): forward_vector = forward_vector.normalize()
    left_vector = forward_vector.cross(up.normalize())
    true_up_vector = left_vector.cross(forward_vector)

    orientation = Matrix4(left_vector.x, left_vector.y, left_vector.z, 0,
                          true_up_vector.x, true_up_vector.y, true_up_vector.z, 0,
                          -forward_vector.x, -forward_vector.y, -forward_vector.z, 0,
                          0, 0, 0, 1)

    return orientation * translation(-from_where.x, -from_where.y, -from_where.z)

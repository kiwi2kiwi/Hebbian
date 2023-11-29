import numpy as np
import random
random.seed(1)
import Coordinates

def new_positions_spherical_coordinates():
    phi = random.uniform(0, 2 * np.pi)
    costheta = random.uniform(-1, 1)
    u = random.uniform(0, 1)

    theta = np.arccos(costheta)
    r = ((size - 10) / 2) * np.sqrt(u)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return (x, y, z)


def new_positions_circular_coordinates():
    phi = random.uniform(0, 2 * np.pi)
    costheta = random.uniform(-1, 1)
    u = random.uniform(0, 1)

    size = 100
    theta = np.arccos(costheta)
    r = (size / 2) * np.sqrt(u)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    # z = r * np.cos(theta)
    return (x, y)


def ordered_input_neurons(height, width, plane_end):
    global size
    V = []
    area = size - 20
    y_distance = area / height
    z_distance = area / width
    Y = np.arange(-(size / 2) + 10, (size / 2) - 10, y_distance)
    Z = np.arange(-(size / 2) + 10, (size / 2) - 10, z_distance)
    for y in Y:
        for z in Z:
            V.append(Coordinates.Coordinate(plane_end, y, z))
    return V


def ordered_output_neurons(height, width, plane_end):
    global size
    V = []
    area = size - 20
    y_distance = area / height
    z_distance = area / width
    Y = np.arange(-(size / 2) + 10, (size / 2) - 10, y_distance)
    Z = np.arange(-(size / 2) + 10, (size / 2) - 10, z_distance)
    for y in Y:
        for z in Z:
            V.append(Coordinates.Coordinate(plane_end, y, 0))
    return V

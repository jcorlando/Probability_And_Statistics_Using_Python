import numpy as np


def create_vector_points(origin, destination):
    origin_x = (1/(np.cos(origin)))
    origin_y = np.cos(origin)
    destination_x = (1/(np.cos(destination))) - (1/(np.cos(origin)))
    destination_y = np.cos(destination) - np.cos(origin)
    return origin_x, origin_y, destination_x, destination_y

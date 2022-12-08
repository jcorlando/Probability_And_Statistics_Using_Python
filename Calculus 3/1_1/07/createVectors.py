import numpy as np


def create_vector_points(origin, destination):
    origin_x = np.exp(-1*origin)
    origin_y = (np.exp(2*origin)) - 1
    destination_x = np.exp(-1*destination) - np.exp(-1*origin)
    destination_y = ((np.exp(2*destination)) - 1) - ((np.exp(2*origin)) - 1)
    return origin_x, origin_y, destination_x, destination_y

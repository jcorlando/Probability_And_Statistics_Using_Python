import numpy as np


# Create Vectors (Tail & Head) => (origin,, destination) To Help Evaluate The
# Direction (Path Taken) of the Parametric Function Respective Of The Parameter
def create_vector_points(origin, destination):
    origin_x = origin + np.sin(origin)
    origin_y = 1 - np.cos(origin)
    destination_x = (destination + np.sin(destination)) - (origin + np.sin(origin))
    destination_y = (1 - np.cos(destination)) - (1 - np.cos(origin))
    return origin_x, origin_y, destination_x, destination_y

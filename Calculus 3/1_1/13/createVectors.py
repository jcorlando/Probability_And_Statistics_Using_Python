import numpy as np


# Create Vectors (Tail & Head) => (origin,, destination) To Help Evaluate The
# Direction (Path Taken) of the Parametric Function Respective Of The Parameter
def create_vector_points(origin, destination):
    origin_x = 6*np.sin(2*origin)
    origin_y = 4*np.cos(2*origin)
    destination_x = (6*np.sin(2*destination)) - (6*np.sin(2*origin))
    destination_y = (4*np.cos(2*destination)) - (4*np.cos(2*origin))
    return origin_x, origin_y, destination_x, destination_y

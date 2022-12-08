import numpy as np


# Create Vectors (Tail & Head) => (origin,, destination) To Help Evaluate The
# Direction (Path Taken) of the Parametric Function Respective Of The Parameter
def create_vector_points(origin, destination):
    origin_x = 3 - 2*np.cos(origin)
    origin_y = -5 + 3*np.sin(origin)
    destination_x = (3 - 2*np.cos(destination)) - (3 - 2*np.cos(origin))
    destination_y = (-5 + 3*np.sin(destination)) - (-5 + 3*np.sin(origin))
    return origin_x, origin_y, destination_x, destination_y

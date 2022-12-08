import numpy as np


# Create Vectors (Tail & Head) => (origin,, destination) To Help Evaluate The
# Direction (Path Taken) of the Parametric Function Respective Of The Parameter
def create_vector_points(origin, destination):
    origin_x = np.exp(origin)
    origin_y = np.exp(2*origin)
    destination_x = (np.exp(destination)) - (np.exp(origin))
    destination_y = (np.exp(2*destination)) - (np.exp(2*origin))
    return origin_x, origin_y, destination_x, destination_y

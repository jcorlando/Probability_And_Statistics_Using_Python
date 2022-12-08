import numpy as np


# Create Vectors (Tail & Head) => (origin,, destination) To Help Evaluate The
# Direction (Path Taken) of the Parametric Function Respective Of The Parameter
def create_vector_points(origin, destination):
    origin_x = 2*np.tan(origin)
    origin_y = 3*(1/(np.cos(origin)))
    destination_x = (2*np.tan(destination)) - (2*np.tan(origin))
    destination_y = (3*(1/(np.cos(destination)))) - (3*(1/(np.cos(origin))))
    return origin_x, origin_y, destination_x, destination_y

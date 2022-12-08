import numpy as np


# Create Vectors (Tail & Head) => (origin,, destination) To Help Evaluate The
# Direction (Path Taken) of the Parametric Function Respective Of The Parameter
def create_vector_points(origin, destination):
    origin_x = 500*np.cos(np.pi/6)*origin
    origin_y = 500*np.sin(np.pi/6)*origin - (1/2)*9.8*(origin**2)
    destination_x = (500*np.cos(np.pi/6)*destination) - (500*np.cos(np.pi/6)*origin)
    destination_y = (500*np.sin(np.pi/6)*destination - (1/2)*9.8*(destination**2)) - \
                    (500*np.sin(np.pi/6)*origin - (1/2)*9.8*(origin**2))
    return origin_x, origin_y, destination_x, destination_y

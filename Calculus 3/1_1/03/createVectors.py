
def create_vector_points(origin, destination):
    origin_x = (2*origin) + 4
    origin_y = origin - 1
    destination_x = ((2*destination) + 4) - ((2*origin) + 4)
    destination_y = (destination - 1) - (origin - 1)
    return origin_x, origin_y, destination_x, destination_y

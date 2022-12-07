
def create_vector_points(origin, destination):
    origin_x = (2*origin*origin)
    origin_y = (origin*origin*origin*origin) + 1
    destination_x = (2*destination*destination) - (2*origin*origin)
    destination_y = ((destination*destination*destination*destination) + 1) - ((origin*origin*origin*origin) + 1)
    return origin_x, origin_y, destination_x, destination_y

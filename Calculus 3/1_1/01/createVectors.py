
def create_vector_points(origin, destination):
    origin_x = (origin * origin) + (2 * origin)
    origin_y = origin + 1
    destination_x = ((destination * destination) + (2 * destination)) - ((origin * origin) + (2 * origin))
    destination_y = (destination + 1) - (origin + 1)
    return origin_x, origin_y, destination_x, destination_y

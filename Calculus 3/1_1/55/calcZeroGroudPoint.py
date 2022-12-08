import numpy as np


def calc_ground_zero_time():
    time = 3.0
    while (500*np.sin(np.pi/6)*time - (1/2)*9.8*(time**2)) > 0:
        time += 0.0001
    return time


def calc_ground_zero_distance(end_time):
    distance = 500*np.cos(np.pi/6)*end_time
    return distance

import math


def process_data(n, data):
    return [calc_distance(data[0], data[1]) for _ in range(n)]


def calc_distance(point_a, point_b):
    return math.sqrt(
        (point_b[0] - point_a[0]) ** 2
        + (point_b[1] - point_a[1]) ** 2
        + (point_b[2] - point_a[2]) ** 2
    )

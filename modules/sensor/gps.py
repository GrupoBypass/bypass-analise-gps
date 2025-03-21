import random


def get_position():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    z = random.randint(-100, 100)
    return x, y, z


def calc_distance(n):
    return [(
        get_position()[0] ** 2 + get_position()[1] ** 2 + get_position()[2] ** 2
    ) ** 0.5 for _ in range(n)]

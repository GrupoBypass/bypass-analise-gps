import random
import math


def get_position():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    z = random.randint(-100, 100)
    return x, y, z


def process_data(point_a, point_b):
    # Calcula a distancia entre dois pontos
    print ("process_data")    
    return math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2 + (point_b[2] - point_a[2]) ** 2)
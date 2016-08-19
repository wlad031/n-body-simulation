import random

# noinspection PyPep8Naming
from config import AppConfig as ac


def get_x(array):
    return array[0]


def get_y(array):
    return array[1]


# noinspection PyPep8Naming
def randomize_particles(num):
    res = []

    MAX_SPEED = 50
    MAX_MASS = 10000
    MIN_MASS = 1
    MAX_RADIUS = 5
    MIN_RADIUS = 1

    for i in range(num):
        randint = lambda: random.randint(0, 255)
        color = '#%02X%02X%02X' % (randint(), randint(), randint())

        res.append({
            'id': i,
            'position': [random.randint(0, ac['window_width']),
                         random.randint(0, ac['window_height'])],
            'speed': [random.randint(-MAX_SPEED, MAX_SPEED),
                      random.randint(-MAX_SPEED, MAX_SPEED)],
            'mass': random.randint(MIN_MASS, MAX_MASS),
            'radius': random.randint(MIN_RADIUS, MAX_RADIUS),
            'color': color,
        })

    return res

import numpy as np


class GravitationalSystem:
    # noinspection PyClassHasNoInit,PyUnresolvedReferences
    class Particle:
        id = 0
        acceleration = 0
        position = np.array([0, 0])
        speed = np.array([0, 0])
        mass = np.float32(0)
        radius = np.float32(1)
        color = 'black'

        def __str__(self):
            return (str(self.id) + ' ' +
                    str(self.position) + ' ' +
                    str(self.speed) + ' ' +
                    str(self.mass) + ' ' +
                    str(self.radius) + ' ' +
                    self.color)

    def __init__(self, particles, G, dt):
        self.particles = self.__parse_particles(particles)
        self.G = G
        self.dt = dt

    # noinspection PyPep8Naming,PyAugmentAssignment,PyTypeChecker
    def update_state(self):
        for p_i in self.particles:

            F = 0

            for p_j in self.particles:

                if p_i == p_j:
                    continue

                r = p_j.position - p_i.position
                r_ij = np.linalg.norm(r)
                F_ij = self.G * p_i.mass * p_j.mass / r_ij ** 3 * r

                F += F_ij

            p_i.acceleration = F / p_i.mass

            p_i.speed = p_i.speed + p_i.acceleration * self.dt
            p_i.position = p_i.position + p_i.speed * self.dt

    def get_particles(self):
        return self.particles

    def add(self, particle):
        self.particles += self.__parse_particles([particle])

    # noinspection PyMethodMayBeStatic
    def __parse_particles(self, arr):
        res = []

        # Available particle properties
        properties = {
            'id': int,
            'position': np.array,
            'speed': np.array,
            'mass': float,
            'radius': float,
            'color': str,
        }

        for p in arr:
            particle = self.Particle()

            # noinspection PyShadowingBuiltins
            for property in properties.keys():
                if p[property] is not None:
                    # :)))
                    setattr(particle, property,
                            properties[property](p[property]))

            res.append(particle)

        return res

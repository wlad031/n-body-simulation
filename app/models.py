import numpy as np
from helper import randomize_particles


class GravitationalSystem:
    # noinspection PyClassHasNoInit,PyUnresolvedReferences
    class Particle:
        id = 0
        acceleration = 0
        force = np.array([0, 0])
        position = np.array([0, 0])
        speed = np.array([0, 0])
        mass = np.float32(0)
        radius = np.float32(1)
        color = 'black'

        def __str__(self):
            return (' '.join(map(str, [self.id, self.position, self.speed, self.mass, self.radius, self.color])))

    def __init__(self, particles, g, dt):
        self.particles = self.__parse_particles(
            particles if particles != 'random' else randomize_particles(50))
        self.G = g
        self.dt = dt

    # noinspection PyPep8Naming,PyAugmentAssignment,PyTypeChecker
    def update_state(self):

        to_join = []

        for p_i in self.particles:

            p_i.force = 0

            for p_j in self.particles:

                if p_i == p_j:
                    continue

                r = p_j.position - p_i.position
                r_ij = np.linalg.norm(r)

                if r_ij <= p_i.radius + p_j.radius:
                    if {'first': p_j, 'second': p_i} not in to_join:
                        to_join.append({
                            'first': p_i,
                            'second': p_j,
                        })
                    break

                F_ij = self.G * p_i.mass * p_j.mass / r_ij ** 3 * r

                p_i.force += F_ij

            p_i.acceleration = p_i.force / p_i.mass
            p_i.speed = p_i.speed + p_i.acceleration * self.dt
            p_i.position = p_i.position + p_i.speed * self.dt

        for joining in to_join:
            particle = self.Particle()

            if joining['first'].mass >= joining['second'].mass:
                first = joining['first']
                second = joining['second']
            else:
                first = joining['second']
                second = joining['first']

            particle.position = first.position
            particle.mass = first.mass + second.mass
            particle.speed = (first.mass * first.speed +
                              second.mass * second.speed) / particle.mass
            particle.radius = first.radius + int(second.radius / 2)
            particle.color = first.color
            particle.id = self.particles[-1].id + 1

            self.particles.append(particle)
            self.particles.remove(joining['first'])
            self.particles.remove(joining['second'])

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

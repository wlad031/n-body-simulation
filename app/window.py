import time
import numpy as np
from Tkinter import *

from helper import *


class GravitationalSystemDrawer:
    __DEFAULT_ANIMATION_DELAY = 0.025
    __PAUSE = False

    def __init__(self, gravitational_system, window_width, window_height,
                 canvas_color):

        self.root = Tk()
        self.root.resizable(0, 0)
        self.canvas = Canvas(self.root, width=window_width,
                             height=window_height, bg=canvas_color)

        self.system = gravitational_system
        system_points = self.system.get_particles()
        self.points = []

        for particle in system_points:
            x = get_x(particle.position)
            y = get_y(particle.position)
            r = particle.radius
            color = particle.color

            # TODO more drawable objects (e.g. moving-vectors)

            self.points.append({
                'point': self.__create_point(x, y, r, color=color),
                'position': particle.position
            })

        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

    # noinspection PyBroadException
    def animation(self):
        while True:
            time.sleep(self.__DEFAULT_ANIMATION_DELAY)

            self.system.update_state()
            system_points = self.system.get_particles()

            for i in range(len(system_points)):
                delta = system_points[i].position - self.points[i]['position']
                dx = get_x(delta)
                dy = get_y(delta)

                try:
                    self.canvas.move(self.points[i]['point'], dx, dy)

                    pos = self.canvas.coords(self.points[i]['point'])

                    self.points[i]['position'] = np.array([
                        pos[0] + (pos[2] - pos[0]) / 2,
                        pos[1] + (pos[3] - pos[1]) / 2
                    ])

                    self.canvas.update()
                except Exception:
                    return

    def __update_elements(self, system_points):
        pass

    def __create_point(self, x, y, r, color):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color,
                                       outline=color)

    def __create_line(self, x1, x2, color):
        return self.canvas.create_line(get_x(x1), get_y(x1), get_x(x2),
                                       get_y(x2), fill=color)

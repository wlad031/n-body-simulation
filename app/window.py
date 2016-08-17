import time
import numpy as np

try:
    # noinspection PyUnresolvedReferences
    from Tkinter import *
except ImportError:
    # noinspection PyUnresolvedReferences
    from tkinter import *

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
        self.screen_elements = []

        self.__update_elements()

        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

    # noinspection PyBroadException
    def animation(self):
        while True:
            time.sleep(self.__DEFAULT_ANIMATION_DELAY)

            self.system.update_state()

            try:
                self.__update_elements()
                self.canvas.update()
            except Exception as e:
                print e
                return

    def __update_elements(self):
        system_points = self.system.get_particles()

        for system_point in system_points:
            found = False

            for element in self.screen_elements:

                if system_point.id != element['id']:
                    continue

                # Update screen elements

                delta = system_point.position - element['position']
                dx = get_x(delta)
                dy = get_y(delta)

                self.canvas.move(element['screen_point'], dx, dy)

                pos = self.canvas.coords(element['screen_point'])

                element['position'] = np.array([
                    pos[0] + (pos[2] - pos[0]) / 2,
                    pos[1] + (pos[3] - pos[1]) / 2
                ])

                found = True
                break

            # Add new elements, if needed
            if not found:
                # TODO more drawable objects (e.g. moving-vectors)

                self.screen_elements.append({
                    'id': system_point.id,
                    'screen_point': self.__create_point(
                        get_x(system_point.position),
                        get_y(system_point.position),
                        system_point.radius,
                        color=system_point.color),
                    'position': system_point.position
                })

    def __create_point(self, x, y, r, color):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color,
                                       outline=color)

    def __create_line(self, x1, x2, color):
        return self.canvas.create_line(get_x(x1), get_y(x1), get_x(x2),
                                       get_y(x2), fill=color)

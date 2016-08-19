import time

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
    __EXIT = False
    __SHOW_FORCE_LINES = False

    def __init__(self, gravitational_system, window_width, window_height,
                 canvas_color):

        self.root = Tk()
        self.root.resizable(0, 0)
        self.canvas = Canvas(self.root, width=window_width,
                             height=window_height, bg=canvas_color)

        self.gravitational_system = gravitational_system
        self.screen_elements = []

        self.__update_elements()

        self.canvas.pack()

        self.root.bind('f', self.__push_f)
        self.root.bind('p', self.__push_p)
        self.root.bind('<Escape>', self.__push_esc)

        self.root.protocol("WM_DELETE_WINDOW", self.__close)

        self.root.after(0, self.__animation)
        self.root.mainloop()

    # noinspection PyBroadException
    def __animation(self):
        while True:
            if self.__EXIT:
                break

            time.sleep(self.__DEFAULT_ANIMATION_DELAY)

            if not self.__PAUSE:
                self.gravitational_system.update_state()
                self.__update_elements()

            self.canvas.update()

    def __update_elements(self):
        system_points = self.gravitational_system.get_particles()

        self.canvas.delete('all')

        for system_point in system_points:
            self.screen_elements.append({
                'id': system_point.id,
                'screen_point': self.__create_point(
                    system_point.position,
                    system_point.radius,
                    system_point.color),
                'position': system_point.position
            })

            if self.__SHOW_FORCE_LINES:
                self.screen_elements[-1]['force'] = self.__create_line(
                    system_point.position,
                    system_point.position + system_point.force / 100,
                    system_point.color)

    def __create_point(self, x1, r, color):
        x, y = get_x(x1), get_y(x1)
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color,
                                       outline=color)

    def __create_line(self, x1, x2, color):
        return self.canvas.create_line(get_x(x1), get_y(x1), get_x(x2),
                                       get_y(x2), fill=color)

    # noinspection PyUnusedLocal
    def __push_f(self, event):
        self.__SHOW_FORCE_LINES ^= 1

    # noinspection PyUnusedLocal
    def __push_p(self, event):
        self.__PAUSE ^= 1

    # noinspection PyUnusedLocal
    def __push_esc(self, event):
        self.__EXIT = True
        self.root.withdraw()
        sys.exit(0)

    def __close(self):
        self.__push_esc(None)

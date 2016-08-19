from window import GravitationalSystemDrawer
from models import GravitationalSystem
# noinspection PyPep8Naming
from config import GravitationalSystemConfig as gsc, AppConfig as ac


class App:
    def __init__(self):
        self.system = GravitationalSystem(g=gsc.get('G', 6.0e-1),
                                          dt=gsc.get('dt', 0.1),
                                          particles=gsc.get('particles', []))

    def run(self):
        GravitationalSystemDrawer(self.system,
                                  window_width=ac.get('window_width', 640),
                                  window_height=ac.get('window_height', 480),
                                  canvas_color=gsc.get('color', '#222222'))

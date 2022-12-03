import math
from random import choice

class Body:

    G = 6.67408 * 10**-11
    colours = [(200, 200, 200), (200, 50, 50), (50, 200, 50), (50, 50, 200), (200, 200, 50), (200, 50, 200),
               (50, 200, 200), (0, 100, 200), (200, 0, 100), (100, 200, 0)]

    def __init__(self, x, y, init_vel_x, init_vel_y, mass, radius):
        self._x = x
        self._y = y
        self._x_velocity = init_vel_x
        self._y_velocity = init_vel_y
        self._mass = mass
        self.colour = choice(self.colours)
        self.radius = radius

    def move(self, delta):
        self._x += self._x_velocity * delta
        self._y += self._y_velocity * delta

    def update_acceleration(self, mass, x, y, delta):
        if x != self._x or y != self._y:
            x_disp, y_disp = x - self._x, y - self._y
            rsq = x_disp**2 + y_disp**2
            fg = (self.G * mass) / (rsq)
            theta = math.asin(y_disp / math.sqrt(rsq))
            fx_total = fg * math.cos(theta)
            fy_total = fg * math.sin(theta)
            fx_total = abs(fx_total)
            fy_total = abs( fy_total)
            if x_disp < 0:
                fx_total = -fx_total
            if y_disp < 0:
                fy_total = -fy_total
            self._x_velocity += fx_total * delta
            self._y_velocity += fy_total * delta

    def get_mass(self):
        return self._mass

    def get_coords(self):
        return (self._x, self._y)

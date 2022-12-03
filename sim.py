import body
import pygame as pg

class Universe:
    def __init__(self, *args):
        self.bodies = []
        for i in args:
            self.bodies.append(body.Body(i[0], i[1], i[2], i[3], i[4], i[5]))
            self.scale = 100

    def update_objects(self, delta):
        for bod in self.bodies:
            bod.move(delta)
        for bod in self.bodies:
            for b in self.bodies:
                if bod != b:
                    bod.update_acceleration(b.get_mass(), b.get_coords()[0], b.get_coords()[1], delta)

    def to_AU(self, meters):
        return (float(meters[0]) * 6.68459 * 10**-12 * self.scale + 250, float(meters[1]) * 6.68459 * 10**-12 * self.scale + 250)

    def zoom_in(self):
        if self.scale > 0.001:
            self.scale *= 0.4
            background = pg.Surface(screen.get_size())
            background.fill((0, 0, 0))
            screen.blit(background, (0, 0))

    def zoom_out(self):
        if self.scale < 100000:
            self.scale *= 2.5
            background = pg.Surface(screen.get_size())
            background.fill((0, 0, 0))
            screen.blit(background, (0, 0))

pg.init()

screen = pg.display.set_mode((500, 500))

#Binary star system and planets
uni = Universe((30_000_000_000, 0, 0, 600000, 9 * 10**32, 10), (-30_000_000_000, 0, 0, -600000, 9 * 10**32, 10), (-200_000_000_000, 0, 0, -800000, 10**10, 5), (250_000_000_000, 0, 0, 700000, 10**17, 7), (0, 340_000_000_000, 600000, 0, 10**20, 8))

# Earth and moon
#uni = Universe((0, 0, -12.57, 0, 5.972 * 10**24, 0.01), (0, 384_400_000, 1022, 0, 7.34767309 * 10**22, 0.003))

#Jupiter and moons
'''
jupiter = (0, 0, 0, 0, 1.898 * 10**27, 0.06)

adrastea = (0, 129_000_000, -31378, 0, 2 * 10**15, 0.002)
amalthea = (0, 181_365_840, -26570, 0, 2.08 * 10**18, 0.002)
metis = (0, -128_000_000, 31501, 0, 9.56 * 10**16, 0.002)
thebe = (0, -221_889_000, 23920, 0, 7.77 * 10*17, 0.002)

io = (420_000_000, 0, 0, 17406, 8.931938 * 10**22, 0.01)
callisto = (1_882_700_000, 0, 0, 8204, 1.075938 * 10**23, 0.01)
ganymede = (1_070_400_000, 0, 0, 10_880, 1.4819 * 10**23, 0.01)
europa = (670_900_000, 0, 0, 13743.36, 4.799844 * 10**22, 0.01)

themisto = (7_396_130_000, 0, 0, 4098, 6.89 * 10**14, 0.002)

leda = (-11_195_980_000, 0, 0, -3380, 5.68 * 10**15, 0.005)
ersa = (0, 	11_483_000_000, -3017, 0, 5 * 10**14, 0.005)
pandia = (0, -11_525_000_000, 3007, 0, 5 * 10**14, 0.005)
himalia = (11_388_690_000, 0, 0, 3340, 4.2 * 10**18, 0.007)
lysithia = (-11_700_710_000, 0, 0, -3263.392, 6.3 * 10**16, 0.005)
elara = (0, 11_703_130_000, -3290, 0, 8.7 * 10**17, 0.005)
dia = (0, -12_118_000_000, 3131.777778, 0, 8.7 * 10**16, 0.005)

carpo = (0, 16_989_000_000, -2582.778, 0, 44_960_052_992_916, 0.005)

ananke = (0, 21_042_470_000, -2420, 0, 38.2 * 10**15, 0.005)
aoede = (0, -23_981_000_000, 2178.19444, 0, 89_920_105_985_832, 0.005)
autonoe = (0, 23_039_000_000, -2237.94444, 0, 89_920_105_985_832, 0.05)
callirrhoe = (0, -24_583_090_000, -2263.056, 0, 869_227_691_196_372, 0.005)


aitne = (-23_231_000_000, 0, 0, 2280.833, 44_960_052_992_916, 0.005)
arche = (-22_931_000_000, 0, 0, 2282.222, 	44_960_052_992_916, 0.005)
carme = (-22_579_850_000, 0, 0, 2253, 1.3 * 10**17, 0.005)

uni = Universe(jupiter, io, callisto, ganymede, europa, adrastea, aitne, amalthea, ananke, aoede, arche, autonoe,
               callirrhoe, carme, metis, thebe, themisto, leda, ersa, pandia, himalia, lysithia, elara, dia, carpo)'''

# Sun and planets

#sun = (0, 0, 0, 0, 1.989 * 10**30, 20)

#mercury = (49.461 * 10**6 * 1000, 0, 0, -47362.5, 3.285 * 10**23, 1)

#venus = (-107.48 * 10**6 * 1000, 0, 0, 35021.3889, 4.867 * 10**24, 1)

#earth = (0, 147.27 * 10**6 * 1000, 29780, 0, 5.972 * 10**24, 1)
#moon = (384_400_000, 147.27 * 10**6 * 1000, 29780, 1023.056, 7.34767309 * 10**22, 0.5)

#mars = (0, -226.54 * 10**6 * 1000, -24130.833, 0, 6.39 * 10**23, 1)

#jupiter = (746.5 * 10**6 * 1000, 0, 0, -13060, 1.898 * 10**27, 10)

#saturn = (-1.408 * 10**9 * 1000, 0, 0, 9680, 5.683 * 10**26, 8)

#uranus = (0, 2.9493 * 10**9 * 1000, 6800, 0, 8.681 * 10**25, 7)

#neptune =  (0, -4.4747 * 10**9 * 1000, -5430, 0, 1.024 * 10**26, 7)

#pluto = (147.27 * 10**6 * 1000 * 39.5, 0, 0, 4670, 1.30900 * 10**22, 1)

#uni = Universe(sun, mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune, (147.27 * 10**6 * 1000 * 39.5, 0, 0, 4670, 1.30900 * 10**22, 1))


delta = 100
running = True
clock = pg.time.Clock()
screen.fill((20, 20, 20))

while running:
    clock.tick(1000)

    uni.update_objects(delta)

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                uni.zoom_out()
            elif event.button == 5:
                uni.zoom_in()

    background = pg.Surface(screen.get_size())
    background.set_alpha(50)
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for bod in uni.bodies:
        rad = 1
        if bod.radius*(0.01*uni.scale) > 1:
            rad = bod.radius*(0.01*uni.scale)
        pg.draw.circle(screen, bod.colour, uni.to_AU(bod.get_coords()), rad)

    pg.display.flip()

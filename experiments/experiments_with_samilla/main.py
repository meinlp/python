import matplotlib.pyplot as plt
from samila import GenerativeImage, Projection
import random
import math


def f1(x, y):
    result = random.uniform(-1, 1) * x ** 2 - math.sin(y ** 2) + random.gauss(0, 1)
    return result


def f2(x, y):
    result = random.uniform(-1, 1) * x ** 2 - math.cos(y ** 2) + random.gauss(0, 1)
    return result


def generate():
    g = GenerativeImage(f1, f2)
    g.generate(step=0.003, stop=0)
    g.plot(color="red", bgcolor="black", projection=Projection.MOLLWEIDE)
    # projections: RECTILINEAR, POLAR, AITOFF,
    # HAMMER, LAMBERT, MOLLWEIDE
    # plt.show()  # show in window
    g.save_image(file_adr='test_004.png', depth=3)  # save to file, depth is quality


generate()

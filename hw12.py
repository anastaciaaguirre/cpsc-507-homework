#Author: Anastacia Aguirre

import math

def volume(radius, height):
    area = math.pi * (radius ** 2) #area of the base of the cylinder
    volume = area * height #volume = area of base times height
    print(volume)

volume(10, 30)
#Author: Anastacia Aguirre

import math

def area_cr(radius):
    area = math.pi * (radius ** 2) #area = (pi)r^2
    return area

def area_sq(side):
    area = side ** 2 #area = r^2
    return area

def area_diff(radius, side):
    circle = area_cr(radius) #stores the area of the circle using previous function
    square = area_sq(side) #stores the area of the square using previous function
    diff = square - circle #finds the area of the gap between the square and circle
    print(diff)

area_diff(0.5, 1)
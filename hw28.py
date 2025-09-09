#Author: Anastacia Aguirre

# (HW28.py) Write a function that takes the longitude and latitude of two points and returns
# the Euclidean distance between them. How many parameters should your function take?

import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    in_radical = dx**2 + dy**2 #calculates value inside the radical
    answer = math.sqrt(in_radical)
    print(answer)


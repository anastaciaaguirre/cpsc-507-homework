#Author: Anastacia Aguirre

import math

def maturity(time, temp, ratio):
    a = 23.7 * (time**3)
    b = temp / 273
    c = math.log(ratio, math.e)
    ans = a + b + c #adds each segment of the formula for simplification
    print(ans)


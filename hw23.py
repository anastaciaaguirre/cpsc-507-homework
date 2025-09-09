#Author: Anastacia Aguirre

# (HW23.py) Write a function that compare three different numbers and returns the minimum.
# Call your function for 206, 405 and 112

def minimum(x, y, z):
    if x < y: #removes y from consideration
        if x < z:
            return x
        elif z < x:
            return z
    elif x < z: #removes z from consideration
        if x < y:
            return x
        elif y < x:
            return y
    else: #removes x from consideration
        if y < z:
            return y
        else:
            return z

print(minimum(206, 405, 112))

print(minimum(5, 25, 17))

print(minimum(6, 25, 170))
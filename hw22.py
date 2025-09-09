#Author: Anastacia Aguirre

# (HW22.py) Write a function that compares three different numbers and returns the maxi- mum.
# Call your function for 2, 25, and 17 .

def maximum(x, y, z):
    if x > z: #removes z from consideration
        if x > y:
            return x
        elif y > x:
            return y
    elif x > y: #removes y from consideration
        if x > z:
            return x
        elif z > x:
            return z
    else: #removes x from consideration
        if y > z:
            return y
        else:
            return z


print(maximum(29, 25, 17))

print(maximum(5, 25, 17))

print(maximum(5, 25, 170))
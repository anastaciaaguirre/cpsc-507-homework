#Author: Anastacia Aguirre

# (HW27.py) Use your factorial function and write a function that takes two parameters, n and r,
# and calculates the following formula: P(n,r) = (n!)/(n-r)!

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        recurse = factorial(n-1)
        total = n * recurse
        return total

# print(factorial(3))
# print(factorial(4-1))

def P(n, r):
    n = factorial(n) #calculates numerator
    d = factorial(n-r) #calculates deonimator
    answer = n/d
    print(answer)

print(factorial(5))
print(factorial(4))
print(factorial(5)/factorial(4))
P(5,1)


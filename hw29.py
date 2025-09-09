#Author: Anastacia Aguirre

# (HW29.py) Write a function that can take any 5 numbers and returns the average of these
# numbers. Check how your function is working for numbers: 2, 23, 56, 78, 901 .

def average(a, b, c, d, e):
    sum = a + b + c + d + e #calculates the numerator of the average formula
    answer = sum / 5 #calculates the average of the 5 numbers
    return answer

print(average(2, 23, 56, 78, 901))


#Author: Anastacia Aguirrev

#(HW25.py) Write a function that calculate the summation of the odd numbers between any two numbers,
# a and b. Check if the function is working for summation of odd numbers between 2 and 14 .

def is_odd(n): #cleans our code so we dont have to type this twice
    if n % 2 != 0:
        return True
    else:
        return False


def odd_summation(x, y):
    if x >= y-1:
        return 0
    if is_odd(x+1) == True: #tells us our x+1 value is odd, so whether or not we can add the first inbetween value
        if x >= y-1: #base rerturn value
            return 0
        return (x+1) + odd_summation(x+2, y) #since we determined our first inbetween value is odd, we can start there and move over 2 every time
    else: #tells us our x+1 value is even, so we cannot use this first inbetween value
        if x >= y-1: #base return value
            return 0
        return (x+2) + odd_summation(x+2, y) #since we determined x+1 is even, we move 2 over to start with the first odd number, then move over 2 each time

print(odd_summation(0, 4)) #1 + 3
print(odd_summation(2, 14)) #3 + 5 + 7 + 9 + 11 + 13
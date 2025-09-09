#Author: Anastacia Aguirre

# (HW24.py) Write a function that takes two numbers and Find the summation of all the numbers
# between these two numbers. Check how your function is working by passing 1 and 5 to it.
# What will you get if you pass 20 and 113 to your function?

def summation(x, y):
    if x >= y-1:
        return 0
    return (x+1) + summation(x+1, y)


print(summation(1, 5))
print(summation(20,113))


### Using while loop (for fun) ###
def summation(x, y):
    steps = abs(y - x)  #tells how many numbers we'll end up adding
    i = 1 #gives us a value to add to our start, will grow later
    sum = 0 #empty basket
    if x != y: #guardian
        while i < steps: #only want to find the sum of the numbers inbetween
            if x < y: #ensures we're starting low and working up
                value = x + i #gives us the value we add to our sum. starts with one step up because thats the first number we want
                sum += value #actual adding of part
                i += 1 #moves us along 1 step so we add the following number
            elif y < x: #ensures we're starting high and working low
                value = x - i #gives us the next value to the "left" that we want to add
                sum += value #actual addition
                i += 1 #moves us alone 1 step so we add the following number (ln 23 makes it actually go to the left)
        print(sum)
    else: #guardian
        print(0)


# summation(2, 7)

# summation(1, 5)
#
# summation(5, 1)
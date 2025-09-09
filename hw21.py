#Author: Anastacia Aguirre

# (HW21.py) Write a function that checks if a number is divisible by 5 or not.
# If it was, returns "Yes, it is!" , and if it wasn't, return "No, it is not!"

def div5(n):
    if n % 5 == 0:
        print("Yes, it is!")
    else:
        print("No, it is not!")


div5(15)
div5(7)
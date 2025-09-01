#Author: Anastacia Aguirre

def BMI(inches, pounds):
    result = (pounds/(inches**2)) * 703 #the constant 703 is used for customary to metric conversions
    return result

print(BMI(60, 142.5))
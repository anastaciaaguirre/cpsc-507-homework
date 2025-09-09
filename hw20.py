#Author: Anastacia Aguirre

# (HW20.py) Write a function takes a number grade as its parameter and returns the corre- sponding letter grade.

def letter_grade(n_grade):
    if n_grade >= 93:
        print("A")
    elif n_grade >= 90:
        print("A-")
    elif n_grade >= 87:
        print("B+")
    elif n_grade >= 83:
        print("B")
    elif n_grade >= 80:
        print("B-")
    elif n_grade >= 77:
        print("C+")
    elif n_grade >= 73:
        print("C")
    elif n_grade >= 70:
        print("C-")
    elif n_grade >= 65:
        print("D+")
    elif n_grade >= 55:
        print("D")
    elif n_grade >= 50:
        print("D-")
    else:
        print("F")

letter_grade(94)
letter_grade(91)
letter_grade(88)
letter_grade(84)
letter_grade(81)
letter_grade(78)
letter_grade(74)
letter_grade(71)
letter_grade(66)
letter_grade(56)
letter_grade(52)
letter_grade(30)

#Author: Anastacia Aguirre

# (HW26.py) Write a function that takes the temperature and if the temperature was above 78
# asks you to turn on the AC and if the temperature was below 62 asks you to turn on the heater.
# For temperature greater than or equal to 62 and less than or equal to 78, tells you "it's a wonderful weather!" .

def thermostat(temp):
    if temp > 78: #above 78
        print("Please turn on the AC")
    elif temp < 68: #below 68
        print("Please turn on the heater")
    else: #between 78 and 68, inlcuding the ends
        print("It's a wonderful day!")

thermostat(89)
thermostat(78)
thermostat(73)
thermostat(68)
thermostat(50)
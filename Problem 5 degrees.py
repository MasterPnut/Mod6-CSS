#Ryne Bigueras
#2/26/22

#Problem 4:Search the internet for how to convert radians to degrees.
#Write a program to compute the conversion given a user input value.
#Print this value as well as the calculated value
#using the degrees function in the math module.


import math

r = float(input("Give a radians: "))

d = r * (180/math.pi)

print(d)


print(math.degrees(r))

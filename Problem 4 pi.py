#Ryne Bigueras
#2/26/22

#Problem 4:Search on the internet for a way to calculate an approximation for pi.
#There are many that use simple arithmetic.
#Write a program to compute the approximation and then print that value as well
#as the value of math.pi from the math module.

def pi():
    pi = 0
    b = 4
    c = 1
    for i in range(1, 1000000):
        a = 2 * ( i % 2 ) - 1
        pi += a * b / c
        c += 2
    print(pi)

pi()


import math

print (math.pi)

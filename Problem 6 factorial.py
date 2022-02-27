#Ryne Bigueras
#2/26/22

#Problem 6:Use a for statement to calculate the factorial of a user input value.
#Print this value as well as the calculated value
#using the factorial function in the math module.

import math

def calculating(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
value = int(input(" Please enter any Value : "))

f = calculating(value)
print("Factorial", f)


print ("Factorial", math.factorial(value))


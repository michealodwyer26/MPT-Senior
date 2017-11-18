'''
This program solves the quadriatic eaquation by useing the b formula
Inputs: a, b, c as float
Outputs: x1, x2
'''

# import modules
import math
import cmath # module to work with complex numbers

# function to solve the equation
def solveQuadraticEquation():
    '''
    solveEquation uses the b-formula to find the solutions
    of a quadratic equation
    '''

    # input a, b, c

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # calculate d
    d = b ** 2 - 4 * a * c

    # d positive gives real roots; d negative gives comlex roots
    if d >= 0:

        # calculate x1
        x1 = (-b - math.sqrt(d)) / (2 * a)

        # calculate x2
        x2 = (-b + math.sqrt(d)) / (2 * a)

    else:
        # calculate x1
        x1 = (-b - cmath.sqrt(d)) / (2 * a)

        # calculate x2
        x2 = (-b + cmath.sqrt(d)) / (2 * a)

    # end if
        

    # print x1, x2
    print("x1 = ", x1)
    print("x2 = ", x2)

def solveEquation():
    '''
    solveEquation uses the b-formula to find the solutions
    of a quadratic equation
    '''

    # input a, b, c

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # calculate d
    d = b ** 2 - 4 * a * c

    # calculate x1
    x1 = (-b - math.sqrt(d)) / (2 * a)

    # calculate x2
    x2 = (-b + math.sqrt(d)) / (2 * a)

    # print x1, x2
    print("x1 = ", x1)
    print("x2 = ", x2)


# end def

solveQuadraticEquation()

# -*- coding: utf-8 -*-
"""
Created on Wed Jul  23 20:50:51 2023

@author: echon
"""

def MCintegrate(f, a, b, n):
    """
    
    Parameters
    ----------
    f : TYPE function
    f returns a float between a and b
    a : TYPE float
    DESCRIPTION: lower limit
    b : TYPE float
    DESCRIPTION: upper limit
    n : TYPE int
    DESCRIPTION: number of random points to take in the box
    Returns
    -------
    integral of f from a to b
    
    """
    from random import random 
        
    # random returns a random number between 0 and 1

    maxF = 3

    area = 0
    saveX = []
    for i in range(n):

        # generate a random point in the boxc
        # x between a and b
        # z between 0 and maxF
        randNoX = random()*(b-a) + a
        randNoY = random()*maxF
        saveX.append(randNoX)
        saveX.append(randNoY)
        print(randNoX, randNoY)

        if randNoY <= f(randNoX): area += 1

    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    print(min(saveX), max(saveX))
    return(integral)


if __name__ == "__main__":

    # import numpy as np
    # import matplotlib.pyplot as plt
    def f(x):
        return x**2

area = MCintegrate(f, 0, 3., 500000)

print(round(area, 2))
print(f'Area {area: 0.2f}')


def trap(f, a, b, n):
    h = (b - a) / n  
    integral = 0.5 * (f(a) + f(b))  
 
    for i in range(1, n):
        x = a + i * h
        integral += f(x)  
 
    integral *= h  
    return integral
 
 
def f(x):
    return x ** 2
 
a = 0  
b = 2  
n = 100  
 
result = trap(f, a, b, n)
print("Approximate integral:", result)
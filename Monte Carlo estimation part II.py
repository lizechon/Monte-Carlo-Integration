# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:20:37 2023

@author: echon
"""

import numpy as np
import matplotlib.pyplot as plt
import MonteCarlo_Double as mc

def f(x, y):
     return x**2 + y**2
 
def g(x, y):
     return x**2 + y**2 - 1.5**2
 
 
x0, x1 = -1.5, 1.5
y0, y1 = -1.5, 1.5
 
n = 2500
 
area = mc
print("Area of the circle with radius 1.5:", area)
 
 
theta = np.linspace(0, 2*np.pi, 100)
x_circle = 1.5 * np.cos(theta)
y_circle = 1.5 * np.sin(theta)
 
plt.figure(figsize=(6, 6))
plt.scatter(np.random.uniform(x0, x1, n), np.random.uniform(y0, y1, n), s=1, color='c', alpha=0.5)
plt.plot(x_circle, y_circle, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Monte Carlo Integration of Circle')
plt.grid(True)
plt.show()
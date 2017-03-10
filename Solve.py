#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Main Entrance and Engine for Solving Schrodinger Equation Numerically
# Author: Robert Brown, Changkai Zhang
# Starting March, 2017

# import packages
import numpy as np
import matplotlib.pyplot as plt

# import support files
from Potential import potential
from InitCond import initial
from Schrodinger import TimeRate_WaveFunc


# -----------------------------------------------
#           Range and Step Size Setup
# -----------------------------------------------
# min x, max x, number of x points
xrange = (-1,2,100)
# min t, max t, number of time points
trange = (0,1,500)
# time & space steps
dx, dt = [(k[1] - k[0])/k[2] + 0j for k in (xrange, trange)]


# -----------------------------------------------
#                Generate Grids
# -----------------------------------------------
# vector of x coordinates of spatial points
x = np.linspace(xrange[0], xrange[1], xrange[2])
# vectorize V function to allow it to act on each element of x array
vec_potential = np.vectorize(potential)
# calculate potential at each point xi
V = vec_potential(x)


# -----------------------------------------------
#           Initialize Solution Data
# -----------------------------------------------
# array to store x points, contains 2 rows to store prior time level
psi = np.empty([xrange[2],2], dtype=complex)


# -----------------------------------------------
#              Solve the Equation
# -----------------------------------------------
# boundary conditions
psi[:,0] = initial(x) # set initial wavefunction to gaussian
dx2 = complex(dx**2)

# iterate over every time
for j in range(1001):
    # Runge-Kutta 3
    k1 = dt * TimeRate_WaveFunc(psi[:,0], V, dx2)
    k2 = dt * TimeRate_WaveFunc(psi[:,0] + k1/2, V, dx2)
    k3 = dt * TimeRate_WaveFunc(psi[:,0] + k2/2, V, dx2)
    psi[:,0] = psi[:,0] + 1/6 * k1 + 2/3 * k2 + 1/6 * k3
    psi[:,0] /= max(psi[:,0])


# -----------------------------------------------
#           Visualization of Solution
# -----------------------------------------------
fig = plt.figure()
plt.plot(x,np.absolute(psi[:,0]),'r')
plt.title(r"Characteristic time: {}".format(j))

plt.show()

# End of File

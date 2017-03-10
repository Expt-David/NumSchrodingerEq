#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Main Entrance and Engine for Solving Schrodinger Equation Numerically
# Author: Robert Brown, Changkai Zhang
# Starting March, 2017

# import packages
import numpy as np

def TimeRate_WaveFunc(psi, V, dx2):
    # supposed to return an approximation of ∂Ψ/∂t
    x = np.empty([len(psi),], dtype=complex)
    for i in range(len(psi)):
        imax=len(psi)-1
        if i == 0:
            x[i] = 0.5j/dx2 * (psi[0] + psi[2] - 2*psi[1]) - 1j * V[i]
        elif i == imax:
            x[i] = 0.5j/dx2 * (psi[imax] + psi[imax-2] - 2*psi[imax-1])/dx2 - 1j * V[i]
        else:
            x[i] = 0.5j/dx2 * (psi[i-1] - 2*psi[i] + psi[i+1])/dx2 - 1j * V[i]
    return x

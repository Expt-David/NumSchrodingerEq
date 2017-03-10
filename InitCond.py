#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Inital Condition Setup
# Author: Robert Brown, Changkai Zhang
# Starting March, 2017

# import packages
import numpy as np

def initial(x):
    # initial state (guassian)
    var = 0.001
    # return np.sin(x*np.pi)
    return 1/np.sqrt(2*np.pi*var) * np.exp(-(x - 0.5)**2/(2*var))

# End of File

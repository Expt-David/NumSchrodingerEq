#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Potential Setup
# Author: Robert Brown, Changkai Zhang
# Starting March, 2017

import numpy as np

def potential(x):
    # infinite square well potential
    # return 0 if 0 < x < 1 else float("inf") # square well
    return 0    # free particle
    # return x**2 # harmonic potential

# End of File

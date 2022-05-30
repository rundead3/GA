# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:36:20 2022

@author: João Correia
"""

import numpy as np

matrix = np.loadtxt("data.txt",skiprows=1)


# d_data -> A matrix with the descriptors 
d_data = []
for i in range(len(matrix)):
    d_data.append(matrix[i][:-1])


# b_data -> A vector with the Bioavailability 
b_data = []
for i in range(len(matrix)):
    b_data.append(matrix[i][-1])
    


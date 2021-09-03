from tqdm import tqdm
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import animation
def applyrules(sizex, sizey,Nn, array):
    for i in range(sizex):
        for j in range(sizey):
            if array[i,j]==1:
                if ( Nn[i,j] < 2) or (Nn[i,j] > 3):
                    array[i,j] = 0
            else:
                if Nn[i,j] == 3:
                    array[i,j] = 1
                    
    return array


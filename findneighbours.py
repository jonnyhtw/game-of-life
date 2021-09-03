from tqdm import tqdm
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import animation
import numpy as np

def findneighbours(sizex, sizey, array):

    Nn = np.zeros(shape = (sizex,sizey))#number of neighbours

    for i in range(sizex):
        
        for j in range(sizey):

            Nn[i,j] = np.sum( [

                array[i-1, j-1], 
                array[i, j-1], 
                array[i+1-sizex*(i==sizex-1), j-1],

                array[i-1, j],
                array[i+1-sizex*(i==sizex-1), j],

                array[i-1, j+1-sizey*(j==sizey-1)],
                array[i, j+1-sizey*(j==sizey-1)],
                array[i+1-sizex*(i==sizex-1), j+1-sizey*(j==sizey-1)]
            ])
            
    return Nn



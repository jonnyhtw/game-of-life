
import sys
sys.executable





import numpy as np
import matplotlib.pyplot as plt
import copy
import animatplot as amp
from matplotlib import animation

import warnings
warnings.filterwarnings("ignore")




def applyrules(size,Nn, array):
    for i in range(size):
        for j in range(size):
            if array[i,j]==1:
                if Nn[i,j] < 2:# Any live cell with fewer than two
                               #live neighbours dies, as if by underpopulation.
                    array[i,j] = 0
                elif Nn[i,j] == 2:# Any live cell with two or three
                                                      # live neighbours lives on to the next generation.
                    array[i,j] = 1
                elif Nn[i,j] == 3:
                    array[i,j] = 1
                elif Nn[i,j] > 3:# Any live cell with more than three
                                 # live neighbours dies, as if by overpopulation.
                    array[i,j] = 0
            if array[i,j]==0:
                if Nn[i,j] == 3:# Any dead cell with exactly three
                                #live neighbours becomes a live cell, as if by reproduction.
                    array[i,j] = 1
                    
    return array




def findneighbours(size, array):

    Nn = np.zeros(shape = (size,size))#number of neighbours

    for i in range(size):
        
        for j in range(size):

            Nn[i,j] = np.sum( [

                array[i-1, j-1], 
                array[i, j-1], 
                array[i+1-size*(i==size-1), j-1],

                array[i-1, j],
                array[i+1-size*(i==size-1), j],

                array[i-1, j+1-size*(j==size-1)],
                array[i, j+1-size*(j==size-1)],
                array[i+1-size*(i==size-1), j+1-size*(j==size-1)]                    

            ])
            

    return Nn




def plotarray(x):

    myplot = plt.imshow(x, cmap = 'Greys')

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    ax.tick_params(axis=u'both', which=u'both',length=0)

    return myplot




size = 100


init = 'rand'

if init == 'glider':

    array = np.zeros(shape = (size,size))
    array[0, 1:4] = 1
    array[1, 3] = 1
    array[2, 2] = 1

if init == 'rand':

    array = np.round(np.random.rand(size,size))

gens = 10

arrays = []

fig = plt.figure(figsize=[5,5])

import matplotlib
matplotlib.use('Agg')

for i in range(gens):    

    print('generation '+str(i))

    Nn = findneighbours(size, array)

    arrays.append(applyrules(size,Nn, array))

    ax = plt.subplot(1,1,1,aspect = 'equal')

    plotarray(array)

    plt.title('generation ' + str(i))

    plt.gca().invert_yaxis()

    plt.savefig('{:04}'.format(i)+'.png')#,dpi=1000)


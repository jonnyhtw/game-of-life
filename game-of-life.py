from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import copy
import animatplot as amp
from matplotlib import animation


def applyrules(sizex, sizey,Nn, array):
    for i in range(sizex):
        for j in range(sizey):
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

def plotarray(x):

    myplot = plt.imshow(x, cmap = 'Greys')

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    ax.tick_params(axis=u'both', which=u'both',length=0)

    return myplot

sizex = 50
sizey = 50

gun = np.flipud(np.array([
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                       [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                       [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                       ]))
array = np.zeros(shape = (size,size))

for i in range(gun.shape[0]):
    for j in range(gun.shape[1]):
        array[i+20,j+10] = gun[i,j]

gens = 1000

fig = plt.figure(figsize=[5,5])

import matplotlib
matplotlib.use('Agg')

for i in tqdm(range(gens)):

    print('generation '+str(i))

    Nn = findneighbours(sizex, sizey, array)

    array = applyrules(sizex, sizey,Nn, array)

    if init == 'gun':
        array[0,:] = 0
        array[-1,:] = 0
        array[:,0] = 0
        array[0:,-1] = 0

    ax = plt.subplot(1,1,1,aspect = 'equal')

    plotarray(array[2:-2,2:-2])

    plt.title('generation ' + str(i))

    plt.gca().invert_yaxis()

    plt.savefig('{:04}'.format(i)+'.png',dpi=100)

    plt.close()


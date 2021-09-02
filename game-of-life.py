from tqdm import tqdm
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

sizex = 40
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
array = np.zeros(shape = (sizex,sizey))

for i in range(gun.shape[0]):
    for j in range(gun.shape[1]):
        array[i+25,j+5] = gun[i,j]

gens = 500

fig = plt.figure(figsize=[5,5])


for i in tqdm(range(gens)):

    print('generation '+str(i))

    Nn = findneighbours(sizex, sizey, array)

    array = applyrules(sizex, sizey,Nn, array)

    ax = plt.subplot(1,1,1,aspect = 'equal')

    plotarray(array[2:-2,2:-2])

    plt.title('generation ' + str(i))

    plt.gca().invert_yaxis()

    plt.savefig('{:04}'.format(i)+'.png',dpi=100)

    plt.close()


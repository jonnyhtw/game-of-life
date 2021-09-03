from tqdm import tqdm
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import animation

from applyrules import applyrules
from plotarray import plotarray
from findneighbours import findneighbours


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

    array[0,:] = 0
    array[1,:] = 0
    array[2,:] = 0
    array[-1,:] = 0
    array[-2,:] = 0
    array[-3,:] = 0
    array[:,0] = 0
    array[:,1] = 0
    array[:,2] = 0
    array[:,-1] = 0
    array[:,-2] = 0
    array[:,-3] = 0

    ax = plt.subplot(1,1,1,aspect = 'equal')

    myplot = plt.imshow(array[2:-2,2:-2], cmap = 'Greys')

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    ax.tick_params(axis=u'both', which=u'both',length=0)
#    plotarray(array[2:-2,2:-2])

    plt.title('generation ' + str(i))

    plt.gca().invert_yaxis()

    plt.savefig('{:04}'.format(i)+'.png',dpi=100)

    plt.close()

os.system('rm 0000.png')
os.system('convert *.png game-of-life.gif')
os.system('rm *.png')

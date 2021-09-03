from tqdm import tqdm
import glob
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import animation

from applyrules import applyrules
from findneighbours import findneighbours

sizex = 50
sizey = 50

gun = np.genfromtxt('gun.txt')

array = np.zeros(shape = (sizex,sizey))

for i in range(gun.shape[0]):
    for j in range(gun.shape[1]):
        array[i+25,j+5] = gun[i,j]

gens = 200

for i in tqdm(range(gens)):

    print('generation '+str(i))

    Nn = findneighbours(sizex, sizey, array)

    array = applyrules(sizex, sizey,Nn, array)

    array[0,:] = array[-1,:] = array[:,0] = array[:,-1] = 0

    myplot = plt.pcolor(array, cmap = 'Greys')

    plt.title('generation ' + str(i))

    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig('{:04}'.format(i)+'.png',dpi=100)


    plt.close()

# filepaths
fp_in = "./*.png"
fp_out = "./game-of-life.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=100, loop=0)

os.system('rm *.png')


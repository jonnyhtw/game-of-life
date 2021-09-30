import copy
from tqdm import tqdm
from tqdm import tqdm_gui
import glob
from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import animation
import matplotlib
matplotlib.use('Agg')

plt.ion()

from applyrules import applyrules
from findneighbours import findneighbours

sizex = 50
sizey = 50

_gun = False

if _gun == True:

    gun = np.genfromtxt('gun.txt')

    array = np.zeros(shape = (sizex,sizey))

    for i in range(gun.shape[0]):
        for j in range(gun.shape[1]):
            array[i+25,j+5] = gun[i,j]

else:

    array = np.random.choice([0,1],(sizex,sizey))

gens = int(1e2)

coverage = np.mean(array)

for i in range(gens):

    #    ax = plt.subplot(1,2,1)
    fig, (ax1, ax2) = plt.subplots(1,2, constrained_layout=True)

    print('generation '+str(i+1)+' of '+str(gens)+' generations!' )

    Nn = findneighbours(sizex, sizey, array)

    array = applyrules(sizex, sizey,Nn, array)

    if _gun:

        array[0,:] = array[-1,:] = array[:,0] = array[:,-1] = 0

        plotarray = array[2:-3,2:-3]

    else:
        plotarray = copy.deepcopy(array)

    ax1.imshow(plotarray, cmap = 'Greys', aspect = 'auto')

    if _gun == False:

        randx = np.random.randint(0,sizex-1)
        randy = np.random.randint(0,sizey-1)

        array[randx, randy] = 1

        #plt.scatter(randx, randy, color = 'b', s = 100, alpha = 0.1,)

    plt.title('generation ' + str(i))

    ax1.get_xaxis().set_ticks([])
    ax1.get_yaxis().set_ticks([])

    coverage = np.append(coverage, (np.mean(plotarray))) 

   # ax = plt.subplot(1,2,2)

    ax2.plot(coverage)
    plt.xlim(0,gens)
    plt.ylim(0,0.2)

    plt.savefig('{:04}'.format(i)+'.png',dpi=100)


#    plt.tight_layout()

    plt.close()

# filepaths
fp_in = "./*.png"
fp_out = "./game-of-life.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=100, loop=0)

os.system('rm *.png')


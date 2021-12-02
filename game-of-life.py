import copy
import cartopy.crs as ccrs
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

os.system('rm *.png')

sizex = 360
sizey = 180

array = np.random.choice([0,1],(sizex,sizey))
array = np.zeros((sizex,sizey))

gens = int(360)

for i in range(gens):

    ax = plt.subplot(1,1,1,projection = ccrs.Orthographic(central_longitude = 174.7787+i, central_latitude = 0))

    print('generation '+str(i+1)+' of '+str(gens)+' generations!' )

    Nn = findneighbours(sizex, sizey, array)

    array = applyrules(sizex, sizey,Nn, array)

    plotarray = copy.deepcopy(array)

    xs, ys = np.where(plotarray.astype(bool))

    plt.scatter(xs - 180, ys - 90, s = 1 , alpha = 0.5, transform = ccrs.PlateCarree(), c = 'r')

    ax.coastlines()
    ax.stock_img()
    
    if i == 0:

        for j in range(int(sizex*sizey/100)):

            randx = np.random.randint(0,sizex-1)
            randy = np.random.randint(0,sizey-1)

            if (randx <= sizex - 2 - 1) and (randy <= sizey - 2 - 1):
            
                array[randx:randx+3, randy] = 1
                array[randx+2, randy+1] = 1
                array[randx+1, randy+2] = 1

    plt.title('generation ' + str(i))

    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])

    plt.savefig('{:04}'.format(i)+'.png',dpi=100)

    plt.close()

# filepaths
fp_in = "./*.png"
fp_out = "./game-of-life.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)

os.system('rm *.png')

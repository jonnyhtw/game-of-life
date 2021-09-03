from tqdm import tqdm
import os
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import animation

def plotarray(x):

    myplot = plt.imshow(x, cmap = 'Greys')

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    ax.tick_params(axis=u'both', which=u'both',length=0)

    return myplot


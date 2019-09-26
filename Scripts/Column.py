import os
import pandas as pd
import numpy as np
from scipy import ndimage
from scipy import misc
from PicObj import p
from PicObj import Pic
from PicObj import *
from GameMap import *

"""Here I am looking at a sample user's game and """
os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\410screens\\0')
df = pd.read_csv("rollout.csv")
os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\410screens\\0\\screens')

def add():
    xlist = []
    ylist = []
    tilelist = []
    snake_x = []
    snake_y = []
    monster_x = []
    monster_y = []
    for file in df.index:
        p.choosepic(str(file) + ".png")

        """
            Qbert's mean x and y locations, and tile number.
            PIL uses a coordinate system with (0, 0) in the upper left corner.
        """
        if p.isqbertin():
            xlist.append(p.qbertmean()[1])
            ylist.append(p.qbertmean()[0])
            if overallboard.reverselook(p) is not None:
                tilelist.append(overallboard.reverselook(p))
            else:
                tilelist.append(0)
        else:
            xlist.append(0)
            ylist.append(0)
            tilelist.append(0)

        """
            The snake's mean x and y locations, and tile number.
        """
        if p.issnakein():
            snake_x.append(p.snakemean()[1])
            snake_y.append(p.snakemean()[0])
        else:
            snake_x.append(0)
            snake_y.append(0)

        """
            The monster's mean x and y locations, and tile number.
        """
        if p.ismonsterin():
            monster_x.append(p.monstermean()[1])
            monster_y.append(p.monstermean()[0])
        else:
            monster_x.append(0)
            monster_y.append(0)

    df["qbert_x"] = xlist
    df["qbert_y"] = ylist
    df["qbert_tile"] = tilelist
    df["snake_x"] = snake_x
    df["snake_y"] = snake_y
    df["monster_x"] = monster_x
    df["monster_y"] = monster_y
    os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\410screens\\0')
    df.to_csv('out.csv')

"""filedict = {}
for filename in os.listdir(os.getcwd()):
    p.choosepic(filename)
    filedict[filename] = p.qbertmean()"""

import os
import pandas as pd
import numpy as np
from scipy import ndimage
from scipy import misc

os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\409screens')
default = misc.imread("0.png")
pic = default

colors = []

def choosepic(file):
    """Method to assign the pic variable to a file in your current working directory"""
    global pic
    pic = misc.imread(file)
    print("There are " + str(pic.shape[0]) + " rows, " + str(pic.shape[1]) + " columns.")
    return pic

"""
    There are 210 rows, 160 columns, and 3 color channels. The 3 color channels are RGB.
    We are looking for the QBert figure. We need to figure out what color he is.
    Then we need to find him in the image. The default is set to, 0.png, the gameboard with no characters on it.
    Sample files in my directory:
    colormatchQBERT.png is the gameboard with QBERT and the green snake.
"""

def counttile():
    """Method to count the number of tiles with a particular pixel color"""
    tiles = 0
    for j in range(pic.shape[0] - 1):
        for i in range(pic.shape[1] - 1):
            if pic[j][i][0]==45 and pic[j][i][1]==87 and pic[j][i][2]==176:
                tiles += 1
    return tiles


def isqbertin():
    """
    Method to indicate whether QBERT is in the photo
    potential issue - the color of QBERT could occur somewhere else
    """
    yes = False
    for j in range(pic.shape[0] - 1):
        for i in range(pic.shape[1] - 1):
            if pic[j,i][0]==181 and pic[j,i][1]==83 and pic[j,i][2]==40:
                yes = True
    return yes

def diffcolor():
    """This returns a list of the distinct RBG colors in the gameboard, as lists"""
    colors = []
    for j in range(pic.shape[0] - 1):
        for i in range(pic.shape[1] - 1):
            if [pic[j][i][0],pic[j][i][1],pic[j][i][2]] not in colors:
                colors.append([pic[j][i][0],pic[j][i][1],pic[j][i][2]])
    return colors

def colorlocs():
    """
    Boolean method to check if QBert is in the photo,
    also prints each pixel coordinate
    """
    bool = False
    for j in range(pic.shape[0] - 1):
        for i in range(pic.shape[1] - 1):
            if pic[j,i][0]==181 and pic[j,i][1]==83 and pic[j,i][2]==40:
                bool = True
                print([j,i])
    if bool==False:
        print("QBert is not in this photo.")
    else:
        print("These are the locations of QBert's colors, [row,col].")

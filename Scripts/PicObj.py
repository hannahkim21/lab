import os
import pandas as pd
import numpy as np
from scipy import ndimage
from scipy import misc

"""I have downloaded the screencaps from user 409's game. This command changes
#the directory so that we can access the image files."""
os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\409screens')
"""Let's make sure we're in the right place!
#Right now this isn't generalized, it just works for the directory I saved pictures in.
"""
print("Right now we're in " + str(os.getcwd()) + ".")

class Pic(object):
    def __init__(self, file, pic=None, shape=[], colors=[], qbertloc=[]):
        self.file = file
        self.pic = pic
        self.shape = shape
        self.colors = colors
        self.qbertloc = qbertloc

    """These methods update the instance attributes of the Pic object:
        - SciPy image object
        - color list.
        - Qbert's color locations
    """
    def choosepic(self, file):
        newpic = misc.imread(file)
        self.file = file
        self.pic = newpic
        self.shape = newpic.shape
        self.colors = self.colorlist()
        self.qbertloc = self.colorlocs()

    """A list of the discinct colorways in a photo"""
    def colorlist(self):
        color = []
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                if [self.pic[j][i][0],self.pic[j][i][1],self.pic[j][i][2]] not in color:
                    color.append([self.pic[j][i][0],self.pic[j][i][1],self.pic[j][i][2]])
        return color

    def colorlocs(self):
        """Identify QBERT's locations"""
        colorlocs = []
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                    if self.pic[j,i][0]==181 and self.pic[j,i][1]==83 and self.pic[j,i][2]==40:
                        colorlocs.append([j,i])
        return colorlocs

    def snakelocs(self):
        """Identify snake's locations"""
        colorlocs = []
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                    if self.pic[j,i][0]==146 and self.pic[j,i][1]==70 and self.pic[j,i][2]==192:
                        colorlocs.append([j,i])
        return colorlocs

    def monsterlocs(self):
        """Identify monster's locations"""
        colorlocs = []
        li = [[138, 12], [138, 13], [138, 14], [138, 15], [138, 16], [138, 17], [138, 18], [138, 19], [138, 140], [138, 141], [138, 142], [138, 143], [138, 144], [138, 145], [138, 146], [138, 147], [139, 12], [139, 13], [139, 14], [139, 15], [139, 16], [139, 17], [139, 18], [139, 19], [139, 140], [139, 141], [139, 142], [139, 143], [139, 144], [139, 145], [139, 146], [139, 147]]
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                    if self.pic[j,i][0]==50 and self.pic[j,i][1]==132 and self.pic[j,i][2]==50:
                        if [j,i] not in li:
                            colorlocs.append([j,i])
        return colorlocs

    def qbertmean(self):
        """QBERT's mean location"""
        if self.isqbertin():
            arr = np.array(self.qbertloc)
            return [np.mean(arr[:,0]), np.mean(arr[:,1])]
        else:
            return None

    def snakemean(self):
        """Snake's mean location"""
        if self.issnakein():
            arr = np.array(self.snakelocs())
            return [np.mean(arr[:,0]), np.mean(arr[:,1])]
        else:
            return None

    def monstermean(self):
        """Monster's mean location"""
        if self.ismonsterin():
            arr = np.array(self.monsterlocs())
            return [np.mean(arr[:,0]), np.mean(arr[:,1])]
        else:
            return None

    """These methods describe the image:
        - isqbertin() tells if QBert is in the image
        - issnakein() tells if the snake is in the image
        - ismonsterin() tells if the monster is in the image
    """
    def isqbertin(self):
        yes = False
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                if self.pic[j,i][0]==181 and self.pic[j,i][1]==83 and self.pic[j,i][2]==40:
                    yes = True
        return yes

    def issnakein(self):
        yes = False
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                if self.pic[j,i][0]==146 and self.pic[j,i][1]==70 and self.pic[j,i][2]==192:
                    yes = True
        return yes

    def ismonsterin(self):
        li = [[138, 12], [138, 13], [138, 14], [138, 15], [138, 16], [138, 17], [138, 18], [138, 19], [138, 140], [138, 141], [138, 142], [138, 143], [138, 144], [138, 145], [138, 146], [138, 147], [139, 12], [139, 13], [139, 14], [139, 15], [139, 16], [139, 17], [139, 18], [139, 19], [139, 140], [139, 141], [139, 142], [139, 143], [139, 144], [139, 145], [139, 146], [139, 147]]
        yes = False
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                if self.pic[j,i][0]==50 and self.pic[j,i][1]==132 and self.pic[j,i][2]==50:
                    if [j,i] not in li:
                        yes = True
        return yes

    def lives(self):
        list = []
        for j in range(self.pic.shape[0] - 1):
            for i in range(self.pic.shape[1] - 1):
                if self.pic[j,i][0]==210 and self.pic[j,i][1]==210 and self.pic[j,i][2]==64:
                    list.append([j,i])
        return list

    """This method is a text description of the Pic object."""
    def describe(self):
        print("We are looking at " + str(self.file) + ".")
        print("There are " + str(self.pic.shape[0]) + " rows, " + str(self.pic.shape[1]) + " columns.")
        print("The colors are " + str(self.colors) + " .")
        inclusion  = ""
        inclusion2 = ""
        inclusion3 = ""
        bool = self.isqbertin()
        if bool==False:
            inclusion = "not "
        print("QBert is " + inclusion + "in the picture.")
        bool2 = self.issnakein()
        if bool2==False:
            inclusion2 = "not "
        print("The snake is " + inclusion2 + "in the picture.")
        bool3 = self.ismonsterin()
        if bool3==False:
            inclusion3 = "not "
        print("The monster is " + inclusion3 + "in the picture.")

"""Here we construct a default Pic object for convenience, called p.
This object can be used as a variable updated to whichever photo you want to look at.
Call p.describe() in command prompt for more information.
"""
p = Pic("0.png", None, "", [], [])
p.choosepic(p.file)

score_locs = [
[6, 35],
[6, 36],
[6, 37],
[6, 43],
[6, 44],
[6, 45],
[6, 53],
[6, 58],
[6, 59],
[6, 60],
[6, 61],
[6, 62],
[6, 66],
[6, 67],
[6, 68],
[6, 69],
[6, 70],
[7, 34],
[7, 38],
[7, 42],
[7, 46],
[7, 52],
[7, 53],
[7, 62],
[7, 66],
[8, 34],
[8, 38],
[8, 42],
[8, 46],
[8, 51],
[8, 53],
[8, 61],
[8, 66],
[8, 67],
[8, 68],
[8, 69],
[9, 34],
[9, 38],
[9, 42],
[9, 46],
[9, 50],
[9, 53],
[9, 60],
[9, 70],
[10, 34],
[10, 38],
[10, 42],
[10, 46],
[10, 50],
[10, 51],
[10, 52],
[10, 53],
[10, 54],
[10, 59],
[10, 70],
[11, 34],
[11, 38],
[11, 42],
[11, 46],
[11, 53],
[11, 59],
[11, 66],
[11, 70],
[12, 35],
[12, 36],
[12, 37],
[12, 43],
[12, 44],
[12, 45],
[12, 53],
[12, 59],
[12, 67],
[12, 68],
[12, 69]]

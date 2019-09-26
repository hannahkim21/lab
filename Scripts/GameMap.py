import os
import pandas as pd
import numpy as np
from scipy import ndimage
from scipy import misc
import PicObj
from PicObj import p
from PicObj import Pic
from PicObj import *

class Gameboard(object):

    def __init__(self, colorname, piclist, board):
        self.colorname = colorname
        self.piclist = piclist
        self.board = board

    def whichbox(self, coords):
        """Tells you which box a set of coordinates is in"""
        for key, value in self.board.items():
            for x in value:
                if x==coords:
                    print(key)

    def add(self, numstring, filestring):
        if filestring is None:
            self.board[numstring] = "Nothing there"
            self.piclist.append(None)
        if filestring is not None:
            pic = Pic(filestring, None, None, [], [])
            pic.choosepic(pic.file)
            self.piclist.append(pic)
            self.board[numstring] = pic.qbertloc

    def gothrough(self):
        for key, value in self.colorname.items():
        #if value is not None:
            self.add(key, value)

class Overall(Gameboard):
    #Here args will refer to the other gameboard objects
    #This is just a method for the overall board construction
    def __init__(self, colorname, piclist, board, mean):
        Gameboard.__init__(self, colorname, piclist, board)
        self.mean = mean

    #FIXME
    #I want it to go through all of the boards I set up, and check
    #for any values that aren't nothing, and add them to my overall
    #board. Issue - is adding the wrong value list
    #Make a while loop and set a bool to if I've fixed it yet?
    """Issue: updates the keys in self.board with the last value
    in arg.board for all of the keys"""
    def combine(self, *args):
        for key, value in self.board.items():
            if (value=="Nothing there"):
                for arg in args:
                    for key2,val2 in arg.board.items():
                        if (val2!="Nothing there"):
                            if (key==key2):
                                self.board[key] = val2

        for pic in self.piclist:
            for arg in args:
                if arg.piclist[self.piclist.index(pic)] is not None:
                    self.piclist[self.piclist.index(pic)] = arg.piclist[self.piclist.index(pic)]

        self.meanlist()

    def reverselook(self, pic):
        #Given a picture, find the location of Qbert
        #changedir os.chdir(file path) 'C:\\Users\\hkhan\\Documents\\CAL SP 2019\\scripts\\411screens'
        # so that im not checking on the same pics that i made it on
        reach = False
        save_loc = pic.qbertloc
        for key, value in self.board.items():
            if (type(value)==list):
                for item in value:
                    for loc in save_loc:
                        if (item==loc):
                            reach = True
                            return key

        if not reach:

    def meanlist(self):
        x = []
        for i in self.piclist:
            x.append(i.qbertmean())
        self.mean = x

"""Make a Pic object for each tile and save the locations of QBert's colors.
Use: Pic(file, pic, shape, colors, qbertloc)"""


"""Instantiate the gameboard object with an empty dictionary."""
g = Gameboard({}, [], {})

os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\409screens')
"""Instantiate the gameboard object with relevant files for user 409."""
u_409 = Gameboard({
"1" : "60.png",
"2" : "80.png",
"3" : "46.png",
"4" : None,
"5" : "94.png",
"6" : "428.png",
"7" : None,
"8": None,
"9" : "109.png",
"10" : "439.png",
"11" : None,
"12" : None,
"13" : None,
"14" : "176.png",
"15" : None,
"16" : None,
"17" : None,
"18" : None,
"19" : None,
"20" : "247.png",
"21" : None,
}, [], {})
u_409.gothrough()

os.chdir('C:\\Users\\hkhan\\Documents\\CollinsLab\\Screens\\410screens')
print("Right now we're in " + str(os.getcwd()) + ".")

u_410 = Gameboard({
"1" : None,
"2" : None,
"3" : None,
"4" : "76.png",
"5" : None,
"6" : None,
"7" : "273.png",
"8": "282.png",
"9" : None,
"10" : None,
"11" : "640.png",
"12" : "328.png",
"13" : "478.png",
"14" : None,
"15" : "263.png",
"16" : "413.png",
"17" : "435.png",
"18" : "460.png",
"19" : "483.png",
"20" : None,
"21" : "170.png",
}, [], {})
u_410.gothrough()

overallboard = Overall({
"1" : None,
"2" : None,
"3" : None,
"4" : None,
"5" : None,
"6" : None,
"7" : None,
"8": None,
"9" : None,
"10" : None,
"11" : None,
"12" : None,
"13" : None,
"14" : None,
"15" : None,
"16" : None,
"17" : None,
"18" : None,
"19" : None,
"20" : None,
"21" : None,
}, [], {}, [])
overallboard.gothrough()
overallboard.combine(u_409, u_410)

"""Get enough user information to map locations of all of the tiles. Then combine that into one
dictionary (this dictionary is stored as the attribute overallboard.board) so that I can reverse look up the location of Qbert given:
    - a photo
    - qbert's colors
I will use his colors to look up locations of that color in the photo. Then I will match the locations
of his colors to the location dictionary. Not sure it will overlap entirely: issues could be that he is inbetween
tiles so only some of them match. Another issue could be the direction he is facing.
This method will return the location of qbert.
"""

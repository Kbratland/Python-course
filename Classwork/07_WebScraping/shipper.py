from webbrowser import *
from random import *

searchString = ""
numRange = randint(0,25)
for lp in range(numRange):
    searchString = ""
    for lp in range(0,15):
        searchString +=  chr(randint(ord('a'), ord('z')))
    open("https://ship.shapewright.com/?name="+searchString)
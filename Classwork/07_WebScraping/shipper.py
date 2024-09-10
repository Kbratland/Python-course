from webbrowser import *
from random import *

searchString = ""
for lp in range(25):
    searchString = ""
    for lp in range(0,randint(1,5)):
        searchString +=  chr(randint(ord('a'), ord('z')))
        searchString +=  chr(randint(ord('A'), ord('Z')))
        searchString += str(randint(0,99))
    open("https://ship.shapewright.com/?name="+searchString)
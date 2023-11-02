from webbrowser import *
from pyperclip import *
from random import *

searchString = ""
random = False
sType = 3
if random:
    numRange = randint(0,25)
    for lp in range(numRange):
        searchString = ""
        searchString +=  chr(randint(ord('a'), ord('z')))
        searchString +=  chr(randint(ord('a'), ord('z')))
        searchString +=  chr(randint(ord('a'), ord('z')))
        open("https://google.com/search?q="+searchString)
else:
    if sType == 1:
        searchString = "weather in "+ paste()
        open("https://google.com/search?q=" + searchString)
    elif sType == 2:
        searchString = paste()
        open("https://www.google.com/maps/search/" + searchString)
    elif sType == 3:
        searchString = paste()
        #Common code resources
        open("https://stackoverflow.com/search?q="+searchString,2)
        open("https://www.codeguru.com/?s="+searchString,2)
        open("https://google.com/search?q="+searchString,2)
    elif sType == 4:
        pass
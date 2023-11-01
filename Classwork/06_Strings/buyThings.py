from re import *
from pyperclip import *

def makeShopList(text = "I want 9 jars of pickles, 7 cheeses,  I could use about 4 waffles, and 3 beans, maybe also pickup 82 fish."):
    listString = []
    outText = ""
    buyReg = compile(r"\d+\D+[?.\,|\.]")
    for groups in buyReg.findall(text):
        listString.append("\n"+groups)
    for lp in range(len(listString)):
        listString[lp] = listString[lp][:len(listString[lp])-1] 
    outText = " ".join(listString)
    return outText

print(makeShopList(paste()))

    
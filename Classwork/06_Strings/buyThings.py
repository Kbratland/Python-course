from re import *
from pyperclip import *

def makeShopList(text):
    listString = []
    buyReg = compile(r"\d+\s\w+")
    for groups in buyReg.findall(text):
        listString.append("\n"+groups) 
    return listString


temp = ("I want 9 pickles 7 cheeses,  I could use about 4 waffles and 3 beans, maybe also pickup 82 fish")
listTemp = (makeShopList(paste()))
for lp in range(len(listTemp)):
    print(listTemp[lp])
    